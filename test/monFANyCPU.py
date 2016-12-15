#!/usr/bin/python

import RPi.GPIO as GPIO
import commands
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 1000)

def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000

pwm.start(50)
os.system('clear')

while True:
	temp = round(get_cpu_temp())
	time.sleep(1)
	os.system('clear')
	print "Temperatura CPU: ", temp
	if temp <= 38:
		pwm.ChangeDutyCycle(50)
		print "Ventilador al 50%"
	elif temp >= 38 and temp <= 40:    
		pwm.ChangeDutyCycle(40)
		print "Ventilador al 60%"
	elif temp >= 41 and temp <= 43:  
		pwm.ChangeDutyCycle(30)
		print "Ventilador al 70%"
	elif temp >= 44 and temp <= 46:
		pwm.ChangeDutyCycle(20)
		print "Ventilador al 80%"
	elif temp >= 47 and temp <= 49:
		pwm.ChangeDutyCycle(10)
		print "Ventilador al 90%"
	elif temp >= 49:
		pwm.ChangeDutyCycle(0)
		print "Ventilador al 100%"