#!/bin/bash

python3 /home/pi/Desktop/main.py

sudo service tor restart
sudo service php7.4-fpm restart
sudo service nginx restart
