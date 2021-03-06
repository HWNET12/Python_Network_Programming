from asyncio import subprocess
from ctypes.wintypes import PINT
from re import sub
import sys
import subprocess

#Checking IP reachability
def ip_reach(list):

    for ip in list:
        ip = ip.rstrip("\n")

        #To ping we are using the call method from within the subprocess module and we are passing several arguments
        #'''ping %s /n 2' % (ip)' Explanation: ping with the %s which is the string format operator and then /n 2 which is the number of echo requests to send to each device
        # Then we enter the % operator and then the single ip address'''

        #""" The next 2 arguments stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL are suppressing any output or errors from the ping command because we
        # don't want any messages generated by the ping command to interfer with the output of our application   """
        ping_reply = subprocess.call('ping %s /n 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        #ICMP type 0 echo reply which means that the ping was successful and the device is reachable
        if ping_reply == 0:
            print(f"\n (ip) is reachable :0\n")
            continue
        else:
            print(f"\n {ip} is not reachable :( Check connectivity and try again\n")
            sys.exit()

