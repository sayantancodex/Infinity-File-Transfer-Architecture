import os
import platform
import socket
import encryptor
import time


def send():
    if platform.system() == "Windows":
        print("WINDOWS OS DETECTED")
        print(f"ADDRESS: {socket.gethostbyname(socket.gethostname())}")
        file_name = input("Enter File Path to be sent (With Proper Extention): ")
        dest_ip = input("Enter Receiver IP Address: ")
        dest_port = input("Enter the Reciever PORT (Default 4000)")
        if dest_port =="":
            dest_port = 4000
        print("ENCRYPTING DATA FOR A SECURE TRANSFER")
        #encrypt
        encryptor.encrypt(file_name)
        time.sleep(5)
        os.system("echo NETCAT SERVER STARTED")
        a = os.system(f"ncat {dest_ip} {dest_port} < filedownload.sayformat")
        
        os.remove("filedownload.sayformat")

    if platform.system() == "Linux":

        print("LINUX OS DETECTED")
        print(f"ADDRESS: {socket.gethostbyname(socket.gethostname())}")
        file_name = input("Enter File Path to be sent (With Proper Extention): ")
        dest_ip = input("Enter Receiver IP Address: ")
        dest_port = input("Enter the Reciever PORT (Default 4000)")
        if dest_port =="":
            dest_port = 4000
        print("ENCRYPTING DATA FOR A SECURE TRANSFER")
        encryptor.encrypt(file_name)
        time.sleep(5)
        os.system("echo NETCAT SERVER STARTED")
        os.system(f"nc {dest_ip} {dest_port} < filedownload.sayformat")

        
        os.remove("filedownload.sayformat")
