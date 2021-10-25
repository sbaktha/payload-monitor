import serial
import csv

ser = serial.Serial('/dev/ttyACM0')
print(ser)
#while ser.in_waiting:
#   print('hey')
# file_name = "http://raw.githubusercontent.com/sbaktha/payload-monitor/main/data.csv"
file_name = "./testdata2.csv"
with open(file_name, 'w') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['Index','AccX', 'AccY', 'AccZ','MagX', 'MagY', 'MagZ', 'GyrX', 'GyrY', 'GyrZ','Alt','Temp'])
sero = ser.readline()
sero = ser.readline()
def Convert(string):
    li = list(string.split(","))
    return li
m=1
while True:
    ser_bytes = ser.readline()
    print(ser_bytes)
    k=Convert(ser_bytes.decode('utf-8'))
    print(k)

    k.insert(0,m)
    print(k)
    m=m+1
    with open(file_name,"a") as f:
        writer = csv.writer(f,delimiter=",")
    #    writer.writerow(m)
        print(k)
        writer.writerow(k)



