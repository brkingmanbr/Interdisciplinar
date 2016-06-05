from tkinter import *
#import tkinter as tk
from tkinter.ttk import *

'''dias de 0 a 6
segunda = 0
domingo = 6
'''

def mes(frame, nome_do_mês = 'sem nome', dias = 30, dia_da_semana_inicial = 0):
    diaAtual = dia_da_semana_inicial+1
    dia = 1
    Button(frame, text='♪┏ ( ･o･) ┛♪┗ (･o･ ) ┓♪').grid(row=0, column=0, columnspan=8, sticky='WE')
    Label(frame, text='Segunda').grid(row=1, column=+2)
    Label(frame, text='Terça').grid(row=1, column=+3)
    Label(frame, text='Quarta').grid(row=1, column=+4)
    Label(frame, text='Quinta').grid(row=1, column=+5)
    Label(frame, text='Sexta').grid(row=1, column=+6)
    Label(frame, text='Sábado').grid(row=1, column=+7)
    Label(frame, text='Domingo').grid(row=1, column=+1)

    for linha in range(2, 23, 5):#18, 5):
        if diaAtual <= dias:
            Label(frame, text='7:30 - 8:30').grid(row=linha+1, column=0)
            Label(frame, text='8:30 - 9:30').grid(row=linha+2, column=0)
            Label(frame, text='9:30 - 10:30').grid(row=linha+3, column=0)
            Label(frame, text='10:30 - 11:30').grid(row=linha+4, column=0)
            for coluna in range(diaAtual, 8):
                if dia <= dias:
                    Button(frame, text='Dia: %i'%dia).grid(row=linha, column=coluna)
                    Button(frame, text='7:30 - 8:30').grid(row=linha+1, column=coluna)
                    Button(frame, text='8:30 - 9:30').grid(row=linha+2, column=coluna)
                    Button(frame, text='9:30 - 10:30').grid(row=linha+3, column=coluna)
                    Button(frame, text='10:30 - 11:30').grid(row=linha+4, column=coluna)
                    dia += 1
            diaAtual = 1

if __name__ == '__main__':
    JP = Tk()
    JP.resizable(False, False)
    tudo = Frame(JP).grid()
    meses = Notebook(JP)

    Janeiro = Frame(meses)
    Fevereiro = Frame(meses)
    Março = Frame(meses)
    Abril = Frame(meses)
    Maio = Frame(meses)
    Junho = Frame(meses)
    Julho = Frame(meses)
    Agosto = Frame(meses)
    Setembro = Frame(meses)
    Outubro = Frame(meses)
    Novembro = Frame(meses)
    Dezembro = Frame(meses)

    meses.add(Janeiro, text='Janeiro')
    meses.add(Fevereiro, text='Fevereiro')
    meses.add(Março, text='Março')
    meses.add(Abril, text='Abril')
    meses.add(Maio, text='Maio')
    meses.add(Junho, text='Junho')
    meses.add(Julho, text='Julho')
    meses.add(Agosto, text='Agosto')
    meses.add(Setembro, text='Setembro')
    meses.add(Outubro, text='Outubro')
    meses.add(Novembro, text='Novembro')
    meses.add(Dezembro, text='Dezembro')
    meses.grid()
    #26 Linhas por mês normal de 30 dias
    #meses = 'Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'
    mes(frame=Janeiro,dias = 30, dia_da_semana_inicial = 1)
    mes(frame=Fevereiro, dias=31, dia_da_semana_inicial = 2)
    mes(frame=Março, dias=30, dia_da_semana_inicial = 3)
    mes(frame=Abril, dias=31, dia_da_semana_inicial = 4)
    mes(frame=Maio, dias=30, dia_da_semana_inicial = 5)
    mes(frame=Junho, dias=31, dia_da_semana_inicial = 5)
    mes(frame=Julho, dias=30, dia_da_semana_inicial = 6)
    mes(frame=Agosto, dias=31, dia_da_semana_inicial = 7)
    mes(frame=Setembro, dias=30, dia_da_semana_inicial = 1)
    mes(frame=Outubro, dias=31, dia_da_semana_inicial = 2)
    mes(frame=Novembro, dias=31, dia_da_semana_inicial = 3)
    mes(frame=Dezembro, dias=30, dia_da_semana_inicial = 4)
    JP.mainloop()
    exit()