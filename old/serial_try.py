import serial

ser = serial.Serial("COM4")
print(ser.name)         # check which port was really used
ser.write(b'h\n')     # write a string
line = ser.readline()
print(line)
