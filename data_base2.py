import mysql.connector
conn=mysql.connector.connect(user='root', password='root', host='localhost',database='MachineLearning')
mycursor=conn.cursor()
#mycursor.execute('create table ML(Name VARCHAR(20),Email VARCHAR(40), MobileNo VARCHAR(20))')
#s= "create table MLL(Name VARCHAR(20),Email VARCHAR(40), MobileNo VARCHAR(20));"
#s="insert into MLL(Name,Email,MobileNo) VALUES('Har','har1@gmail.com','9899994895');"
s="select * from MLL where Name='Har';"
#s="select * from MLL"
mycursor.execute(s)
data=mycursor.fetchall()
for i,j,k in data:
    print('''\
    Name: {}
    Email: {}
    MobileNo: {}    
    '''.format(i,j,k))
conn.close()
#conn.commit() #whichever changes like inserting data you make will be updated in the table/database
print("Data updated")
