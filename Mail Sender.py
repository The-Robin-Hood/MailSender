import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = raw_input("Enter the valid username of smtp2go")
password = raw_input("Enter the password")
msg = MIMEMultipart('mixed')

sender = raw_input("Enter the Sender Email ID :")
No_of_recipient= int(raw_input("Enter the Number of recipients:"))
if (No_of_recipient == 1):
    recipient = raw_input("Enter the Recipient Email ID:")
elif (No_of_recipient>1):
    recipient=[]
    for i in  range(No_of_recipient):      
        recipient.append(raw_input("Enter the Recipients:"))
else:
    print("Enter a Valid Number")
msg['Subject'] = raw_input("Enter the Subject:")
msg['From'] = sender
msg['To'] = ",".join(recipient)
Format= raw_input("Enter the format of the mail P or H(Plain OR Html):")
P ="P"
H="H"
if (Format == P):
    Format = "plain"
elif (Format == H ):
    Foramt = "html"
else:
    print("Enter a Valid Format H or P !!")
    exit(1)
Content=raw_input("Enter the Content of the Mail:")

    
text_message = MIMEText(Content, Format)
msg.attach(text_message)

mailServer = smtplib.SMTP('mail.smtp2go.com', 2525) # 8025, 587 and 25 can also be used. 
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(username, password)
mailServer.sendmail(sender, recipient, msg.as_string())
mailServer.close()
