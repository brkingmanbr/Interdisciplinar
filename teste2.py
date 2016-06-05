from tkinter import *
from tkinter.ttk import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root)
listbox.pack()
def x():
	return 'teste2'
y = Button(root, text=x()).pack()
a = []
for i in range(100):
	a.append(Button(root, text='teste %i'%i))
for ele in a:
	listbox.insert(END, a)

# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

mainloop()
rom tkinter import *
import webbrowser

def callback(event):
    webbrowser.open_new(r"http://www.google.com")

root = Tk()
link = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", callback)
root.mainloop()