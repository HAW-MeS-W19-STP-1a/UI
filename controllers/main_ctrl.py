from PyQt5.QtCore import QObject, pyqtSlot, QDateTime, QTimer
from random import random
import serial
import pandas as pd
import time


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
        self._model.console_buffer = str(value) + self._model.console_buffer

    def set_com_mode(self, value):
        if value:
            try:
                self._model.ser = serial.Serial("COM4")
                time.sleep(0.1)
                if self._model.debug_mode:
                    print("Setting com_mode to: " + str(value))
                    self.add_to_console_buffer(QDateTime.currentDateTime().toString("[hh:mm:ss]") + " [DEBUG] " + "Connection opened.\r\n")
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
                self.add_to_console_buffer(QDateTime.currentDateTime().toString("[hh:mm:ss]") + " [DEBUG] " + "Connection closed.\r\n")
    def set_debug_mode(self, value):
        print("Setting Debug Mode to " + str(value))
        self._model.debug_mode = value
        self.update_view_dateTime()

    def set_simulate_mode(self, value):
        if self._model.debug_mode:
            print("Setting Simulate Mode to" + str(value))
        self._model.simulate_mode = value

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

    def set_data1_idx(self, value):
        print("Index is " + str(value))
        value = self._model.data.columns[value]
        if self._model.debug_mode:
            print("Setting data1_idx to " + str(value))
        self._model.data1_idx = value

    def set_data2_idx(self, value):
        print("Index is " + str(value))
        value = self._model.data.columns[value]
        if self._model.debug_mode:
            print("Setting data2_idx to " + str(value))
        self._model.data2_idx = value

    def send_command(self, value):
        if self._model.debug_mode:
            print("Sending command: " + str(value))
        self.add_to_console_buffer(QDateTime.currentDateTime().toString("[hh:mm:ss]") + " -> " + str(value) + "\r\n")
        if self._model.com_mode:
            # TODO Implement sending of commands
            self.send_command_to_station(value + "\r\n")

    def send_command_to_station(self, command):
        if self._model.debug_mode:
            print("Sending line to station: " + command)
        if self._model.ser:
            self._model.ser.write(command.encode("UTF-8"))
            line = ""
            while "OK" not in line and "ERROR" not in line:
                line = self._model.ser.readline().decode("UTF-8")
                if self._model.debug_mode:
                    print("Received line from station: " + line)
                self.add_to_console_buffer(QDateTime.currentDateTime().toString("[hh:mm:ss]") + " <- " + line)
                self.evaluate_rec_command(line)

    def evaluate_rec_command(self, line):
        if "+CGUI" in line:
            line = line.replace("+CGUI: ", "")
            line = line.replace("\r\n", "")
            items = line.split(",")
            dateTime = QDateTime.fromString(
                "20" + items[0] + items[1] + items[2] + items[3] + items[4] +
                items[5], "yyyyMMddhhmmss")
            newData = {
                "DateTime": dateTime.toString("dd.MM.yyyy hh:mm:ss"),
                "DateTimeInSec": dateTime.toSecsSinceEpoch(),
                "t_bme": int(items[6])/100,
                "t_cpu": int(items[7])/100,
                "t_qmc": int(items[8])/100,
                "t_mpu": int(items[9])/100,
                "w_dir": int(items[10])/10,
                "w_spd": int(items[11]),
                "pres": int(items[12])/100,
                "hum": int(items[13])/1024,
                "zen": int(items[14])/10,
                "azm": int(items[15])/10,
                "lat": int(items[16])/10000,
                "lon": int(items[17])/10000,
                "alt": int(items[18])/10,
                "v_bat": int(items[19])/100,
                "i_bat": int(items[20])/100,
                "v_solar": int(items[21])/100,
                "i_solar": int(items[22])/100,
                "v_sys": int(items[23])/100
            }
            if (newData["DateTimeInSec"] not in self._model.data["DateTimeInSec"].values) and (newData["DateTimeInSec"] > 60*60*24):
                newData = pd.DataFrame([newData])
                self._model.data = self._model.data.append(newData,
                                                           ignore_index=True)

    def simulate_new_data(self):
        if self._model.debug_mode:
            print("Simulating new Data.")
        dateTime = QDateTime.currentDateTimeUtc()
        newData = {
            "DateTime": dateTime.toString("dd.MM.yyyy hh:mm:ss"),
            "DateTimeInSec": dateTime.toSecsSinceEpoch(),
            "t_bme": random(),
            "t_cpu": random(),
            "t_qmc": random(),
            "t_mpu": random(),
            "w_dir": random(),
            "w_spd": random(),
            "pres": random(),
            "hum": random(),
            "zen": random(),
            "azm": random(),
            "lat": random(),
            "lon": random(),
            "alt": random(),
            "v_bat": random(),
            "i_bat": random(),
            "v_solar": random(),
            "i_solar": random(),
            "v_sys": random()
        }
        newData = pd.DataFrame([newData])
        self._model.data = self._model.data.append(newData,
                                                   ignore_index=True)

    def set_station_location(self, lat=53.556354, lon=10.022650):
        lat = int(lat*10000)
        lon = int(lon*10000)
        self.send_command("AT+CGNSPOS=%d,%d,%d" % (lat, lon, 0))

    def set_station_time(self, time=QDateTime.currentDateTimeUtc()):
        time = time.toString("yy,MM,dd,hh,mm,ss")
        self.send_command("AT+CTIME=" + time)

    def set_station_meas_int(self, meas_int):
        self.send_command("AT+CINTV=%d" % meas_int)

    def exec_station_wkup(self):
        self.send_command("AT+CWKUP")

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
        if self._model.simulate_mode:
            self.simulate_new_data()
        else:
            self.set_com_mode(True)
            self.send_command("AT+CGUI?")
            self.set_com_mode(False)

        self.update_view_dateTime()
        if self._model.update_int != -1:
            self._update_timer.start(self._model.update_int)
