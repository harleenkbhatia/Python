#libraries to be imported
import smtplib
#calling modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr="kaurbhatiaharleen2@gmail.com"
toaddr="harleenkaurb22@gmail.com"

#instanceof MIMEMultipart.
msg= MIMEMultipart()

#storing the sender's email
msg['From']= fromaddr
#storing the receiver's email
msg['To']=toaddr
#storing subject
msg['Subject']= "test attachment"
#string to store body
body="this is a test message for attachment."
#attach the body with the msg instance.
msg.attach(MIMEText(body,'plain'))

#open file to be sent
filename=r'C:\Users\Jagdeep\PycharmProjects\untitled1\adamsNum.py'
attachment=open(filename, "rb")

#instance of MIMEBase and named as p
p = MIMEBase('application','octet-stream')
#to change the playload into encoded form
p.set_payload((attachment).read())
#encode into_base64
encoders.encode_base64(p)
p.add_header('Content-Disposition',"attachment; filename=%s"%filename)
#attach the instance 'p' to instance 'msg'
msg.attach(p)
#creates SMTP session
s= smtplib.SMTP('smtp.gmail.com',587)
#starts TLS for security
s.starttls()
#authentication
s.login(fromaddr,"gurvinder")
#Converts the Multipart msg into a  string
text=msg.as_string()
#sending the mail
s.sendmail(fromaddr,toaddr,text)
#terminating the session
s.quit()