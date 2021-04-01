"""A python class that is able to send an email from the terminal to a given email address
using smtplib library"""

import smtplib
from email.mime.text import MIMEText

class MailBot:
    """
    Defined parameters for connection settings , email configurations.Possess funcitons to create connection and send an email using SMTP protocol.
    Default server is gmail with connection over TLS.
    :param i_username (required): Username for login server.
    :param i_password (required): Password for login server.
    :param i_server (default gmail): SMTP server to connect.
    :param use_SSL (default False): In case connect over SSL is required. Keep as True or False.
    """
    
    def __init__(self,i_username,i_password,server_usage=("smtp.gmail.com",587),use_ssl=False):
        self.i_username = i_username
        self.i_password = i_password
        self.server_name =  server_usage[0]
        self.server_port = server_usage[1]
        self.use_ssl = use_ssl
        
        if self.use_ssl :
            self.smtpserver = smtplib.SMTP_SSL(self.server_name,self.server_port)
        else:
            self.smtpserver = smtplib.SMTP(self.server_name,self.server_port)
        
        self.connected = False
        self.recipients = []
    
    def set_message(self,message_content,i_subject="",i_from=None):
        self.msg = MIMEText(message_content,'plain')
        self.msg['Subject'] = i_subject
        if i_from is None:
            self.msg['From'] = self.i_username
        else:
            self.msg['From'] = i_from
        self.msg['To'] = None
    
    def set_recipients(self,i_recipients):
        if not isinstance(i_recipients,(list,tuple)):
            raise TypeError("Recipients data not in proper format.")
        self.recipients = i_recipients
    
        
    def connect(self):
        """
        To be called before sending messages.
        Connects to SMTP server using the provided username and password.
        """
        if not self.use_ssl:
            self.smtpserver.starttls()
        self.smtpserver.login(self.i_username,self.i_password)
        self.connected = True
    
    def disconnect(self):
        self.smtpserver.close()
        self.connected = False
    
    def send_mail(self,close_connection=False):
        """
        Sends message to all the specified recipients.
        :param close_connections (defautl = False): Decide to close the connection once email sending is complete.
        """
        if not self.connected:
            raise ConnectionError("Not Connected to any server.")
        
        for recipient in self.recipients:
            self.msg.replace_header("To",recipient)
            self.smtpserver.send_message(self.msg)
        
        if close_connection:
            self.disconnect()