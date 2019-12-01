from PyQt5.QtCore import QObject, pyqtSignal, QDateTime


class Model(QObject):
    amount_changed = pyqtSignal(int)
    debug_mode_changed = pyqtSignal(bool)
    even_odd_changed = pyqtSignal(str)
    enable_reset_changed = pyqtSignal(bool)
    update_int_changed = pyqtSignal(int)
    view_time_int_changed = pyqtSignal(str)
    view_dateTime_start_changed = pyqtSignal(QDateTime)
    view_dateTime_stop_changed = pyqtSignal(QDateTime)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
        self.amount_changed.emit(value)

    @property
    def debug_mode(self):
        return self._debug_mode

    @debug_mode.setter
    def debug_mode(self, value):
        self._debug_mode = value
        self.debug_mode_changed.emit(value)

    @property
    def even_odd(self):
        return self._even_odd

    @even_odd.setter
    def even_odd(self, value):
        self._even_odd = value
        self.even_odd_changed.emit(value)

    @property
    def update_int(self):
        return self._update_int

    @update_int.setter
    def update_int(self, value):
        self._update_int = value
        self.update_int_changed.emit(value)

    @property
    def enable_reset(self):
        return self._enable_reset

    @enable_reset.setter
    def enable_reset(self, value):
        self._enable_reset = value
        self.enable_reset_changed.emit(value)

    @property
    def view_dateTime_start(self):
        return self._view_dateTime_start

    @view_dateTime_start.setter
    def view_dateTime_start(self, value):
        self._view_dateTime_start = value
        self.view_dateTime_start_changed.emit(value)

    @property
    def view_dateTime_stop(self):
        return self._view_dateTime_stop

    @view_dateTime_stop.setter
    def view_dateTime_stop(self, value):
        self._view_dateTime_stop = value
        self.view_dateTime_stop_changed.emit(value)

    @property
    def view_time_int(self):
        return self._view_time_int

    @view_time_int.setter
    def view_time_int(self, value):
        self._view_time_int = value
        self.view_time_int_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._amount = 0
        self._even_odd = ''
        self._enable_reset = False
        self._debug_mode = True
        self._view_dateTime_start = QDateTime.currentDateTimeUtc()
        self._view_dateTime_stop = QDateTime.currentDateTimeUtc()
        self._view_time_int = "1h"
        self._update_int = 5000
