from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot, QDateTime
from views.main_view_ui import Ui_MainWindow
import pyqtgraph as pg
from mywidgets.mygraphicswidget import MyGraphicsWidget
import pandas as pd


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._gw = MyGraphicsWidget(self._ui.graphicsView,
                                    self._ui.graphicsLabel, self._model.y1,
                                    self._model.y2, self._model.x)

        # connect widgets to controller
        # buttons
        self._ui.pushButton_clear_window.clicked.connect(
            self._main_controller.clear_console_window)
        self._ui.pushButton_update.clicked.connect(
            self._main_controller.on_update_timer_expired)
        # menu actions
        self._ui.action_enable_debug.triggered.connect(
            lambda: self._main_controller.set_debug_mode(True))
        self._ui.action_disable_debug.triggered.connect(
            lambda: self._main_controller.set_debug_mode(False))
        self._ui.action_enable_com.triggered.connect(
            lambda: self._main_controller.set_com_mode(True))
        self._ui.action_disable_com.triggered.connect(
            lambda: self._main_controller.set_com_mode(False))

        self._ui.action_set_update_interval_5_sec.triggered.connect(
            lambda: self._main_controller.set_update_int((5 * 1000)))
        self._ui.action_set_update_interval_1_min.triggered.connect(
            lambda: self._main_controller.set_update_int((60 * 1000)))
        self._ui.action_set_update_interval_15_min.triggered.connect(
            lambda: self._main_controller.set_update_int((15 * 60 * 1000)))
        self._ui.action_set_update_interval_1_h.triggered.connect(
            lambda: self._main_controller.set_update_int((60 * 60 * 1000)))
        self._ui.action_set_update_interval_manuel.triggered.connect(
            lambda: self._main_controller.set_update_int(-1))

        self._ui.action_set_view_custom.triggered.connect(
            lambda: self._main_controller.set_view_time_int("custom"))
        self._ui.action_set_view_1_minute.triggered.connect(
            lambda: self._main_controller.set_view_time_int("1min"))
        self._ui.action_set_view_15_minute.triggered.connect(
            lambda: self._main_controller.set_view_time_int("15min"))
        self._ui.action_set_view_1_h.triggered.connect(
            lambda: self._main_controller.set_view_time_int("1h"))
        self._ui.action_set_view_1_d.triggered.connect(
            lambda: self._main_controller.set_view_time_int("1d"))
        self._ui.action_set_view_1_w.triggered.connect(
            lambda: self._main_controller.set_view_time_int("1w"))
        self._ui.action_set_view_1_m.triggered.connect(
            lambda: self._main_controller.set_view_time_int("1m"))

        # Console Window
        self._ui.line_send_command.returnPressed.connect(
            lambda: self.on_send_command_returnPressed(
                self._ui.line_send_command.text()))

        # listen for model event signals
        self._model.com_mode_changed.connect(self.on_com_mode_changed)
        self._model.data_changed.connect(self.on_data_changed)
        self._model.debug_mode_changed.connect(self.on_debug_mode_changed)
        self._model.update_int_changed.connect(self.on_update_int_changed)
        self._model.view_time_int_changed.connect(
            self.on_view_time_int_changed)
        self._model.view_dateTime_start_changed.connect(
            self.on_view_dateTime_start_changed)
        self._model.view_dateTime_stop_changed.connect(
            self.on_view_dateTime_stop_changed)
        self._model.console_buffer_changed.connect(
            self.on_command_buffer_changed)

        # set a default value
        self._main_controller.set_debug_mode(True)
        self._main_controller.set_com_mode(False)
        self._main_controller.set_view_time_int("1h")
        self._main_controller.set_update_int(-1)

    @pyqtSlot(bool)
    def on_com_mode_changed(self, value):
        self._ui.action_enable_com.setChecked(value)
        self._ui.action_disable_com.setChecked(not value)

    @pyqtSlot(pd.DataFrame)
    def on_data_changed(self, value):
        self._ui.tableWidget.setData(value.transpose().to_dict())
        self.update_graph()

    @pyqtSlot(bool)
    def on_debug_mode_changed(self, value):
        self._ui.action_enable_debug.setChecked(value)
        self._ui.action_disable_debug.setChecked(not value)

    @pyqtSlot(int)
    def on_update_int_changed(self, value):
        self._ui.action_set_update_interval_5_sec.setChecked(value == (5 *
                                                                       1000))
        self._ui.action_set_update_interval_1_min.setChecked(value == (60 *
                                                                       1000))
        self._ui.action_set_update_interval_15_min.setChecked(
            value == (15 * 60 * 1000))
        self._ui.action_set_update_interval_1_h.setChecked(value == (60 * 60 *
                                                                     1000))
        self._ui.action_set_update_interval_manuel.setChecked(value == -1)

    @pyqtSlot(str)
    def on_view_time_int_changed(self, value):
        self._ui.action_set_view_custom.setChecked(value == "custom")
        self._ui.action_set_view_1_minute.setChecked(value == "1min")
        self._ui.action_set_view_15_minute.setChecked(value == "15min")
        self._ui.action_set_view_1_h.setChecked(value == "1h")
        self._ui.action_set_view_1_d.setChecked(value == "1d")
        self._ui.action_set_view_1_w.setChecked(value == "1w")
        self._ui.action_set_view_1_m.setChecked(value == "1m")

        if value == "custom":
            self._ui.dateTimeEdit_start.setReadOnly(False)
            self._ui.dateTimeEdit_stop.setReadOnly(False)
        else:
            self._ui.dateTimeEdit_start.setReadOnly(True)
            self._ui.dateTimeEdit_stop.setReadOnly(True)

    @pyqtSlot(QDateTime)
    def on_view_dateTime_start_changed(self, value):
        if self._model.view_time_int != "custom":
            self._ui.dateTimeEdit_start.setDateTime(value)

    @pyqtSlot(QDateTime)
    def on_view_dateTime_stop_changed(self, value):
        if self._model.view_time_int != "custom":
            self._ui.dateTimeEdit_stop.setDateTime(value)

    @pyqtSlot(str)
    def on_command_buffer_changed(self, value):
        self._ui.textBrowser_Console.setText(value)

    def on_send_command_returnPressed(self, value):
        self._main_controller.send_command(value)
        self._ui.line_send_command.clear()

    # def pyqtgraphdemo(self):
    #     # axis = da.DateAxis(orientation="bottom")
    #     # self._ui.graphicsView.AxisItems={"bottom":axis}
    #     self.pw = self._ui.graphicsView
    #     self.pw.setTitle("This is just a test")
    #     self.axis = DateAxisItem(orientation="bottom")
    #     self.axis.attachToPlotItem(self.pw.getPlotItem())
    #     self.p1 = self.pw.plotItem
    #     self.p1.setLabels(left="axis 1")

    #     # create a new Viewbox, link the right axis to its coordinate system
    #     self.p2 = pg.ViewBox()
    #     self.p1.showAxis("right")
    #     self.p1.scene().addItem(self.p2)
    #     self.p1.getAxis("right").linkToView(self.p2)
    #     self.p2.setXLink(self.p1)
    #     self.p1.getAxis("right").setLabel("axis 2", color="#ff0000")

    #     self.updateViews(self.p1, self.p2)
    #     self.p1.vb.sigResized.connect(
    #         lambda: self.updateViews(self.p1, self.p2))

    #     self.p1.plot(x=self._model.x, y=self._model.y1)
    #     self.p2.addItem(
    #         pg.PlotCurveItem(x=self._model.x, y=self._model.y2, pen="r"))

    #     self.vLine = pg.InfiniteLine(angle=90, movable=False)
    #     self.hLine = pg.InfiniteLine(angle=0, movable=False)
    #     self.p1.addItem(self.vLine, ignoreBounds=True)
    #     self.p1.addItem(self.hLine, ignoreBounds=True)
    #     self.label = self._ui.graphicsLabel
    #     self.proxy = pg.SignalProxy(
    #         self.p1.scene().sigMouseMoved,
    #         rateLimit=60,
    #         slot=lambda evt: self.mouseMoved(evt, self.p1, self.label, self.
    #                                          vLine, self.hLine, self._model.y1,
    #                                          self._model.y2, self._model.x))

    # def mouseMoved(self, evt, plot, label, vLine, hLine, data1, data2,
    #                dateTime):
    #     pos = evt[0]
    #     if plot.sceneBoundingRect().contains(pos):
    #         mousePoint = plot.vb.mapSceneToView(pos)
    #         dt = int(mousePoint.x())
    #         if dt > 0 and dt < dateTime.max():
    #             dt, index = self.find_nearest(dateTime, dt)
    #             label.setText(
    #                 "<span style='font-size: 12pt'>x=%s,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>"
    #                 % (QDateTime.fromSecsSinceEpoch(dt).toString("dd.MM.yyyy hh:mm:ss"), data1[index], data2[index]))
    #         vLine.setPos(dt)
    #         hLine.setPos(mousePoint.y())

    # def find_nearest(self, array, value):
    #     array = np.asarray(array)
    #     idx = (np.abs(array - value)).argmin()
    #     return array[idx], idx

    # # Handle view resizing:
    # def updateViews(self, p1, p2):
    #     # view has resized; update auxilliary views to match
    #     p2.setGeometry(p1.vb.sceneBoundingRect())

    #     # need to re-update linked axes since this was called
    #     # incorrectly while views had different shaped
    #     p2.linkedViewChanged(p1.vb, p2.XAxis)

    def update_graph(self):
        # p1 = self._ui.graphicsView.plot()
        # p1.setPen((200, 200, 100))
        self._ui.graphicsView.plot(
            y=self._model.data["t_bme"].tolist(),
            # x=self._model.data["DateTime"].tolist(),
            clear=True)
        print("temp:" + str(self._model.data["t_bme"].tolist()))
        print("dateTime:" + str(self._model.data["DateTime"].tolist()))
