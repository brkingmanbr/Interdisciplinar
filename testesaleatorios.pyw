####################################
####################################
##############relógio###############
# import tkinter
# from time import strftime
# relogio = tkinter.Label()
# relogio.pack()
# relogio['font'] = 'Helvetica 20 bold'
# relogio['text'] = strftime('%H:%M:%S')

# def tictac():
# 	agora = strftime('%H:%M:%S')
# 	if agora != relogio['text']:
# 		relogio['text'] = agora
# 	relogio.after(100, tictac)
# tictac()
# relogio.mainloop()
# ####################################
# ####################################

# img = PhotoImage(file='aang.png')
# exit()

from tkinter import *
from tkinter.ttk import *
JP = Tk()
JP.grid()
meses = Notebook(JP)
Janeiro = Frame(meses)

meses.add(Janeiro, text='Janeiro')
meses.grid()

#main.mes(frame=Janeiro, dias = 30, dia_da_semana_inicial = 1)

JP.mainloop()
exit()