#!/bin/bash

v=$(google-chrome --version)
v=(${v/// })
v=${v[-1]}
v=${v%.*}
echo $v
mkdir -p /tmp/CHROMEDRIVERINSTALLER/
OUTPATH="/tmp/CHROMEDRIVERINSTALLER"
wget  https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$v  -O  "$OUTPATH/LATEST_RELEASE_$v"

#/chromedriver_linux64.zip

driver_version=$(cat  "$OUTPATH/LATEST_RELEASE_$v")

echo $driver_version

# download the driver

wget  "https://chromedriver.storage.googleapis.com/$driver_version/chromedriver_linux64.zip"  -O "$OUTPATH/chromedriver_linux64.zip"

# install driver

sudo unzip "$OUTPATH/chromedriver_linux64.zip" -d /usr/local/bin/ 


echo 'SUCCESS! Installed chromedriver  version $driver_version, compatible to your google-chrome.'
