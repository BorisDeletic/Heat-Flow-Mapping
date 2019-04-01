import serial
import time
import csv
import datetime


def read_temps(raw):
	H_sensor_order = [6,5,0,3,8,2,9,7,1,4]
	V_sensor_order = [1,0,3,2]

	try:
		Htemps = sort_temps(raw, H_sensor_order, 'H:')
		Vtemps = sort_temps(raw, V_sensor_order, 'V:')
#		print('\n NEW LINE')
		print(Htemps)
#		print(Vtemps)
		return (Htemps, Vtemps)

	except:
		return (False, False)


def sort_temps(raw, sensor_order, key):
	temps = [0 for x in range(len(sensor_order))]

	split_values = raw.split(',')
	split_values.pop()

	if split_values[0][:2] == key:
		split_values[0] = split_values[0][3:]
		for i, temp in enumerate(split_values):
			senID = sensor_order[i]
			temps[senID] = float(temp)

		return temps

	else:
		return False


def log_data(temps, cable):
	if temps != False and 0 not in temps:
		t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(t)
		write_row = [t] + temps
		with open("/mnt/TempSensors/" + cable + "_data.csv", 'a') as f:
			cwriter = csv.writer(f)
			cwriter.writerow(write_row)



ser = serial.Serial('/dev/ttyACM0', 9600)
#while True:
for i in range(10):
	time.sleep(0.5)
	if(ser.in_waiting > 0):
		line = ser.readline()
		line_str = line.decode('utf-8')
#		print(line_str)
		Htemps, Vtemps = read_temps(line_str)

		log_data(Htemps, "H")
		log_data(Vtemps, "V")
#		print(temps)
#		try:
#			if 0 not in temps:
#				log_data(temps)
#		except:
#			pass
#line = "H: 21.56,21.87,21.12,21.62,22.62,21.50,22.00,21.37,21.12,21.31,"
#read_temps(line)
