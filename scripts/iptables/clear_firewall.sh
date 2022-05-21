#!/bin/bash

## -F, --flush [chain]
## Clear all rules
sudo iptables -F
sudo iptables -F -t nat
sudo iptables -F -t mangle

##  -X, --delete-chain [chain]
sudo iptables -X
sudo iptables -X -t nat
sudo iptables -X -t mangle

sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P INPUT ACCEPT
