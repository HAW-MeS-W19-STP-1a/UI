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
            print("Clearing Console Window")
        self._model.console_buffer = ""

    def add_to_console_buffer(self, value):
        if self._model.debug_mode:
            print("Adding to console_buffer: " + str(value))
        self._model.console_buffer = self._model.console_buffer + str(
            value) + "\r\n"

    def set_com_mode(self, value):
        if self._model.debug_mode:
            print("Setting com_mode to: " + str(value))
        self._model.com_mode = value

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

    def send_command(self, value):
        if self._model.com_mode:
            # TODO Implement sending of commands
            if self._model.debug_mode:
                print("Sending command: " + str(value))
        self.add_to_console_buffer("-> " + str(value))

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
