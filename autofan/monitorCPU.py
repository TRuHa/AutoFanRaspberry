#!/usr/bin/python

import commands
import time
import sys
import os

def get_cpu_temp():
	tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
	cpu_temp = tempFile.read()
	tempFile.close()
	return int(cpu_temp)

def get_obj():
        objfile = open("/storage/autofan/obj")
        obj_temp = objfile.read()
        objfile.close()
        return float(obj_temp)

def get_ciclo():
        ciclofile = open("/storage/autofan/ciclo")
        ciclo_temp = ciclofile.read()
        ciclofile.close()
        return int(ciclo_temp)

os.system('clear')

try:
	while True:
		temp = round(get_cpu_temp())/1000
		obj = round(get_obj())
		ciclo = round(get_ciclo())
		print ""
		print "-------------------------------------------------------------"
		print ""
		print "        _____  _   _  _____  _____  ___  _____  _   _"
		print "       |  _  || | | ||_   _||  _  || __||  _  || \ | |"
		print "       |  _  || |_| |  | |  | |_| || _| |  _  ||  \| |"
		print "       |_| |_||_____|  |_|  |_____||_|  |_| |_||_|\__|"
		print ""
		print "                     === AutoFan 1.0 ==="
		print ""
		print "-------------------------------------------------------------"
		print ""
		print "  Este programa hace un test de AutoFan."
		print ""
		print "  Con el puede realizar un monitoreo de la temperatura"
		print "  y comprobar la eficacia del mismo."
		print ""
		print "-------------------------------------------------------------"
		print "                  Temperatura CPU: ", str(temp)
		print "                  Temperatura OBJ: ", str(obj)
		print ""
		print "               Ciclo del ventilador = ", str(ciclo)
		print "-------------------------------------------------------------"
		print ""
		print "Presione [CTRL+C] para abortar."
		time.sleep(0.5)
		os.system('clear')

except KeyboardInterrupt:
	print ""
