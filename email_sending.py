#smtp- simple mail transfer protocol
import smtplib

host= "smtp.gmail.com"
port =465 #SSL TLS 587

emailid="kaurbhatiaharleen2@gmail.com"
Sname="Harleen"
Rname1, Rname2 ="Maitree","Sarah"
password="gurvinder"
receiver="harleenkaurb22@gmail.com","harleenkaurbhatia4@gmail.com"
subject="Test Mail."
dictionary={Sname:Rname1, Sname:Rname2}
for i,v in dictionary.items():
    body="Hey! This is", i, ". How are you", v, "? Hope you are doing well. Happy Diwali, May this diwali enlightens " \
     "your upcoming year."
email_text='''\
From:{0}
To:{1}
{2}
{3}
'''.format(emailid,receiver,subject,body)
#connecct to the server
server= smtplib.SMTP_SSL(host,port)
server.ehlo()
#login to the server
server.login(emailid,password)
server.sendmail(emailid,receiver,email_text)
server.close()