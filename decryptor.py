
import os
def decrypt(filename):
    with open("filedownload.sayformat", "rb") as f:
        
        print("Reading File...")
        data = f.read()

        
    with open(f"{filename}","wb+") as g:
        
        print("Decrypting Data...")
        data2 = g.write(data[::-1])
    
    