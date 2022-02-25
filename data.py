import sys 
import os
import hashlib
from cryptography.fernet import Fernet

def encrypt(Entered_Password):
    File_R = open("data","rb")
    Content = File_R.read()    
    Entered_Password_Bytes = Entered_Password.encode()
    hash = hashlib.sha1(Entered_Password_Bytes).hexdigest()
    a = str(hash[0:16])
    #a="12345678" #Not real key
    b = "uUwt5gVisMTVff6UDP-3BKqDlO8="
    key = a+b
    f = Fernet(key)
    Encrypted_Contents = f.encrypt(Content)
    File_R.close()
    File_W = open("data", "wb")
    File_W.write(Encrypted_Contents)  
    File_W.close()

def decrypt(Entered_Password):
    File_R = open("data","rb")
    Content = File_R.read()
    Entered_Password_Bytes = Entered_Password.encode()
    hash = hashlib.sha1(Entered_Password_Bytes).hexdigest()
    a = str(hash[0:16])        
    #a="12345678" #Same Goes Here
    b = "uUwt5gVisMTVff6UDP-3BKqDlO8="
    key = a+b
    f = Fernet(key)
    Decrypted_Content = f.decrypt(Content).decode()
    File_R.close()
    File_W = open("data","w")
    write = File_W.write(Decrypted_Content)
    File_W.close()

def add(Entered_Password,URL,User,Password,Email):
    decrypt(Entered_Password)
    File_A = open("data","a")
    Data = URL+" || " +User+" || " +Password+" || " +Email+"\n"
    Content = Data
    write = File_A.write(Content)
    File_A.close()
    encrypt(Entered_Password)

def show(Entered_Password,URL):
    decrypt(Entered_Password)
    File_R = open("data","r")
    if URL == "ALL":
        print("----------------------------------------------------------------")
        for i in File_R:
            Content = i.split(" || ")
            if Content[0] != "\n"
                print ("Site"+"\t\t"+"Username"+"\t"+"E-Mail"+"\t\t\t"+"Password")
                print (Content[0]+'\t\t'+Content[1]+'\t\t'+Content[2]+'\t\t'+Content[3])
        encrypt(Entered_Password)    
    else:
        print("----------------------------------------------------------------")
        for i in File_R:
            Content = i.split(" || ")
            if Content[0] == URL:
                print ("Site"+"\t\t"+"Username"+"\t"+"E-Mail"+"\t\t\t"+"Password")
                print (Content[0]+'\t\t'+Content[1]+'\t\t'+Content[2]+'\t\t'+Content[3])
        encrypt(Entered_Password)
