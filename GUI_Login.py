import tkinter
global Login
Login = tkinter.Tk()
Login.title("Login/Signup")
Login.geometry("300x300")  # the size of window
label = tkinter.Label(Login, text="Please choose anyone option!!", background="#ecdfab", foreground="#115599").grid()
def login():
    tkinter.Label(Login, text="Enter Username : ").grid(row=1)
    tkinter.Label(Login, text="Enter Password : ").grid(row=2)
    entry = tkinter.Entry(Login)
    entry2 = tkinter.Entry(Login)
    entry2.grid(row=2, column=1)
    entry.grid(row=1, column=1)
button = tkinter.Button(Login, text="Login", command=login).grid()

def signup():
    #Signup = tkinter.Tk()
    #Signup.title("Signup")
    #Signup.geometry("300x300")  # the size of window
    #label = tkinter.Label(Signup, text="Please Signup!!", background="#ecdfab", foreground="#115599").grid()
    tkinter.Label(Login, text="New Username : ").grid(row=1)
    tkinter.Label(Login, text="New Password : ").grid(row=2)
    global entry11
    global entry22
    entry11 = tkinter.Entry(Login)
    entry22 = tkinter.Entry(Login)
    entry22.grid(row=2, column=1)
    entry11.grid(row=1, column=1)

    def signin():
        file = open("login.temp", 'a')
        file.write("{} \n".format(entry11.get()))
        file.write("{} \n".format(entry22.get()))
        file.close()
        #Signin = tkinter.Tk()
        #Signin.title("Signin")
        #Signin.geometry("300x300")  # the size of window
        label = tkinter.Label(Login, text="What you want to do?", background="#ecdfab", foreground="#115599").grid()

        def new():
            tkinter.Label(Login, text="To : ").grid(row=2)
            tkinter.Label(Login, text="Subject :").grid(row=3)
            tkinter.Label(Login, text="Message :").grid(row=4)
            entry = tkinter.Entry(Login)
            entry2 = tkinter.Entry(Login)
            entry3 = tkinter.Entry(Login)
            entry3.grid(row=4, column=1)
            entry2.grid(row=3, column=1)
            entry.grid(row=2, column=1)


        def logout():

            label = tkinter.Label(Login, text="LoggedOut", background="#ecdfab", foreground="#115599").grid()

            Login.mainloop()
            login()

        button = tkinter.Button(Login, text="New Message", command=new).grid()
        button = tkinter.Button(Login, text="Logout", command=logout).grid()

    button = tkinter.Button(Login, text="Signin",command=signin).grid(row=5, column=1)
button = tkinter.Button(Login, text="Signup", command=signup).grid()
#button=tkinter.Button(Login,text="Login",command=).grid(row=5,column=0)
Login.mainloop()


