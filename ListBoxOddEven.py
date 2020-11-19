import tkinter
OddEven=tkinter.Tk()
OddEven.title('Odd Even List')
entry=tkinter.Entry(OddEven)
entry.grid()
def enter():

    data = int(entry.get())
    OddEven.title('Odd Even')
    listbox = tkinter.Listbox(OddEven)
    listboxx = tkinter.Listbox(OddEven)
    listbox.grid(row=0, column=1)
    listboxx.grid(row=0, column=2)
    i = 1
    for i in range(i, data + 1):
        if i % 2 == 0:
            a=0
            listbox.insert(a,i)
            a += 1
            i += 1

        else:
            a=0
            listboxx.insert(a,i)
            i += 1
            a+=1

button=tkinter.Button(OddEven,text="Submit",command=enter)
button.grid()
OddEven.mainloop()

