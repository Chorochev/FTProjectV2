#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "${GREEN}Coping file wsgi.py.${NC}\n"       
cp /home/sshalex/python/wsgi.py /var/www/python_app/wsgi.py
printf "${GREEN}Coping file bs_controler.py.${NC}\n" 
cp /home/sshalex/python/bs_controler.py /var/www/python_app/bs_controler.py
printf "${GREEN}Coping file bs_helper.py.${NC}\n" 
cp /home/sshalex/python/bs_helper.py /var/www/python_app/bs_helper.py

printf "${GREEN}restart uwsgi.${NC}\n"  
systemctl restart uwsgi

printf "${GREEN}end.${NC}\n"  