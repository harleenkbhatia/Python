import tkinter
Prime=tkinter.Tk()
Prime.title('Odd Even List')
entry=tkinter.Entry(Prime)
entry.grid()
def enter():

    data = int(entry.get())
    Prime.title('Prime')
    listbox = tkinter.Listbox(Prime)
    listboxx = tkinter.Listbox(Prime)
    listbox.grid(row=0, column=1)
    listboxx.grid(row=0, column=2)
    i = 1
    for num in range(2, data + 1):
        if num > 0:
            for i in range(2, num):
                if num % i == 0:
                    listbox.insert(0,num)
                    break
            else:
                listboxx.insert(0,num)

button=tkinter.Button(Prime,text="Submit",command=enter)
button.grid()
Prime.mainloop()