import paramiko
import os.path
import time
import sys 
import re

#Checking username/password file 
#Prompting user for unput -() USERNAME/PASSWORD
user_file = input("\n# Enter user file path and name (e.g. D:\MyApps\myfile.txt): ")

#Verifying the validity of the USERNAME/PASSWORD file
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid :)\n")

else:
    print(f"\n* {user_file} does not exist :( Please check and try again.\n")
    sys.exit()

#Checking commands file
#Prompting user for input - COMMADS FILE
cmd_file = input("\n# Enter commands file path and name (e.g. D:\MyApps\myfile.txt): ")

#Verifying the validity of the COMMANDS FILE
if os.path.isfile(cmd_file) == True:
    print("\n* Command File is valid :)\n")

else:
    print(f"\n*nFile {cmd_file} does not exist :( Please check and try again.\n")
    sys.exit()

#Open SSHv2 connection to the device
def ssh_connection(ip):

    #Importing these two variables from the global namespace into the local namespace of the ssh_connection function
    global user_file
    global cmd_file

    #Ceating SSH CONNECTION
    try:
        #Define SSH paramaters
        selected_user_file = open(user_file, 'r')

        #starting from the beginning of the file
        selected_user_file.seek(0)

        #Reading the username from the file
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

        #starting from the beginning of the file
        selected_user_file.seek(0)

        #Reading the password from the file
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

        #Logging into the device
        session = paramiko.SSHClient()

        #For testing purposes, this allows auto-accepting unknown host keys
        #Do not use in production! The default would be RejectPolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect to the device using username and password 
        session.connect(ip.rstrip("\n"), username = username, password = password)

        #Start an interactive shell session on the router
        connection = session.invoke_shell()

        #Paramiko's way of sending commands to the device. Setting terminal length for entire output - disable pagination (When you go to show run for example and there is an option for more)
        connection.send("enable\n")
        connection.send("terminal length 0\n") #Is simmillar to us typing the spacebar key on the command prompt to get more information
        time.sleep(1)

        #Entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        #Open user selected file for reading
        selected_cmd_file = open(cmd_file, 'r')

        #Starting from the beginning of the file
        selected_cmd_file.seek(0)

        #Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)

        #Closing the user file
        selected_user_file.close()

        #Closing the command file
        selected_cmd_file.close()

        #checking command output for IOS syntax errors
        router_output = connection.recv(65535)

        

        if re.search(b"% Invalid input", router_output):
            print(f"* There was atleast one IOS syntax errors on device {ip}")
        
        else:
            print(f"\nDone for device {ip} :)\n")
        
        #Test for reading command output
        #print(str(router_output) + "\n")
        #Using REGEX to exract only IPs from output - We can use the index at the end to get just the loopback address from each Arista device
        #print(re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", str(router_output))[1]) #We have to put str(router_output) or else we get TypeError: cannot use a string pattern on a bytes-like object

        #Closing the connection
        session.close()

    except paramiko.AuthenticationException:
        print("* Invalid username or password :( \n* Please check the username/password file device configuration.")
        print("* Closing program... Bye!")
