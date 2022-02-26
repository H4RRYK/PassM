import argparse
import pass_util
import sys
import getpass
import data
import os

def main():

    par = argparse.ArgumentParser(description="testing",usage="[options]")

    Entered_Password = getpass.getpass("Enter master key:");

    n = len(sys.argv)       

    if pass_util.check(Entered_Password) is True:
        print("Authentication Complete!")

    else:
        print("Accesse Denied!")
        sys.exit()

    par.add_argument("-a","--add",help="Add new entry",metavar="",type=int,const=1,nargs="?")
    par.add_argument("-ap","--add_pass",help="Add password manually",metavar="",const=1,nargs="?")
    par.add_argument("-s","--show",help="Show by site",metavar="Site's name/Domain",const=1,nargs="?")
    par.add_argument("-e","--encrypt",help="Encyprt the data file.Try not to double encrypt the file.",metavar="",const=1,nargs="?")
    par.add_argument("-d","--decrypt",help="Decrypt the data file.Dont forget to re-encrypt the file or the programe will fail.",metavar="",const=1,nargs="?")
    args = par.parse_args()

    def int_table():
        print ("--------------------------")
        print ("What would you like to do?")
        i = input("Select ([A]dd,[S]how,[E]ncrypt,[D]ecrypt,[Q]uit) : ")
        if i.upper() == "Q":
            sys.exit()  
        
        if i.upper() == "S":
            show()

        if i.upper() == "E":
            data.encrypt(Entered_Password)
            print ("Your Data file has been encrypted!")
            Rerun()

        if i.upper() == "D":
            data.decrypt(Entered_Password)
            print("Your Data file has been decrypted! Make sure to re-encrypt the data file once done.")
            Rerun()
            
        if i.upper() == "A":
            select = input("Do You Want To Generat A Password (Y/n) : ")
            
            if select.upper() == "Y":
                add()
        
            if select.upper() == "N":
                add_pass()  
        
    def add():
        URL = input("Enter the website name :")
        User = input("Enter your username for this site :")
        Email=input("Enter yout e-mail used for this site :")
        Pass_Len=input("What length do you want your password to be?(Default is 16) :") or 16
        Assword=pass_util.password_gen(int(Pass_Len))
        print("Your Data is successfully Saved.")
        print("---------------------")
        print("Site     : "+URL)   
        print("Username : "+User)
        print("E-mail   : "+Email)
        print("Password : "+Assword)
        print("---------------------")
        data.add(Entered_Password, URL, User, Email, Assword)
        Rerun()

    def add_pass():
        URL = input("Enter the website name :")
        User = input("Enter your username for this site :")
        Email=input("Enter yout e-mail used for this site :")
        Assword=input("Enter your Password for this site :")
        print("Your Data is successfully Saved.")
        print("---------------------")
        print("Site     : "+URL)   
        print("Username : "+User)
        print("E-mail   : "+Email)
        print("Password : "+Assword)
        print("---------------------")
        data.add(Entered_Password, URL, User, Email, Assword)
        Rerun()

    def show():
        URL = input("Which site are you trying to access?(Default = ALL) :") or "ALL"
        data.show(Entered_Password, URL)
        Rerun()

    def Rerun():
        Re_Run = input("Would you like to re-run the application?(Y/N):")

        if Re_Run.upper() == "Y":
            int_table()

        else:
            os.system('cls')
            sys.exit()

    if args.add:
        add()

    if args.add_pass:
        add_pass()

    if args.show:
        show()

    if n == 1:
        int_table()

if __name__ == "__main__":
    main()
