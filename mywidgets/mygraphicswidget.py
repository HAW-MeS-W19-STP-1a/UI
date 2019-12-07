from PyQt5.QtCore import QDateTime
from mywidgets.dateaxisitem import DateAxisItem
import numpy as np
import pyqtgraph as pg


class MyGraphicsWidget():
    def __init__(self, plotWidget, label, data1, data2, dateTimeArray):
        self._pw = plotWidget
        self._label = label
        self._data1 = data1
        self._data2 = data2
        self._dateTimeArray = dateTimeArray
        self._axis = DateAxisItem(orientation="bottom")
        self._axis.attachToPlotItem(self._pw.getPlotItem())

        self._p1 = self._pw.plotItem
        self._p1.setLabels(left="axis 1")

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
        self._p1.getAxis("right").setLabel("axis 2", color="#ff0000")

        self.updateViews()
        self._p1.vb.sigResized.connect(self.updateViews)
        self._vLine = pg.InfiniteLine(angle=90, movable=False)
        self._hLine = pg.InfiniteLine(angle=0, movable=False)
        self._p1.addItem(self._vLine, ignoreBounds=True)
        self._p1.addItem(self._hLine, ignoreBounds=True)
        self._proxy = pg.SignalProxy(self._p1.scene().sigMouseMoved,
                                     rateLimit=60,
                                     slot=self.mouseMoved)

        self._p1.plot(x=self._dateTimeArray, y=self._data1, pen="g")

    # Handle view resizing:
    def updateViews(self):
        # view has resized; update auxilliary views to match
        self._vb2.setGeometry(self._p1.vb.sceneBoundingRect())

        # need to re-update linked axes since this was called
        # incorrectly while views had different shaped
        self._vb2.linkedViewChanged(self._p1.vb, self._vb2.XAxis)

    def mouseMoved(self, evt):
        pos = evt[0]
        if self._p1.sceneBoundingRect().contains(pos):
            mousePoint = self._p1.vb.mapSceneToView(pos)
            dt = int(mousePoint.x())
            if dt > 0 and dt < self._dateTimeArray.max():
                dt, index = self.find_nearest(self._dateTimeArray, dt)
                self._label.setText(
                    "<span style='font-size: 12pt'>x=%s,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>"
                    % (QDateTime.fromSecsSinceEpoch(dt).toString(
                        "dd.MM.yyyy hh:mm:ss"), self._data1[index],
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
