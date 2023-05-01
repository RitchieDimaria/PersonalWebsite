#!/bin/sh

#Ensure you are in root shell before initiating script.

sudo apt-get update
sudo apt-get install nginx
sudo systemctl start nginx
sudo systemctl status nginx
exit