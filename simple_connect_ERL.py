#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

net_connect = Netmiko(
    "192.168.69.1",
    username="gmann",
    password=getpass(),
    device_type="vyatta_vyos",
)

print(net_connect.find_prompt())
net_connect.disconnect()