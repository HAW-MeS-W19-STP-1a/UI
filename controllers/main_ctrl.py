from PyQt5.QtCore import QObject, pyqtSlot, QDateTime, QTimer


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model
        self._update_timer = QTimer(self)
        self._update_timer.timeout.connect(self.on_update_timer_expired)
        self._update_timer.start(self._model.update_int)

    def clear_console_window(self):
        if self._model.debug_mode:
            print("Clear Window Button pressed.")
        # TODO: clear console window

    def set_debug_mode(self, value):
        print("Setting Debug Mode to " + str(value))
        self._model.debug_mode = value
        self.update_view_dateTime()

    def set_view_time_int(self, value):
        if self._model.debug_mode:
            print("Changing view time interval to " + str(value))
        self._model.view_time_int = value
        self.update_view_dateTime()

    def set_update_int(self, value):
        if self._model.debug_mode:
            print("Changing update interval to " + str(value))
        self._update_timer.stop()
        self._model.update_int = value
        if self._model.update_int != -1:
            self._update_timer.start(self._model.update_int)

    def update_view_dateTime(self):
        if self._model.debug_mode:
            print("Updating view DateTime")

        if self._model.view_time_int == "custom":
            # TODO implement custom view time
            pass
        else:
            self._model.view_dateTime_stop = QDateTime.currentDateTimeUtc()
            if self._model.view_time_int == "1min":
                self._model.view_dateTime_start = \
                    self._model.view_dateTime_stop.addSecs(-60)
            elif self._model.view_time_int == "15min":
                self._model.view_dateTime_start = \
                    self._model.view_dateTime_stop.addSecs(-(60 * 15))
            elif self._model.view_time_int == "1h":
                self._model.view_dateTime_start = \
                    self._model.view_dateTime_stop.addSecs(-(60 * 60))
            elif self._model.view_time_int == "1d":
                self._model.view_dateTime_start = \
                    self._model.view_dateTime_stop.addDays(-1)
            elif self._model.view_time_int == "1w":
                self._model.view_dateTime_start = \
                    self._model.view_dateTime_stop.addDays(-7)
            elif self._model.view_time_int == "1m":
                self._model.view_dateTime_start = \
                    self._model.view_dateTime_stop.addMonths(-1)

    def on_update_timer_expired(self):
        # TODO get the new Data from the station
        self.update_view_dateTime()
        if self._model.update_int != -1:
            self._update_timer.start(self._model.update_int)
    # @pyqtSlot(int)
    # def change_amount(self, value):
    #     self._model.amount = value

    #     # calculate even or odd
    #     self._model.even_odd = 'odd' if value % 2 else 'even'

    #     # calculate button enabled state
    #     self._model.enable_reset = True if value else False
