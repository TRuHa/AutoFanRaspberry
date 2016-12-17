#!/usr/bin/python
#Version AutoFan1.0

import commands
import time
import os

os.system('clear')

def get_cpu_temp():
	tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
	cpu_temp = tempFile.read()
	tempFile.close()
	return float(cpu_temp)/1000

while True:
	print "Temperatura CPU ", round(get_cpu_temp())
	time.sleep(0.5)
	os.system('clear')
