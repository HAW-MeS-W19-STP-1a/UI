from PyQt5.QtCore import QObject, pyqtSignal, QDateTime
import pandas as pd
import numpy as np
import serial


class Model(QObject):
    amount_changed = pyqtSignal(int)
    console_buffer_changed = pyqtSignal(str)
    com_mode_changed = pyqtSignal(bool)
    data_changed = pyqtSignal(pd.DataFrame)
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
    def console_buffer(self):
        return self._console_buffer

    @console_buffer.setter
    def console_buffer(self, value):
        self._console_buffer = value
        self.console_buffer_changed.emit(value)

    @property
    def com_mode(self):
        return self._com_mode

    @com_mode.setter
    def com_mode(self, value):
        self._com_mode = value
        self.com_mode_changed.emit(value)

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

    @property
    def ser(self):
        return self._ser

    @ser.setter
    def ser(self, value):
        self._ser = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.data_changed.emit(value)

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
        self._console_buffer = ""
        self._com_mode = False
        self._data = pd.DataFrame(columns=[
            "DateTime", "t_bme", "t_cpu", "t_qmc", "t_mpu", "w_dir", "w_spd",
            "pres", "hum", "zen", "azm", "lat", "lon", "alt", "v_bat", "i_bat",
            "v_solar", "i_solar", "v_5v"
        ])
        self._ser = None
        self.x = (np.arange(8)+1) * (3600 * 24 * 356)
        self.y1 = [1, 6, 2, 4, 3, 5, 6, 8]
        self.y2 = [10, 20, 30, 40, 50, 60, 70, 80]
        self.y3 = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
