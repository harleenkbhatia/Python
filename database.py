import mysql.connector
mydb=mysql.connector.connect(user="root", password="root",host="localhost",database="Harleen")
cursorr=mydb.cursor()
name=str(input("Enter your Name: "))
Email=str(input("Enter your Email ID: "))
MobileNo=int(input("Enter your mobile no.: "))

#query="create table Data(UserId VARCHAR(10), Name VARCHAR(20), Email VARCHAR(20), MobileNo VARCHAR(20));"
s="insert into Data(UserId, Name, Email, MobileNo) values (,name,Email,MobileNo);"
#query="select * from Data;"
cursorr.execute(s)
mydb.commit()

print("data updated")