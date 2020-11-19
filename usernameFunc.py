dictionary = {'harleen': "xyz", "rahul": "abc", "rohit": "opq"}
def Login():
    username = input("Enter Username:")
    password = input("Enter Password:")
    try:
        if password in dictionary[username]:
            print("Welcome to the portal.")
    except:
        print("Entered username or password is incorrect.")
def Signup():
    print("New to the Portal-Sign up")
    Name = input("Name: ")
    enterUsername = input("Username: ")
    enterPassword = input("Password: ")
    dictionary.update({enterUsername: enterPassword})
    print(dictionary)
    Login()
Choice=int(input("Choose 1 for Login and 2 for Sign up : "))
if Choice==1:
    Login()
else:
    Signup()
'''
def Login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    username1 = "harleen"
    password1 = "xyz"
    if username == username1:
        if password == password1:
            print("welcome to the portal")
    else:
        count = 1
        while count <= 3:
            print("try again")
            username = input("Enter Username:")
            password = input("Enter Password:")
            count += 1
        else:
            print("your account is locked")
def Signup():
        Name = input("Enter your name: ")
        Age = input("Enter your age: ")
        Username = input("Enter your username: ")
        Password = input("Enter password: ")
Choice=int(input("Choose 1 for Login and 2 for Sign up : "))
if Choice==1:
    Login()
else:
    Signup()
'''