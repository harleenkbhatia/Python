print("Hi")
FirstName=str(input("What is your First name : "))
ChatData=open("chatdata.txt",'w')
ChatData.writelines([FirstName,'\n'])
Email=input("Enter your Email ID: ")
ChatData.writelines([Email,'\n'])
PhoneNum=input("Enter a 10 digit phone no.: ")
if len(PhoneNum)!=10:
    print("Enter a valid 10 digit phone number")
    PhoneNum=input("Enter a 10 digit phone number: ")
    ChatData.writelines([PhoneNum,'\n'])
elif len(PhoneNum)==10:
    None
else:
    print("reload")
ChatData.writelines([PhoneNum,'\n'])
PinCode=str(input("Enter your area's 6 digit pincode: "))
if len(PinCode)!=6:
    print("Enter a valid 6 digit pincode")
elif len(PinCode)==6:
    None
else:
    print("reload")
ChatData.writelines([PinCode,'\n'])
Address=input("Enter your permanent address:")
ChatData.writelines([Address,'\n'])
print("welcome to our app thankyou for registering")
ChatData.close()