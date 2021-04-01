# TO DO 
# Take input as subject , body and recipient list 
# Store them in a variable call your defined class and shoot and email.j

# Create a script to configure the username and password 
# store password using database or any technique
# retrieve that password and configure 
# send email using  that 
import getpass
from assignment_1 import mail_sender
from assignment_1 import retrieve_validate_user_password
sender = str(input("Sender ?"))
obj = retrieve_validate_user_password.RetrieveUser(sender)
pwd = obj.fetch_password()
if pwd is None:
    print(sender + " is not registered . Please trigger configure_user.py script for registering the user.")
    exit()

print("Registered User ! Enter password for login (No worries password won't  be displayed on screen) : ")
count = 3
login = False
while count != 0:
    password2 = getpass.getpass()
    print(password2)
    if obj.validate_login(password2):
        login = True
        print("User login success ! Proceed to send mail.")
        break
    else:
        count -= 1
        print("Invalid password.Retry count left " + str(count))

if login:
    subject = str(input("Subject ?"))
    body = str(input("Body ?"))
    recipient = str(input("Recipients ?"))
    mailbotobj = mail_sender.MailBot('animeshsaxena78@gmail.com','mummyanimeshAM123',('smtp.gmail.com',587),False)
    mailbotobj.set_message(body,subject,"Animesh Saxena")
    mailbotobj.set_recipients([recipient])
    mailbotobj.connect()
    mailbotobj.send_mail()
    print("Email sent !")
else:
    print("Failed to login. Trigger script again and enter right credentials.")
