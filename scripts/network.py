#!/usr/bin/env python
import netifaces as nic
nic.ifaddresses('enp3s0')
ip = nic.ifaddresses('enp3s0')[nic.AF_INET][0]['addr']
print(ip) 

