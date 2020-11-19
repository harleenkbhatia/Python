import tkinter

root=tkinter.Tk()
root.title('List')
#scroll=tkinter.Scrollbar(root)
#scroll.pack(side=tkinter.RIGHT)

listbox=tkinter.Listbox(root)
listbox.insert(0,11)
listbox.insert(1,72)
listbox.insert(2,77)
listbox.grid(row=0,column=0)
listboxx=tkinter.Listbox(root)
listboxx.insert(0,88)
listboxx.insert(1,67)
listboxx.insert(2,34)
listboxx.grid(row=0,column=1)
def exchange(): 
        listboxx.insert(3,listbox.get(tkinter.ACTIVE))
def exchange2():
    listbox.insert(3,listboxx.get(tkinter.ACTIVE))
button=tkinter.Button(root,text='>',command=exchange)
button.grid(row=4,column=0)
button=tkinter.Button(root, text='<',command=exchange2)
button.grid(row=4, column=1)
root.mainloop()