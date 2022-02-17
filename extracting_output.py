"""Extracting ip address out of output"""
import re

a = 'Last login: Wed Feb 16 23:14:42 2022 from 192.168.1.110\r\r\nenable\r\nterminal length 0\r\nenable\nterminal length 0\nArista3>enable\r\nArista3#terminal length 0\r\nPagination disabled.\r\nArista3#\r\nconfigure terminal\r\nArista3#configure terminal\r\nArista3(config)#show interfaces loopback 0\r\nLoopback0 is up, line protocol is up (connected)\r\n  Hardware is Loopback\r\n  Internet address is 3.3.3.3/24\r\n  Broadcast address is 255.255.255.255\r\n  IP MTU 65535 bytes\r\n  Up 1 hour, 6 minutes, 51 seconds\r\nArista3(config)#\r\nArista3(config)#show ntp status\r\nNTP is disabled.\r\nArista3(config)#'

#Notice that there is a delimeter of \r\n throughout the output so we can split using that as the delimeter
b = a.split('\r\n')

#Now we try to find out which index the specific item we are looking for.
b.index('  Internet address is 3.3.3.3/24') # happens to be at index 12 

#Now that we have the index number we can use REGEX to get our ip address from the output
c = b[12]

#r' for raw string [0-9] expects the charcater class 0-9 1,2 0r 3 times by specifying {1,3}. \. to match the exact dot we use the escape (\) character
ip = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", c)

#We can extract it further since the ip is the only element in the list to be be able to get the ip in the form of a string
print(ip[0])