#!/bin/bash

#colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

clear
printf "${YELLOW}******************************************************${NC}\n";
printf "${YELLOW}**** start *******************************************${NC}\n";
printf "${GREEN}**** sudo iptables -t filter -vnL *********************${NC}\n";
sudo iptables -t filter -vnL
printf "${GREEN}**** sudo iptables -t nat -vnL ************************${NC}\n";
sudo iptables -t nat -vnL
printf "${GREEN}**** hostname *****************************************${NC}\n";
hostname
hostname -I
printf "${GREEN}**** the interfaces' names *****************************${NC}\n";
ls /sys/class/net/
printf "${GREEN}**** ip route *****************************************${NC}\n";
ip route
printf "${GREEN}**** ip_forward ***************************************${NC}\n";
cat /proc/sys/net/ipv4/ip_forward
printf "${GREEN}**** rules ********************************************${NC}\n";
sudo iptables-save | cat
printf "${YELLOW}**** end *********************************************${NC}\n";
printf "${YELLOW}******************************************************${NC}\n";