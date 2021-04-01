"""
This package configures a user for sending gmail email to other recipients
"""
import re
import keyring
import getpass

class Configureuser:
    """
    Uses keyring library and stores password for gmail users in the os.
    The method involved set_email_address and set_password validates email and stores password.
    Additonally , a list of user file is also generated.
    """
    def set_password(self,password):
        self.password = password

    def set_email_address(self,email_address):
        self.regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if not re.search(self.regex,email_address):
            raise Exception("Please enter a valid email address !")
        else:
            self.email_address = email_address
    
    def validate_existing_user(self,i_email):
        self.f = open('user_configation.txt',"r")
        li_user = self.f.read().split('\n')
        if i_email in li_user:
            raise Exception("User already exists.")
    
    def store_credentials(self):
        try :
            self.validate_existing_user(self.email_address)
            keyring.set_password(self.email_address,self.email_address,self.password)
            self.f = open("user_configation.txt","a+")
            self.f.write(self.email_address + "\n")
        except Exception as ex:
            print("Faied to configure user ." + str(ex))
            return False
        return True
        

if __name__ == '__main__':
    email = str(input("Enter email : "))
    obj = Configureuser()
    print("Enter your Password (No worries . It won't be printed on your screen.): ")
    password = getpass.getpass()
    obj.set_email_address(email)
    obj.set_password(password)
    if obj.store_credentials():
        print("User Configured Successfully !")
    else:
        print("There is some problem to configure user.")
            
        
        
        