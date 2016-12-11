import commands
import time
import os

os.system('clear')

i = 1
while i <= 10:
	def get_cpu_temp():
		tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
		cpu_temp = tempFile.read()
		tempFile.close()
		return float(cpu_temp)/1000
		#Mostrar temperatura en grados Fahrenheit
		#return float(1.8*cpu_temp)+32

	def main():
		print "Temperatura CPU: ", round(get_cpu_temp())
		time.sleep(0.5)
		os.system('clear')

	if __name__ == '__main__':
		main()
