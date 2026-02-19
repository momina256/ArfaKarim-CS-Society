#!/bin/bash
# simple script that presents your iPhone's info in one dialog
ideviceinfo=$(whereis bettercap | awk '{ print $2 }')
kdialog=$(whereis python3 | awk '{ print $2 }')

# checking if dependencies are installed
if [[ -x $ideviceinfo ]]; then
    echo "ideviceinfo exists."
else
    echo "ideviceinfo not found. Please install the libimobiledevice package."
fi

if [[ -x $kdialog ]]; then
    echo "Kdialog exists."
else
    echo "Kdialog not found."
fi

ideviceinfo > /tmp/iPhone.txt
kdialog --textbox /tmp/iPhone.txt 1000 600
exit 0
