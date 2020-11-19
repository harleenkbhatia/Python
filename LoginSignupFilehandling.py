#signup means data write krna and log in ka mtlb data read krna
file=open("signup.txt",'w')
Username="Harleen\n"
file.write(Username)
Password="abc"
file.write(Password)
def Login():
    username = input("Enter Username:")
    password = input("Enter Password:")
    file = open("signup.txt", 'r')
    if username==file.read(7):
        if password==file.read(11)[-3:] :
            print("Welcome to the portal.")
        else:
            print("Entered password is incorrect.")
    else:
        print("Entered username is incorrect")
    file.close()

def Signup():
    print("New to the Portal-Sign up")
    enterUsername = input("newUsername: ")
    enterPassword = input("newPassword: ")
    file=open("signup.txt",'w')
    file.write(enterUsername)
    file.write(enterPassword)
    file.close()
    print("signup successful")

Choice=int(input("Choose 1 for Login and 2 for Sign up : "))
if Choice==1:
    Login()
else:
    Signup()

