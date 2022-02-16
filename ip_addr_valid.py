import sys
 
#Checking octets
def ip_addr_valid(iplist):
 
    for ip in iplist:
        ip = ip.rstrip("\n")
        octet_list = ip.split('.')
        
             #Making sure the ip address is not reserved(Loopback, Multicast, Broadcast, Link-Local(APIPA) and Reserved for future use 240.0.0.0-255.255.255.254)
        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            continue
             
        else:
            print(f'\n* There was an invalid IP address in the file: {ip} :(\n')
            sys.exit()