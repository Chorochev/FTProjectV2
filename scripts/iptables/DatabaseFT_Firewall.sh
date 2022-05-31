#!/bin/bash

## Firewall for DarabaseFT
## Clear all rules
sudo iptables -F
## Clear chains
sudo iptables -X

# set defaults rules
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT DROP

# Needs for http
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

# tcp port 25  mail-service
# tcp port 80, 443 http/https
# tcp port 3000  grafana-server
# tcp port 5432 postgres
# tcp port 9090 prometheus
# tcp port 9093, 9094 prometheus-aler
# tcp port 9100 prometheus-node
sudo iptables -A INPUT -p tcp -m multiport --dports 25,80,443,3000,5432,9090,9093,9094,9100 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m multiport --sports 25,80,443,3000,5432,9090,9093,9094,9100 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT

# for management - ssh [tcp port 4422]
sudo iptables -A INPUT -p tcp --dport 4422 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp --sport 4422 --match state --state ESTABLISHED -j ACCEPT

# for time-server [udp port 123]
sudo iptables -A INPUT -p udp --dport 123 -m state --state ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p udp --sport 123 -m state --state NEW,ESTABLISHED -j ACCEPT

# for dhclient [udp port 68]
sudo iptables -A INPUT -p udp --dport 68 -j ACCEPT
sudo iptables -A OUTPUT -p udp --sport 68 -j ACCEPT

# for logs
sudo iptables -N LOGGING
sudo iptables -A INPUT -j LOGGING
sudo iptables -A OUTPUT -j LOGGING
sudo iptables -A LOGGING -m limit --limit 5/min -j LOG --log-prefix "IPTables-Dropped: " 
sudo iptables -A LOGGING -j DROP
