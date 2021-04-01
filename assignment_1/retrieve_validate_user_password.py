
import keyring
class RetrieveUser:
    """
    This simulates the login functionality verifies a registered user and matches password with one stored
    and allows user to login and send email.
    : param username: The email for which user has configured password.
    """
    def __init__(self,i_username):
        self.i_username = i_username
        
    def validate_user(self):
        try:
            self.f = open('user_configation.txt',"r")
            li_user = self.f.read().split('\n')
            if self.i_username in li_user:
                print("Valid user.")
                return True
            print("User not registered. Please use the configure_user.py for registering gmail credentials safely.")
            return False
        except Exception as ex:
            print("Some problem in retrieving data ." + str(ex))
            return False
    
    def fetch_password(self):
        if self.validate_user():
            password = keyring.get_password(self.i_username,self.i_username)
            return password
        return None

    def validate_login(self,password2):
        curr_password = self.fetch_password()
        if password2.strip() == curr_password.strip():
            return True
        return False
        