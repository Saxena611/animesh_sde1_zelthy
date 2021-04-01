# SDE1 ASSIGNMENT - ZELTHY

_Language: Python3
Virtual Environment Setup : Run command <pip or pipenv (depending upon the venv)> install -r requirements.txt

## Assignment 1:
Write a python class that is able to send an email from the terminal to a given email address
using smtplib library.

Solution:
Along, with send_mail I have tried to simulate a user management functionality as well.
This has enabled this challenge solution to be used by multiple user without actually exposing their gmail credentials as hardcoded parameters.
Inside package assignment_1 it comprises of thress file with the functionality as defined below:

- configure_user.py : 
    - This script configure the user gmail credentials and safely stores them into the os using keyring technique.
    - Creates and maintains a user_configurations.txt file which maintains the list of users registered.
    - Command : python -m assignment_1.configure_user 
    - You will be asked to enter your gmail username and password which will be safely stored as secret in os.
- mail_sender.py :
    - This script will shoot an email to the provided recipients.
    - This will first make you login by verifying the password on the provided username.
    - Command : python -m assignment_1.send_email
- retrieve_validate_user_password:
    - This is internally used by configure_user and mail_sender for validating existing user and password matching.
    - Type of usermanagement.



