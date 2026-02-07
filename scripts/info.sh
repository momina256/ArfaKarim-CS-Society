#!/bin/bash
platform=$(uname)
if [[ $platform == "Darwin" ]]; then
  # a common indication of iOS is that if /var/mobile exists; check for that directory
  if [[ -d "/var/mobile" ]]; then
    platform="iOS"
    figlet "iOS XNU/Darwin"
  fi 
    platform="MacOS"
    figlet "Mac OS XNU/Darwin"
    battery=$(pmset -g batt)
elif [[ $platform == "Linux" ]]; then
  # on android we should look for /storage/emulated/0
  if [[ -d "/storage/emulated/0" ]]; then
    platform="android"
    figlet "Android/Linux" 
  fi 
    platform="Linux"
    # I am sorry for Alpine Linux :( 
    figlet "GNU/Linux"
fi
date
uptime
duf || df -h
curl wttr.in


