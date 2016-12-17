#!/bin/bash
#Version AutoFan1.0

if ! [ $(id -u) = 0 ]; then
	echo "Debe iniciar como root, abortando."
	exit 1
fi

if ! [ -f /etc/init.d/autofan-init ]; then
	echo "Autofan no instalado."
	exit 1
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
echo "                     === ADVERTENCIA ===                        "
echo ""
echo "   Va a proceder a desinstalar Autofan.                         "
echo ""
echo "   Dejara de funcionar el ventilador para refrigerar su         "
echo "   Raspberry pi en caso de una alta temperatura.                "
echo ""
echo "Presione ENTER para continuar, [CTRL+C] para abortar."
read INPUT
echo ""

echo "[+] Desinstalando cargador de inicio..."
cd /etc/init.d
update-rc.d autofan-init remove
rm autofan-init

echo ""
echo "[+] Borrando archivos..."
rm -R ~/autofan

echo ""
echo "---------------------------------------------------------------"
echo " AutoFan desinstalado correctamente!"
echo "---------------------------------------------------------------"
echo ""
echo "[+] Debe reiniciar el sistema ahora."
echo ""
echo "Presione ENTER para continuar, [CTRL+C] para abortar."
echo ""
read INPUT
reboot

