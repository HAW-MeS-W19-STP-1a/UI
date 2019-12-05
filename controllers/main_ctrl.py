from PyQt5.QtCore import QObject, pyqtSlot, QDateTime, QTimer
import serial
import pandas as pd

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
            value)

    def set_com_mode(self, value):
        if value:
            try:
                self._model.ser = serial.Serial("COM4")
                if self._model.debug_mode:
                    print("Setting com_mode to: " + str(value))
                self._model.com_mode = value
            except Exception as e:
                if self._model.debug_mode:
                    print(e)
        else:
            if self._model.ser:
                self._model.ser.close()
                self._model.ser = None
            self._model.com_mode = value
            if self._model.debug_mode:
                print("Setting com_mode to: " + str(value))

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
        if self._model.debug_mode:
            print("Sending command: " + str(value))
        self.add_to_console_buffer("-> " + str(value) + "\r\n")
        if self._model.com_mode:
            # TODO Implement sending of commands
            self.send_command_to_station(value+"\r\n")

    def send_command_to_station(self, command):
        if self._model.debug_mode:
            print("Sending line to station: " + command)
        if self._model.ser:
            self._model.ser.write(command.encode("UTF-8"))
            line = ""
            while line != "OK\r\n" and line != "ERROR\r\n":
                line = self._model.ser.readline().decode("UTF-8")
                if self._model.debug_mode:
                    print("Received line from station: " + line)
                self.add_to_console_buffer("<- " + line)
                self.evaluate_rec_command(line)

    def evaluate_rec_command(self, line):
        if "+CGUI" in line:
            line = line.replace("+CGUI: ", "")
            line = line.replace("\r\n", "")
            items = line.split(",")
            dateTime = QDateTime.fromString(
                "20"+items[0]+items[1]+items[2]+items[3]+items[4]+items[5],
                "yyyyMMddhhmmss")
            newData = {"DateTime": dateTime,
                       "t_bme": int(items[6]),
                       "t_cpu": items[7],
                       "t_qmc": items[8],
                       "t_mpu": items[9],
                       "w_dir": items[10],
                       "w_spd": items[11],
                       "pres": items[12],
                       "hum": items[13],
                       "zen": items[14],
                       "azm": items[15],
                       "lat": items[16],
                       "lon": items[17],
                       "alt": items[18],
                       "v_bat": items[19],
                       "i_bat": items[20],
                       "v_solar": items[21],
                       "i_solar": items[22],
                       "v_5v": items[23]}
            newData = pd.DataFrame([newData])
            self._model.data = self._model.data.append(newData,
                                                       ignore_index=True)
            if self._model.debug_mode:
                print("Data: " + str(self._model.data))

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
        self.set_com_mode(True)
        self.send_command("AT+CGUI?")
        self.set_com_mode(False)
        self.update_view_dateTime()
        if self._model.update_int != -1:
            self._update_timer.start(self._model.update_int)
