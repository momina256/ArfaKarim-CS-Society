#!/bin/sh
# a script for mounting stuff (compatible on both linux and mac os) 
# run as root
system=$(uname)
linux() {
	sudo fdisk -l 
	printf "Choose the device you want to mount: \n"
	read drive 
	printf "Choose the mount point (e.g /mnt):"
	read mount_point 
	if [[ "$mount_point" == "" ]]; then
   		mount_point="/mnt"
   		printf "Mounted at /mnt."
	else
		sudo mount $drive $mount_point
		printf "Mounted at $mount_point.\n"
	fi
}
macos() {
	sudo diskutil list
	printf "Choose the device you want to mount: \n"
	read drive 
	printf "Choose an optional mount point (e.g /tmp/mnt):"
	read mount_point 
	if [[ "$mount_point" == "" ]]; then
   		sudo diskutil mount $drive
	else
		mkdir $mount_point
		partition_type=$(diskutil info /dev/disk0s1 | grep  -i "bundle" | awk '{ print $3 }')
		sudo mount -t $partition_type $drive $mount_point
		printf "Successfully mounted!\n"
	fi
}
if [[ "$system" == "Linux" ]]; then
	linux
elif [[ "$system" == "Darwin" ]]; then
	macos
else
	printf "Unknown system."
fi
