#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' # No Color

clear
printf "${GREEN}log: /var/log/uwsgi/app/python_app.log${NC}\n"       
tail -n$1 /var/log/uwsgi/app/python_app.log
printf "${GREEN}log: /var/log/nginx/access.log${NC}\n" 
tail -n$1 /var/log/nginx/access.log
printf "${GREEN}log: /var/log/nginx/error.log${NC}\n" 
tail -n$1 /var/log/nginx/error.log
printf "${GREEN}log: /var/local/logs/bookshelf.log${NC}\n"  
tail -n$1 /var/local/logs/bookshelf.log
printf "${GREEN}log: /var/local/logs/bookshelf.helper.log${NC}\n" 
tail -n$1 /var/local/logs/bookshelf.helper.log
printf "${GREEN}log: /var/local/logs/bookshelf.controler.log${NC}\n" 
tail -n$1 /var/local/logs/bookshelf.controler.log
printf "${GREEN}log: /var/local/logs/bookshelf.update.log${NC}\n" 
tail -n$1 /var/local/logs/bookshelf.update.log

printf "${GREEN}end.${NC}\n"  