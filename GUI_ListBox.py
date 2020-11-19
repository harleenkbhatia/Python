#passes values in a list but inside a window
import tkinter

root=tkinter.Tk()
root.title('List')
#scroll=tkinter.Scrollbar(root)
#scroll.pack(side=tkinter.RIGHT)

listbox=tkinter.Listbox(root)
listbox.insert(0,'Ashish')
listbox.insert(1,'Innovate')
listbox.insert(2,'Yourself')
listbox.grid()
button=tkinter.Button(root,text='Show',command=lambda :print(listbox.get(tkinter.ACTIVE)))
button.grid()
root.mainloop()