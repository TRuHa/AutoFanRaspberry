#!/usr/bin/python

import commands
import time
import sys
import os

def get_cpu_temp():
	tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
	cpu_temp = tempFile.read()
	tempFile.close()
	return float(cpu_temp)/1000

os.system('clear')

try:
	while True:
		temp = round(get_cpu_temp())
		print ""
		print "-------------------------------------------------------------"
		print ""
		print "        _____  _   _  _____  _____  ___  _____  _   _        "
		print "       |  _  || | | ||_   _||  _  || __||  _  || \ | |       "
		print "       |  _  || |_| |  | |  | |_| || _| |  _  ||  \| |       "
		print "       |_| |_||_____|  |_|  |_____||_|  |_| |_||_|\__|       "
		print ""
		print "                     === AutoFan 1.0 ===                     "
		print ""
		print "-------------------------------------------------------------"
		print ""
		print "  Este script hace un test de AutoFan.                       "
		print ""
		print "  Con el puede realizar un monitoreo de la temperatura       "
		print "  y comprobar la eficacia del mismo.                         "
		print ""
		print "-------------------------------------------------------------"
		print "                  Temperatura CPU: ", temp
		print "-------------------------------------------------------------"
		print ""
		print "Presione [CTRL+C] para abortar."
		time.sleep(1)
		os.system('clear')

except KeyboardInterrupt:
	print ""
