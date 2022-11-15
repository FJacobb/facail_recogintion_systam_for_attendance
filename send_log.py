import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
import os
class mail:
    def __init__(self):
        mail_content = '''Hello,
        This is the attendance list of the student in lecture today.
        In this mail we are sending an attachment.
        This attachment is the list of student in lecture.
        Thank You
        '''
        #The mail addresses and password
        sender_address = 'projectfestus@gmail.com'
        sender_pass = 'ivpapbtuohicrkur'
        receiver_address = 'projectfestus@gmail.com'
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'A test mail sent by Python. It has an attachment.'
        #The subject line
        #The body and the attachments for the mail
        for file in os.listdir("C:/Users/festu/OneDrive/Documents/100days of code/festus_project"):
            if ".csv" in file:
                attach_file_name = str(file)
        print(attach_file_name)
        message.attach(MIMEText(mail_content, 'plain'))
        try:
            with open(attach_file_name, "rb") as attachment:
                p = MIMEApplication(attachment.read(),_subtype="pdf")
                p.add_header('Content-Disposition', "attachment; filename= %s" % attach_file_name)
                message.attach(p)
        except Exception as e:
            print(str(e))
        #Create SMTP session for sending the mail
        with smtplib.SMTP('smtp.gmail.com', 587) as session: #use gmail with port
            session.starttls() #enable security
            session.login(user=sender_address, password=sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
        return "Mail Sent"