import secrets
import string
import hashlib
def password_gen(Password_Length):
    Characters = string.ascii_letters + string.digits + "~!@#$%^&*()_-=+,.<>/?"
    Random_Password = ''.join(secrets.choice(Characters) for i in range(Password_Length))
    return Random_Password

def check(Entered_Password):
   #Put your master hash in Master_Password_Hash 
    Master_Password_Hash = "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
    Entered_Password_Bytes = Entered_Password.encode()
    Entered_Password_Hash = hashlib.sha256(Entered_Password_Bytes).hexdigest()
    if Entered_Password_Hash == Master_Password_Hash:
        return True
