#!/bin/bash
#Version AutoFan1.0

if ! [ $(id -u) = 0 ]; then
	echo "Debe iniciar como root, abortando."
	exit 1
fi

if [ -f /etc/init.d/autofan-init ]; then
	if grep "AutoFan1.0" /etc/init.d/autofan-init; then
		echo "Actualente instalado, abortado."
		exit 1
	fi
fi

clear
echo ""
echo "----------------------------------------------------------------"
echo ""
echo "        _____  _   _  _____  _____  ___  _____  _   _           "
echo "       |  _  || | | ||_   _||  _  || __||  _  || \ | |          "
echo "       |  _  || |_| |  | |  | |_| || _| |  _  ||  \| |          "
echo "       |_| |_||_____|  |_|  |_____||_|  |_| |_||_|\__|          "
echo ""
echo "                     === AutoFan 1.0 ===                        "
echo ""
echo "----------------------------------------------------------------"
echo ""
echo "   Este instalador hara que el script inicie en el arranque     "
echo "   con el fin de refrigerar nuestra Raspberry pi dependiendo    "
echo "   de la temperatura de la CPU.                                 "
echo ""
echo "Presione ENTER para continuar, [CTRL+C] para abortar."
read INPUT
echo ""

if [ -d ~/autofan ]; then
 	echo "[+] Actualizando archivos..."
	echo ""
	else
	mkdir ~/autofan
	echo "[+] Copiando archivos nuevos..."
	echo ""
fi

cp -f autofan.py ~/autofan/
cp -f uninstall.sh ~/autofan/
cp -f monitorCPU.py ~/autofan/

echo "[+] Instalando cargador inicio..."
echo ""
chmod 755 autofan-init
cp -f autofan-init /etc/init.d
cd /etc/init.d
update-rc.d autofan-init defaults

echo ""
echo "---------------------------------------------------------------"
echo " AutoFan instalado correctamente!"
echo "---------------------------------------------------------------"
echo ""
echo "[+] Debe reiniciar el sistema ahora."
echo ""
echo "Presione ENTER para continuar, [CTRL+C] para abortar."
echo ""
read INPUT
reboot

