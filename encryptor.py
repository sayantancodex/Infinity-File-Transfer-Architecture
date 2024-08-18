import os
def encrypt(filename):
    os.chmod(filename, 0o666)
    with open(f"{filename}", "rb") as f:
        print("Reading File...")
        data = f.read()

    with open("filedownload.sayformat","wb+") as g:
        os.chmod("filedownload.sayformat", 0o666)    
        
        print("Encrypting Data...")
        data2 = g.write(data[::-1])
    
    