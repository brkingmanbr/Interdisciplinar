from tkinter import *
from tkinter.ttk import *

# class barrademenu(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)   
#         #reference to the master widget, which is the tk window                 
#         self.master = master
#         #with that, we want to then run init_window, which doesn't yet exist
#         self.init_window()

#     def init_window(self):
#         #self.master.title("SGPS")
#         self.pack(fill=BOTH, expand=1)
#         # creating a menu instance
#         menu = Menu(self.master)
#         self.master.config(menu=menu)
#         # create the file object)
#         file = Menu(menu)
#         # adds a command to the menu option, calling it exit, and the
#         # command it runs on event is client_exit
#         file.add_command(label="Exit", command=self.client_exit)
#         #added "file" to our menu
#         menu.add_cascade(label="File", menu=file)
#         # create the file object)
#         edit = Menu(menu)
#         # adds a command to the menu option, calling it exit, and the
#         # command it runs on event is client_exit
#         edit.add_command(label="Undo")
#         #added "file" to our menu
#         menu.add_cascade(label="Edit", menu=edit)

    
#     def client_exit(self):
#         exit()

if __name__ == '__main__':
    JP = Tk()
    Frame_menu = Frame(JP)
    menu = Menu(JP)
    JP.config(menu=menu)
    file = Menu(menu)    
    menu.add_cascade(label="Editar", menu=file)
    file.add_command(label="Editar Professores") #deve abrir o CRUD de professor
    file.add_command(label="Editar Turmas") #deve abrir o CRUD de turmas
    login = Menu(menu)
    menu.add_cascade(label="Login", menu=login)
    aang = PhotoImage(file='aang.png')
    login.add_command(label="Alterar senha", image=aang, command=lambda: print('XX'))
    menu.add_cascade(label="Cronograma", command=lambda: print('XX'))
    JP.mainloop()
    exit()