#!/usr/bin/python

import sys

def get_obj():
	objfile = open("/storage/autofan/obj")
	obj_temp = objfile.read()
	objfile.close()
	return float(obj_temp)

def set_obj():
        objfile = open("/storage/autofan/obj", "w")
        objfile.write(newobj)
        objfile.close()

obj = round(get_obj())

try:

        print ""
        print "Va a procer a actualizar la temperatura maxima."
        print ""
        print "Pulse control+C para cancelar."
        print ""
        print "Objetivo actual: " + str(obj)

        newobj = raw_input("Nuevo objetivo : ")
	if not newobj.isdigit():
		print ""
		print "Introduzca solo valor numerico"
		sys.exit(0)

	set_obj()
        obj = round(get_obj())
        print ""
        print "Temperatura actualizada a " + str(obj) + " grados."
	print ""
	print "Muchas gracias."

except ValueError:
	print ""
	print "Valor intoducido erroneo."

except KeyboardInterrupt:
	print ""
	print "ancelado por el Usuario"

finally:
	print ""
	print "Hasta Pronto"

