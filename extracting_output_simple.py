import re

a = 'Last login: Wed Feb 16 23:14:42 2022 from 192.168.1.110\r\r\nenable\r\nterminal length 0\r\nenable\nterminal length 0\nArista3>enable\r\nArista3#terminal length 0\r\nPagination disabled.\r\nArista3#\r\nconfigure terminal\r\nArista3#configure terminal\r\nArista3(config)#show interfaces loopback 0\r\nLoopback0 is up, line protocol is up (connected)\r\n  Hardware is Loopback\r\n  Internet address is 3.3.3.3/24\r\n  Broadcast address is 255.255.255.255\r\n  IP MTU 65535 bytes\r\n  Up 1 hour, 6 minutes, 51 seconds\r\nArista3(config)#\r\nArista3(config)#show ntp status\r\nNTP is disabled.\r\nArista3(config)#'

ip = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", a.split('\r\n')[12])
