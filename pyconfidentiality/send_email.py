import os
import smtplib  # This module is defines an SMTP client session object that can be used to send mail
from email.message import EmailMessage, message


def send_message(username, password, reciever, subject, msg, mode=1):
    '''
    Send emails using GMAIL
    '''
    # For security purpose it is always recommended to grab the sender's email address and password from the system
    # However you can simply put in the creditials as strings to the variables if needed
    Email_id = username  # Sender's email address obtained
    Email_password = password  # Sender's password
    Test_email_id = reciever  # Receiver's password

    # Craft the email
    msg = EmailMessage()  # Creating an email object
    msg['Subject'] = subject  # Subject of the message
    msg['From'] = Email_id  # Sender's email address
    msg['To'] = Test_email_id  # Receiver's email address
    # For sending to multiple recievers,open a .csv file and read the email address in a list of strings and pass the list
    msg.set_content(msg)
    # Set up SMTP Session over SSL
    transmission_mode = mode
    if transmission_mode == 1:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Email_id, Email_password)  # Authentication
            smtp.send_message(msg)  # Send the message
    else:
        # If you are facing timeout-error for SSL and lack time then use the following

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()  # Encrypt the traffic using Tranport Layer Security
            smtp.ehlo()
            smtp.login(Email_id, Email_password)  # Authentication
            smtp.send_message(msg)  # Send the message
