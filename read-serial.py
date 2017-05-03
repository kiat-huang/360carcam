import serial
ser = serial.Serial('/dev/ttyUSB0',115200)
while 1:
    print(ser.readline())

