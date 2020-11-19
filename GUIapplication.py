import tkinter
window=tkinter.Tk()
window.title("Innovate Yourself")
window.geometry("200x200") #the size of window
label=tkinter.Label(window,text="Hello World", background="#ecdfab", foreground="#115599")
label.grid()
entry=tkinter.Entry(window)
entry.grid()

#print("entered text: ",entry.get())
#help(tkinter.Label)
def enter():
    print('entered data',entry.get())
    data = tkinter.Label(window, text="{}".format(entry.get()))
    data.grid()
button=tkinter.Button(window,text="Submit",command=enter).grid()
def data1():
    a=c1.get()
    b=c2.get()
    c=c3.get()
    if a==1:
        print("Foot Ball is selected")
    elif b==1:
        print('Basket ball is selected')
    else:
        print('Cricket is selected')
c1=tkinter.IntVar()
c2=tkinter.IntVar()
c3=tkinter.IntVar()
check1=tkinter.Checkbutton(window, text="Foot ball",variable=c1,command=data1)
check2=tkinter.Checkbutton(window, text="Basket ball",variable=c2,command=data1)
check3=tkinter.Checkbutton(window, text="Cricket",variable=c3,command=data1)
check1.grid()
check2.grid()
check3.grid()

#radio button used to select from multiple options.
def data2():
    p=rb.get()
    q=rb.get()
    if p==1:
        print("MALE is selected")
    else:
        print('FEMALE is selected')
rb=tkinter.IntVar()
rb1=tkinter.Radiobutton(window,text="MALE",variable=rb,value=1,command=data2)
rb2=tkinter.Radiobutton(window,text="FEMALE",variable=rb,value=2,command=data2)
rb1.grid()
rb2.grid()
window.mainloop()
