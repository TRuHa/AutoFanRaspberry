#!/usr/bin/python
#Version AutoFan1.0

distro = open("/etc/issue","r")
if distro.read() < "OpenELEC":
	import sys
	sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib')
distro.close()

import RPi.GPIO as GPIO
import commands
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 1000)
fan = 50


def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000

pwm.start(50)
os.system('clear')

try:
	while True:
		os.system('clear')
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
		print "  Con el puede comprobar el correcto funcionamiento,         "
		print "  monitoreo de temperaturas y rendimiento del ventilador.    "
		print ""
		print "-------------------------------------------------------------"
		print "      Temperatura CPU: ", temp, " |  Ventilador al", fan,"%"
		print "-------------------------------------------------------------"
		print ""
		print "Presione [CTRL+C] para abortar."
		time.sleep(1)
		if temp <= 38:
			pwm.ChangeDutyCycle(50)
			fan = 50
		elif temp >= 38 and temp <= 40:    
			pwm.ChangeDutyCycle(40)
			fan = 60
		elif temp >= 41 and temp <= 43:  
			pwm.ChangeDutyCycle(30)
			fan = 70
		elif temp >= 44 and temp <= 46:
			pwm.ChangeDutyCycle(20)
			fan = 80
		elif temp >= 47 and temp <= 49:
			pwm.ChangeDutyCycle(10)
			fan = 90
		elif temp >= 49:
			pwm.ChangeDutyCycle(0)
			fan = 100

except KeyboardInterrupt:
	print ""
	pwm.stop()
	GPIO.cleanup()
