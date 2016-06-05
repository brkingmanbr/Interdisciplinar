from tkinter import *
from tkinter.ttk import *


nome_usuario = 'Jailson Mendes'

j = Tk()
j.title('SGPS - Bem vindo %s'%nome_usuario)
j.geometry('800x600')

LinhaMenu = Frame(j).grid(row=0, column=0)
menu = Menu(LinhaMenu)

l2 = Frame(j).grid(row=1, column=0)

Professor = Label(l2, text='Professor: ').grid(row=0, column=0)
professor = StringVar(); professor.set('Rasta das Terras de Shambalá')
Entry(l2, textvariable=professor, width=25).grid(row=0, column=1)

Turma = Label(l2, text='Turma: ').grid(row=0, column=3)
turma = StringVar(); turma.set('Turma 50419')
Entry(l2, textvariable=turma, width=25).grid(row=0, column=4)

Button(l2, text='Ok', width=25).grid(row=0, column=5)

j.mainloop()