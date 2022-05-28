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
printf "${YELLOW}Delete file /var/www/python_app/wsgi.py.${NC}\n" 
rm /var/www/python_app/wsgi.py
ProgressBar 4 100
printf "${YELLOW}Delete file /var/www/python_app/bs_update_bookshelf.py.${NC}\n" 
rm /var/www/python_app/bs_update_bookshelf.py
ProgressBar 8 100
printf "${YELLOW}Delete file /var/www/python_app/bs_loger.py.${NC}\n" 
rm /var/www/python_app/bs_loger.py
ProgressBar 12 100
printf "${YELLOW}Delete file /var/www/python_app/bs_helper.py.${NC}\n" 
rm /var/www/python_app/bs_helper.py
ProgressBar 16 100
printf "${YELLOW}Delete file /var/www/python_app/bs_controler.py.${NC}\n" 
rm /var/www/python_app/bs_controler.py
ProgressBar 20 100
printf "${YELLOW}Delete file /var/www/python_app/uwsgi.sock.${NC}\n" 
rm /var/www/python_app/uwsgi.sock
ProgressBar 24 100
# html
printf "${YELLOW}Delete files /var/www/python_app/static/*.${NC}\n" 
rm -R /var/www/python_app/static/*
ProgressBar 28 100
printf "${YELLOW}Delete files /var/www/python_app/templates/*.${NC}\n" 
rm -R /var/www/python_app/templates/*
ProgressBar 32 100

# python
printf "${GREEN}Copying file /var/www/python_app/wsgi.py.${NC}\n"       
cp /home/sshalex/python/wsgi.py /var/www/python_app/wsgi.py
ProgressBar 36 100
printf "${GREEN}Copying file /var/www/python_app/bs_update_bookshelf.py.${NC}\n"       
cp /home/sshalex/python/bs_update_bookshelf.py /var/www/python_app/bs_update_bookshelf.py
ProgressBar 40 100
printf "${GREEN}Copying file /var/www/python_app/bs_loger.py.${NC}\n"       
cp /home/sshalex/python/bs_loger.py /var/www/python_app/bs_loger.py
ProgressBar 44 100
printf "${GREEN}Copying file /var/www/python_app/bs_helper.py.${NC}\n" 
cp /home/sshalex/python/bs_helper.py /var/www/python_app/bs_helper.py
ProgressBar 48 100
printf "${GREEN}Copying file /var/www/python_app/bs_controler.py.${NC}\n" 
cp /home/sshalex/python/bs_controler.py /var/www/python_app/bs_controler.py
ProgressBar 52 100
printf "${GREEN}Copying file /var/www/python_app/bs_create_html.py.${NC}\n" 
cp /home/sshalex/python/bs_create_html.py /var/www/python_app/bs_create_html.py 
ProgressBar 56 100
# html
printf "${GREEN}Copying file /var/www/python_app/static/index.html.${NC}\n" 
cp /home/sshalex/html/index.html /var/www/python_app/static/index.html
ProgressBar 60 100
printf "${GREEN}Copying file /var/www/python_app/templates/template_dictionary.html.${NC}\n" 
cp /home/sshalex/html/templates/template_dictionary.html /var/www/python_app/templates/template_dictionary.html
ProgressBar 64 100
printf "${GREEN}Copying file /var/www/python_app/templates/template_article.html.${NC}\n"
cp /home/sshalex/html/templates/template_article.html /var/www/python_app/templates/template_article.html
ProgressBar 68 100
printf "${GREEN}create static html.${NC}\n"
python3 /var/www/python_app/bs_create_html.py
ProgressBar 72 100
printf "${GREEN}restart uwsgi.${NC}\n"  
systemctl restart uwsgi
ProgressBar 95 100
printf "${GREEN}restart nginx.${NC}\n"
sudo systemctl restart nginx
ProgressBar 100 100

printf "${GREEN}end.${NC}\n"  