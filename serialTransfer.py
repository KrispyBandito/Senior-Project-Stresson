import serial
import csv

arduino = '/dev/ttyACM0"
baud = 9600
fileName = "stressData.csv"
#date = input("enter todays date")

if __name__ == '__main__':
    ser = serial.Serial(arduino, baud, timeout = 3)
    ser.flush()
while True:
    if ser.in_waiting > 0:
        data = str(ser.readline().decode('utf-8').rstrip())
        print(data)
        with open("stressData.csv", "a") as f:
            writer = csv.writer(f, quoting = csv.QUOTE_MINIMAL)
            writer.writerow(data)
        ser.flush()
        break