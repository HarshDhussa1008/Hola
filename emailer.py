# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported
import time
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import voice_input as vi
import speak as sp

address={
    '''
    'unqiue name for individual':'email ID',
    'nickname' : 'xyz@gmail.com',#example addressing
    '''
    }
password={
    '''
    'xyz@gmail.com' : 'password'#your password here for given address
    '''
    }
sp.speak("hi this is hola version 1.0")
time.sleep(2)
sp.speak("which mail ID to use to send the mail")
inp=vi.get_speech()
fromaddr=address[inp]
print(address[inp])
sp.speak("whom do you wish to send the mail")
inp=vi.get_speech()
toaddr=address[inp]
print(address[inp])


# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

# storing the subject
sp.speak("please suggest a title for this mail")
title=vi.get_speech()
msg['Subject'] = title

# string to store the body of the mail
sp.speak("what do you want to say to "+inp)
body=vi.get_speech()

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

'''
# open the file to be sent 
filename = "File_name_with_extension"
attachment = open("Path of the file", "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
'''

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr, password[fromaddr]) 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 
