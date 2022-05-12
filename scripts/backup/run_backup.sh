#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
# shellcheck disable=SC2034
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# -------------- local variables --------------------------------------------- #
declare storepath="/var/backups/final-task-backups"
declare name_apt="apt"
declare name_dhcp="dhcp"
declare name_network="network"
declare name_ssh="ssh"
declare name_iptables="iptables"

# ---------------------------------------------------------------------------- #
# -------------- inner functions --------------------------------------------- #
function check_backup_catalogs() {
    # checking the general directory
    if [ ! -d "$storepath" ]; then         
        printf "${YELLOW}Creating path '$storepath' for backups .${NC}\n"       
        mkdir $storepath
        set_permissions "$storepath"
    fi
    # checking the subdirectory structure
    if [ ! -d "$storepath/$1" ]; then
        printf "${YELLOW}Creating path '$storepath/$1'.${NC}\n"       
        mkdir "$storepath/$1"
        set_permissions "$storepath/$1"
    fi
}

function set_permissions() {   
    printf "${YELLOW}Setting the permission for '$1'.${NC}\n"
    # The Root can everything
    chmod u+rwx $1 
    # Other users can nothing
    chmod o-rwx $1  
}

function execute_scrip_for_backup() {
    printf "${YELLOW}Setting the permission for run.${NC}\n"
    chmod +x $1
    printf "${YELLOW}Launch 'run_backup_apt.sh'.${NC}\n"
    ./$1
    printf "${YELLOW}Remove 'run_backup_apt.sh'.${NC}\n"
    rm $1
} 
# -------------- inner functions --------------------------------------------- #
# ---------------------------------------------------------------------------- #

# -------------- apt --------------------------------------------------------- #
function backup_for_apt() {
    check_backup_catalogs $name_apt
    printf "${GREEN}Creating backup for apt.${NC}\n" 
    script_name='run_backup_apt.sh'
    files_for_backup='/etc/apt/sources.list'  
    ./backup.sh --create $script_name --files $files_for_backup --destination $storepath'/'$name_apt --name 'backup_'$name_apt --script 'yes'
    execute_scrip_for_backup $script_name
}

# -------------- dhcp -------------------------------------------------------- #
function backup_for_dhcp() {
    check_backup_catalogs $name_dhcp
    printf "${GREEN}Creating backup for dhcp.${NC}\n" 
    script_name='run_backup_dhcp.sh'
    files_for_backup='/etc/default/isc-dhcp-server,/etc/dhcp/dhcpd.conf'  
    ./backup.sh --create $script_name --files $files_for_backup --destination $storepath'/'$name_dhcp --name 'backup_'$name_dhcp --script 'yes'
    execute_scrip_for_backup $script_name
}

# -------------- network ----------------------------------------------------- #
function backup_for_network() {
  check_backup_catalogs $name_network
  printf "${GREEN}Creating backup for network.${NC}\n" 
  script_name='run_backup_network.sh'
  files_for_backup='/etc/hosts,/etc/network/interfaces,/etc/resolv.conf,/etc/resolvconf/resolv.conf.d/base'
  ./backup.sh --create $script_name --files $files_for_backup --destination $storepath'/'$name_network --name 'backup_'$name_network --script 'yes'
  execute_scrip_for_backup $script_name
}

# -------------- ssh --------------------------------------------------------- #
function backup_for_ssh() {
    check_backup_catalogs $name_ssh
    printf "${GREEN}Creating backup for ssh.${NC}\n" 
    script_name='run_backup_ssh.sh'
    files_for_backup='/etc/ssh/sshd_config'
    ./backup.sh --create $script_name --files $files_for_backup --destination $storepath'/'$name_ssh --name 'backup_'$name_ssh --script 'yes'
    execute_scrip_for_backup $script_name    
}

# -------------- iptables ---------------------------------------------------- #
function backup_for_iptables() {
    check_backup_catalogs $name_iptables
    printf "${GREEN}Creating backup for ssh.${NC}\n" 
    script_name='run_backup_iptables.sh'   
    files_for_backup='/etc/network/if-pre-up.d/firewall'    
    ./backup.sh --create $script_name --files $files_for_backup --destination $storepath'/'$name_iptables --name 'backup_'$name_iptables --script 'yes'
    execute_scrip_for_backup $script_name      
}

# -------------- all --------------------------------------------------------- #
function backup_all() {
    backup_for_apt
    backup_for_dhcp
    backup_for_network
    backup_for_ssh
    backup_for_iptables
}

# -------------- main -------------------------------------------------------- #
clear

PS3='Please enter your choice:'
options=("Backup for apt" 
         "Backup for dhcp" 
         "Backup for network"
         "Backup for ssh"
         "backup for iptables"
         "backup all"
         "backup all and quit"
         "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Backup for apt")
            backup_for_apt
            ;;
        "Backup for dhcp")
            backup_for_dhcp
            ;;
        "Backup for network")
            backup_for_network
            ;;
        "Backup for ssh")
            backup_for_ssh
            ;;
        "backup for iptables")
            backup_for_iptables
            ;;
        "backup all")
           backup_all
           ;;
        "backup all and quit")
           backup_all
           break
           ;;
        "Quit")
            break
            ;;
        *) printf "${RED}Invalid the choice!${NC}\n";;
    esac
done