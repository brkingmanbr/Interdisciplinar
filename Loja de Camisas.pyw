from tkinter import *
from tkinter.ttk import *
import pymysql as bd

def conectaBanco():
    parametros = {'user':user.get(),
                  'host':host.get(),
                  'passwd':senha.get(),
                  'autocommit':True}
    global banco
    banco = bd.connect(**parametros)
    global c 
    c = banco.cursor()
    c.execute('''
            CREATE DATABASE IF NOT EXISTS loja;
            use loja;
            create table IF NOT EXISTS tamanho(
            tamanho varchar(30) primary key
            );
            create table IF NOT EXISTS cor(
            cor varchar(30) primary key
            );
            create table IF NOT EXISTS camisa(
            quantidade int,
            cor_c varchar(30),
            tamanho_t varchar(30),
            preço float,
            foreign key (cor_c) references cor(cor),
            foreign key (tamanho_t) references tamanho(tamanho)
            );
            ''')
    tamanho = buscatamanhos()
    cor = buscacores()
    for ta in tamanho:
        c.execute("INSERT INTO tamanho SELECT * FROM (SELECT '%s') AS x WHERE NOT EXISTS ( SELECT * FROM tamanho WHERE tamanho = '%s') LIMIT 1;"%(ta,ta))
    for co in cor:
        c.execute("INSERT INTO cor SELECT * FROM (SELECT '%s') AS x WHERE NOT EXISTS ( SELECT * FROM cor WHERE cor = '%s') LIMIT 1;"%(co,co))
    for co in cor:
        for ta in tamanho:
            c.execute("INSERT INTO camisa SELECT * FROM (SELECT 0, '%s','%s', 0.0) AS x WHERE NOT EXISTS ( SELECT * FROM camisa WHERE cor_c = '%s'and tamanho_t = '%s') LIMIT 1;"%(co, ta, co, ta))	
def buscaquant(tamanho, cor):
    c.execute("SELECT quantidade FROM loja.camisa WHERE cor_c = '%s' and tamanho_t = '%s' "%(cor, tamanho))
    return c.fetchone()
def buscapreco(tamanho, cor):
    c.execute("SELECT preço FROM loja.camisa WHERE cor_c = '%s' and tamanho_t = '%s' "%(cor, tamanho))
    return c.fetchone()
def buscatamanhos():
    c.execute("SELECT tamanho FROM loja.tamanho")
    x = c.fetchall()
    resultado = []
    for linha in x:
        resultado.append(linha[0])
    return resultado
def buscacores():
    c.execute("SELECT cor FROM loja.cor")
    x = c.fetchall()
    resultado = []
    for linha in x:
        resultado.append(linha[0])
    return resultado
def add(quantidade, tamanho, cor):
    c.execute("SELECT quantidade FROM loja.camisa WHERE cor_c = '%s' and tamanho_t = '%s' "%(cor, tamanho))
    x = c.fetchone()
    x = x[0]+quantidade
    c.execute("UPDATE loja.camisa SET quantidade = %i WHERE cor_c = '%s' and tamanho_t = '%s' "%(x, cor, tamanho))
    c.fetchone()
    refresh()
def delete(quantidade, tamanho, cor):
    c.execute("SELECT quantidade FROM loja.camisa WHERE cor_c = '%s' and tamanho_t = '%s' "%(cor, tamanho))
    x = c.fetchone()
    x = x[0]-quantidade
    c.execute("UPDATE loja.camisa SET quantidade = %i WHERE cor_c = '%s' and tamanho_t = '%s' "%(x, cor, tamanho))
    c.fetchone()
    refresh()
def teste(t):
    print(t)
def preco(preco, tamanho, cor):
    c.execute("SELECT preço FROM loja.camisa WHERE cor_c = '%s' and tamanho_t = '%s' "%(cor, tamanho))
    x = c.fetchone()
    x = float(preco)-x[0]
    c.execute("UPDATE loja.camisa SET preço = %i WHERE cor_c = '%s' and tamanho_t = '%s' "%(x, cor, tamanho))
    c.fetchone()
    refresh()
def refresh():
    for widget in t.winfo_children():
    	widget.destroy()
    criarTabela()
def criarTabela():
    Label(t, text='Loja de Camisas', justify='center').grid(row=0, column=0, columnspan=4)
    Label(t, text='Quantidade', justify='center', width=15).grid(row=1, column=0)
    Label(t, text='Cor', justify='center', width=15).grid(row=1, column=1)
    Label(t, text='Tamanho', justify='center', width=15).grid(row=1, column=2)
    Label(t, text='Preço UN', justify='center', width=15).grid(row=1, column=3)
    
    tamanho = buscatamanhos()
    cor = buscacores()
    linha = 2
    for ta in tamanho:
        for co in cor:
            Label(t, text=buscaquant(ta, co)).grid(row=linha, column=0)
            Label(t, text=co).grid(row=linha, column=1)
            Label(t, text=ta).grid(row=linha, column=2)
            Label(t, text=buscapreco(ta, co)).grid(row=linha, column=3)
            linha+=1
def criarBOT():
    bot = Frame(tk)
    bot.grid(row=1, column=0)
    Label(bot, text='Cor').grid(row=22, column=0)
    color = StringVar(bot); Entry(bot, textvariable=color).grid(row=23, column=0)
    Label(bot, text='Tamanho').grid(row=22, column=1)
    size = StringVar(bot); Entry(bot, textvariable=size).grid(row=23, column=1)
    Label(bot, text='Quantidade').grid(row=22, column=2)
    amount = StringVar(bot); Entry(bot, textvariable=amount).grid(row=23, column=2)
    Label(bot, text='Preço').grid(row=22, column=3)
    valor = DoubleVar(bot); Entry(bot, textvariable=valor).grid(row=23, column=3)
    Button(bot, text='++Quantidade', command=lambda:add(int(amount.get()), size.get(), color.get())).grid(row=24, column=0, sticky='EW')
    Button(bot, text='--Quantidade', command=lambda:delete(int(amount.get()), size.get(), color.get())).grid(row=24, column=1, sticky='EW')
    Button(bot, text='DefinirPreço', command=lambda:preco(valor.get(), size.get(), color.get())).grid(row=24, column=2, sticky='EW')
def iniciare(event):
    iniciar(jaIniciou)
def iniciar(iniciou):
    if iniciou == False:
        conectaBanco()
        criarTabela()
        criarBOT()
        inicio.destroy()
        jaIniciou = True

if __name__ == '__main__':
    jaIniciou = False
    tk  = Tk()
    t = Frame(tk)
    t.grid(row=0, column=0)
    inicio = Frame(tk)
    inicio.grid(row=1, column=0)
    user = StringVar()
    user.set('root')
    host = StringVar()
    host.set('localhost')
    senha = StringVar()
    Label(inicio, text='Insira os parametros do banco de dados').grid(row=0, column=0, columnspan=2)
    Label(inicio, text='User', justify='left').grid(row=1, column=0)
    Entry(inicio, textvariable=user).grid(row=1, column=1)
    Label(inicio, text='Host', justify='left').grid(row=2, column=0)
    Entry(inicio, textvariable=host).grid(row=2, column=1)
    Label(inicio, text='Password', justify='left').grid(row=3, column=0)
    Entry(inicio, textvariable=senha).grid(row=3, column=1)
    Button(inicio, text='OK', command=lambda:iniciar(jaIniciou)).grid(row=4, column=1, columnspan=1)
    tk.bind("<Return>", iniciare)
    tk.mainloop()
    banco.close()