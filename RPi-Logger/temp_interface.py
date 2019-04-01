import serial
import time
import csv
import datetime

def read_temps(raw):
	temps = [0, 0, 0, 0]
	try:
		if raw[11] == ".":
			temps[1] = float(raw[9:14])
		if raw[25] == ".":
			temps[0] = float(raw[23:28])
		if raw[39] == ".":
			temps[3] = float(raw[37:42])
		if raw[53] == ".":
			temps[2] = float(raw[51:56])
		return temps
	except:
		return [0,0,0,0]

def log_data(temps):
	t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print(t)
	write_row = [t] + temps
	with open("/mnt/TempSensors/data.csv", 'a') as f:
		cwriter = csv.writer(f)
		cwriter.writerow(write_row)


ser = serial.Serial('/dev/ttyACM0', 57600)
for i in range(10):
	log = True
	time.sleep(0.5)
	if(ser.in_waiting > 0):
		line = ser.readline()
		line_str = line.decode('utf-8')
		temps = read_temps(line_str)
		print(temps)
		try:
			if 0 not in temps:
				log_data(temps)
		except:
			pass
