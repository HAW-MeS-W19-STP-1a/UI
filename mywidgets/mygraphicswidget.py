from PyQt5.QtCore import QDateTime
from mywidgets.dateaxisitem import DateAxisItem
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui


class MyGraphicsWidget():
    def __init__(self, plotWidget, label, data1, data2, dateTimeArray):
        self._pw = plotWidget
        self._ylabelLeft = "axis 1"
        self._ylabelRight = "axis 2"
        self._ylabelStyleLeft = {'color': '#00ff00', 'font-size': '20px'}
        self._ylabelStyleRight = {'color': '#ff0000', 'font-size': '20px'}
        self._font = QtGui.QFont()
        self._font.setPixelSize(18)
        self._label = label
        self._data1 = data1
        self._data2 = data2
        self._dateTimeArray = dateTimeArray
        self._axis = DateAxisItem(orientation="bottom")
        self._axis.attachToPlotItem(self._pw.getPlotItem())

        self._p1 = self._pw.plotItem

        # create a new Viewbox, link the right axis to its coordinate system
        self._vb2 = pg.ViewBox()
        self._p2 = pg.PlotCurveItem(x=self._dateTimeArray,
                                    y=self._data2,
                                    pen="r")
        self._vb2.addItem(self._p2)
        self._p1.showAxis("right")
        self._p1.scene().addItem(self._vb2)
        self._p1.getAxis("right").linkToView(self._vb2)
        self._vb2.setXLink(self._p1)

        self.updateViews()
        self._p1.vb.sigResized.connect(self.updateViews)
        self._vLine = pg.InfiniteLine(angle=90, movable=False)
        self._hLine = pg.InfiniteLine(angle=0, movable=False)
        self._p1.addItem(self._vLine, ignoreBounds=True)
        self._p1.addItem(self._hLine, ignoreBounds=True)
        self._proxy = pg.SignalProxy(self._p1.scene().sigMouseMoved,
                                     rateLimit=60,
                                     slot=self.mouseMoved)
        self.setYLabels("axis 1", "axis 2")
        self._p1.getAxis("left").tickFont = self._font
        self._p1.getAxis("right").tickFont = self._font
        self._p1.getAxis("bottom").tickFont = self._font
        self._p1.plot(x=self._dateTimeArray, y=self._data1, pen="g")

    # Handle view resizing:
    def updateViews(self):
        # view has resized; update auxilliary views to match
        self._vb2.setGeometry(self._p1.vb.sceneBoundingRect())

        # need to re-update linked axes since this was called
        # incorrectly while views had different shaped
        self._vb2.linkedViewChanged(self._p1.vb, self._vb2.XAxis)

    def mouseMoved(self, evt):
        if len(self._dateTimeArray) > 2:
            pos = evt[0]
            if self._p1.sceneBoundingRect().contains(pos):
                mousePoint = self._p1.vb.mapSceneToView(pos)
                dt = int(mousePoint.x())
                if dt > 0 and dt < self._dateTimeArray.max():
                    dt, index = self.find_nearest(self._dateTimeArray, dt)
                    self._label.setText(
                        "<span style='font-size: 12pt'>%s :   <span style='color: green'>%s = %0.3f</span>  ;  <span style='color: red'>%s = %0.3f</span>"
                        % (QDateTime.fromSecsSinceEpoch(dt).toString(
                            "dd.MM.yyyy hh:mm:ss"), self._ylabelLeft,
                           self._data1[index], self._ylabelRight,
                           self._data2[index]))
                self._vLine.setPos(dt)
                self._hLine.setPos(mousePoint.y())

    def find_nearest(self, array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx], idx

    def updateGraphs(self, data1, data2, dateTimeArray):
        self._data1 = data1
        self._data2 = data2
        self._dateTimeArray = dateTimeArray
        self._p1.plot(x=self._dateTimeArray,
                      y=self._data1,
                      pen="g",
                      clear=True)
        self._p1.addItem(self._vLine, ignoreBounds=True)
        self._p1.addItem(self._hLine, ignoreBounds=True)
        self._vb2.removeItem(self._p2)
        self._p2 = pg.PlotCurveItem(x=self._dateTimeArray,
                                    y=self._data2,
                                    pen="r")
        self._vb2.addItem(self._p2)

    def setXLim(self, dt_min, dt_max):
        self._p1.vb.setRange(xRange=(dt_min.toSecsSinceEpoch()-60*60,
                                     dt_max.toSecsSinceEpoch()-60*60))

    def setYLabels(self, ylabelLeft, ylabelRight):
        self._ylabelLeft = ylabelLeft
        self._ylabelRight = ylabelRight

        self._p1.setLabel("left", ylabelLeft, **self._ylabelStyleLeft)
        self._p1.setLabel("right", ylabelRight, **self._ylabelStyleRight)
