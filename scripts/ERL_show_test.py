#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

gateway1 = {
    "host": "192.168.69.1",
    "username": "gmann",
    "password": getpass(),
    "device_type": "vyatta_vyos",
}

net_connect = Netmiko(**gateway1)
command = "show interfaces"

print()
print(net_connect.find_prompt())
output = net_connect.send_command(command)
net_connect.disconnect()
print(output)
print()