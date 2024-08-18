import sender
import receiver
import subprocess
import sys
import platform

print('''                                                 
          :=+***+=-.           :=+***+=-          
       :*@@@@@@@@@@@#=     .=#@@@@@@@@@@@#=       
     .#@@@@%*===+#@@@@@=  :@@@@@#*===+#@@@@%:     
    .@@@@#.        +@@@@#. .%#-        .*@@@@.    
    +@@@%           .#@@@%:              *@@@*    
    #@@@=             =@@@@+             -@@@%    
    *@@@#              :%@@@%.           *@@@*    
    .@@@@*.        -#%: .#@@@@+.       .*@@@@.    
     :%@@@@#+=-=+#@@@@@-  -%@@@@#+=-=+#@@@@%.     
       =#@@@@@@@@@@@%+:     =%@@@@@@@@@@@#-       
         .-+*###*+-.          .-+*###*+-.         
''')

print("WELCOME TO INFINITY FILE TRANSFER ARCHITECTURE")
if platform.system() == "Windows":
  console_output = subprocess.check_output("ncat -h",shell=True,text=True)
  if ''' https://nmap.org/ncat ''' in console_output:
      
      print("[+] NETCAT INSTALLATION FOUND")
  else:
    print("[x] NO NETCAT INSTALLATION FOUND PLEASE INSTALL NETCAT FIRST!")
    sys.exit()

if platform.system() == "Linux":
  console_output = subprocess.check_output("nc -h",shell=True,text=True)
  if '''nc''' in console_output:
      print("[+] NETCAT INSTALLATION FOUND")
  else:
    print("[x] NO NETCAT INSTALLATION FOUND PLEASE INSTALL NETCAT FIRST!")
    sys.exit()
   


print("DO YOU WANT TO\n[1] SEND DATA\n[2] RECEIVE DATA\n")
ch = input()

if ch == "1":
    sender.send()
if ch == "2":
    receiver.receive()