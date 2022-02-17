"""Enabling simulataneous ssh connections"""
import threading

#Creating threads Takes 2 parameters the list of IP addresses based on the text file with address and the ssh function\
def create_threads(list, function):

    threads = []

    for ip in list:
        th = threading.Thread(target = function, args = (ip,)) #args is a tuple with a single element
        th.start()
        threads.append(th)

    for th in threads:
        th.join()