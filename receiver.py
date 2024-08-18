import subprocess
import os
import platform
import socket
import decryptor

def receive():
    if platform.system() == "Windows":
        print("WINDOWS OS DETECTED")
        print(f"ADDRESS: {socket.gethostbyname(socket.gethostname())}")
        file_name = input("Enter File Name To be Recieved With Proper Externtion (wrong extention may lead to data corruption): ")
        dest_port = input("Enter the Reciever PORT (Default 4000)")
        if dest_port =="":
            dest_port = 4000
        os.system("echo NETCAT SERVER STARTED")
        os.system(f"ncat -nlvp {dest_port} > filedownload.sayformat")

        print("RECIEVED ENCRYPTED DATA")
        print("DECRYPTING")
        #decrypt
        decryptor.decrypt(file_name)
        print("Done")
        os.remove("filedownload.sayformat")


    if platform.system() == "Linux":

        print("LINUX OS DETECTED")
        print(f"ADDRESS: {socket.gethostbyname(socket.gethostname())}")
        file_name = input("Enter File Name To be Recieved With Proper Externtion (wrong extention may lead to data corruption): ")
        dest_port = input("Enter the Reciever PORT (Default 4000)")
        if dest_port =="":
            dest_port = 4000
        os.system("echo NETCAT SERVER STARTED")
        # os.system(f"nc -nlvp {dest_port} > filedownload.sayformat")
        console_output = subprocess.check_output(f"nc -nlvp {dest_port} > filedownload.sayformat",shell=True,text=True)
        print("")
        if "Ncat: No connection could be made because the target machine actively refused it. ." in console_output:
            print("HOST IS DOWN")
        

        print("RECIEVED ENCRYPTED DATA")
        print("DECRYPTING")
        #decrypt
        decryptor.decrypt(file_name)
        print("Done")
        os.remove("filedownload.sayformat")