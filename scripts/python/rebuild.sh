#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

function ProgressBar {
# Process data
    let _progress=(${1}*100/${2}*100)/100
    let _done=(${_progress}*4)/10
    let _left=40-$_done
# Build progressbar string lengths
    _fill=$(printf "%${_done}s")
    _empty=$(printf "%${_left}s")

# 1.2 Build progressbar strings and print the ProgressBar line
# 1.2.1 Output example:                           
# 1.2.1.1 Progress : [########################################] 100%
printf "\rProgress : [${_fill// /#}${_empty// /-}] ${_progress}%%   "
}

clear
ProgressBar 0 100
printf "${YELLOW}Delete file wsgi.py.${NC}\n" 
rm /var/www/python_app/wsgi.py
ProgressBar 5 100
printf "${YELLOW}Delete file bs_update_bookshelf.py.${NC}\n" 
rm /var/www/python_app/bs_update_bookshelf.py
ProgressBar 10 100
printf "${YELLOW}Delete file bs_loger.py.${NC}\n" 
rm /var/www/python_app/bs_loger.py
ProgressBar 15 100
printf "${YELLOW}Delete file bs_helper.py.${NC}\n" 
rm /var/www/python_app/bs_helper.py
ProgressBar 20 100
printf "${YELLOW}Delete file bs_controler.py.${NC}\n" 
rm /var/www/python_app/bs_controler.py
ProgressBar 25 100
printf "${YELLOW}Delete file uwsgi.sock.${NC}\n" 
rm /var/www/python_app/uwsgi.sock
ProgressBar 30 100

printf "${GREEN}Coping file wsgi.py.${NC}\n"       
cp /home/sshalex/python/wsgi.py /var/www/python_app/wsgi.py
ProgressBar 35 100
printf "${GREEN}Coping file bs_update_bookshelf.py.${NC}\n"       
cp /home/sshalex/python/bs_update_bookshelf.py /var/www/python_app/bs_update_bookshelf.py
ProgressBar 40 100
printf "${GREEN}Coping file bs_loger.py.${NC}\n"       
cp /home/sshalex/python/bs_loger.py /var/www/python_app/bs_loger.py
ProgressBar 45 100
printf "${GREEN}Coping file bs_helper.py.${NC}\n" 
cp /home/sshalex/python/bs_helper.py /var/www/python_app/bs_helper.py
ProgressBar 50 100
printf "${GREEN}Coping file bs_controler.py.${NC}\n" 
cp /home/sshalex/python/bs_controler.py /var/www/python_app/bs_controler.py
ProgressBar 55 100

printf "${GREEN}restart uwsgi.${NC}\n"  
systemctl restart uwsgi
ProgressBar 90 100

printf "${GREEN}restart nginx.${NC}\n"
sudo systemctl restart nginx
ProgressBar 100 100

printf "${GREEN}end.${NC}\n"  