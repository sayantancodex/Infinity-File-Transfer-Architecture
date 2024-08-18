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


print("DO YOU WANT TO\n[1] SEND DATA\n[2] RECEIVE DATA\n")
ch = input()

if ch == "1":
    sender.send()
if ch == "2":
    receiver.receive()