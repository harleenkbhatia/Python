username = input("Enter Username:")
password = input("Enter Password:")
username1= "harleen"
password1= "xyz"
if username == username1 :
    if password == password1 :
        print("welcome to the portal")
else :
    count=1
    while count<=3 :
        print("try again")
        username = input("Enter Username:")
        password = input("Enter Password:")
        count+=1
    else: print("your account is locked")