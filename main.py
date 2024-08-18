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
  if '''connect to somewhere:   nc [-options] hostname port[s] [ports] ...
listen for inbound:     nc -l -p port [-options] [hostname] [port]
options:
        -c shell commands       as `-e'; use /bin/sh to exec [dangerous!!]
        -e filename             program to exec after connect [dangerous!!]
        -b                      allow broadcasts
        -g gateway              source-routing hop point[s], up to 8
        -G num                  source-routing pointer: 4, 8, 12, ...
        -h                      this cruft
        -i secs                 delay interval for lines sent, ports scanned
        -k                      set keepalive option on socket
        -l                      listen mode, for inbound connects
        -n                      numeric-only IP addresses, no DNS
        -o file                 hex dump of traffic
        -p port                 local port number
        -r                      randomize local and remote ports
        -q secs                 quit after EOF on stdin and delay of secs
        -s addr                 local source address
        -T tos                  set Type Of Service
        -t                      answer TELNET negotiation
        -u                      UDP mode
        -v                      verbose [use twice to be more verbose]
        -w secs                 timeout for connects and final net reads
        -C                      Send CRLF as line-ending
        -z                      zero-I/O mode [used for scanning]''' in console_output:
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