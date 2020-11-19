username = input("Enter Username:")
password = input("Enter Password:")
dictionary={'harleen':"xyz","rahul":"abc","rohit":"opq"}
try:
    if password in dictionary[username]:
        print("Welcome to the portal.")
except:
        print("Entered username or password is incorrect.")
finally:
    print("New to the Portal-Sign up")
    Name=input("Name: ")
    enterUsername=input("Username: ")
    enterPassword=input("Password: ")
    dictionary.update({enterUsername : enterPassword})
    print(dictionary)
