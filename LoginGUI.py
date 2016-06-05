from tkinter import *
from tkinter.ttk import *
from time import strftime
from PIL import Image, ImageTk
from Control import *

class Visao(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.master.Co = Controle()
		#self.start_login()
		#self.cronograma()
		self.start_menu()
		#self.refresh()
		#self.professor()
		#self.cronograma()
		self.turma()

	def start_menu(self):
		self.menu = Menu(self.master)
		self.master.config(menu=self.menu)
		self.file = Menu(self.menu)    
		self.menu.add_cascade(label="Editar", menu=self.file)
		self.file.add_command(label="Editar Professores", command=self.professor) #deve abrir o CRUD de professor
		self.file.add_command(label="Editar Turmas", command=self.turma) #deve abrir o CRUD de turmas
		self.login = Menu(self.menu)
		self.menu.add_cascade(label="Login", menu=self.login)
		#self.aang = PhotoImage(file='aang.png')
		#self.login.add_command(label="Alterar senha", image=self.aang, command=lambda: print('XX'))
		self.menu.add_cascade(label="Cronograma", command= self.cronograma)

	def start_login(self):
		self.refresh()
		self.master.title("Tela de Login")
		self.master.resizable(False,False)
		self.grid()
		load = Image.open('aang.png')
		render = ImageTk.PhotoImage(load)
		img = Label(self, image=render)
		img.image = render
		img.grid(row=0, column=0, columnspan=2)

		UsuarioL = Label(self, text='Username: ', anchor='w').grid(row=1, column=0, sticky='we')
		user = StringVar()
		UsuarioE = Entry(self).grid(row=1, column=1, sticky='we')
		SenhaL = Label(self, text='Password: ', anchor='w').grid(row=2, column=0, sticky='we')
		senha = StringVar()
		SenhaE = Entry(self).grid(row=2, column=1, sticky='we')
		Login = Button(self, text='Login', command=lambda: self.verifica_login(user.get(), senha.get())).grid(row=3, columnspan=2, sticky='we')
		self.master.title("Tela de Login")
	
	def ignorar_tictac(self):
		self.agora = strftime('%H:%M:%S')
		if self.agora != relogio['text']:
			relogio['text'] = agora
		relogio.after(100, tictac)
		
		tictac()
		self.relogio = tkinter.Label()
		relogio['font'] = 'Helvetica 20 bold'
		relogio['text'] = strftime('%H:%M:%S')


	def verifica_login(self, login, senha):
		print('isso tem que estar no controle'+login+senha)
		'realizar verificação de login'

	def cronograma(self, linha = 0, coluna = 0):
		self.refresh()
		self.master.title("Cronograma")
		self.Calendario = Frame(self.master)
		self.Calendario.grid(row=linha, column=coluna)
		Button(self.Calendario, text='Retroceder').grid(row=linha,column=0, columnspan=3, sticky='WE')
		Label(self.Calendario, text='Ano Atual: %i'%self.master.Co.ano_atual()).grid(row=linha,column=3)
		Button(self.Calendario, text='Avançar').grid(row=linha,column=4, columnspan=3, sticky='WE')
		self.meses = Notebook(self.Calendario)
		Janeiro = Frame(self.meses)
		Fevereiro = Frame(self.meses)
		Março = Frame(self.meses)
		Abril = Frame(self.meses)
		Maio = Frame(self.meses)
		Junho = Frame(self.meses)
		Julho = Frame(self.meses)
		Agosto = Frame(self.meses)
		Setembro = Frame(self.meses)
		Outubro = Frame(self.meses)
		Novembro = Frame(self.meses)
		Dezembro = Frame(self.meses)

		self.meses.add(Janeiro, text='Janeiro')
		self.meses.add(Fevereiro, text='Fevereiro')
		self.meses.add(Março, text='Março')
		self.meses.add(Abril, text='Abril')
		self.meses.add(Maio, text='Maio')
		self.meses.add(Junho, text='Junho')
		self.meses.add(Julho, text='Julho')
		self.meses.add(Agosto, text='Agosto')
		self.meses.add(Setembro, text='Setembro')
		self.meses.add(Outubro, text='Outubro')
		self.meses.add(Novembro, text='Novembro')
		self.meses.add(Dezembro, text='Dezembro')
		self.meses.grid(row=linha+1, column=coluna, columnspan=7)
		
		
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 1)
		self.mes(frame=Janeiro, dias=totaldias, dia_da_semana_inicial=dia_inicial)
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 2)
		self.mes(frame=Fevereiro, dias=totaldias, dia_da_semana_inicial=dia_inicial)
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 3)
		self.mes(frame=Março, dias=totaldias, dia_da_semana_inicial=dia_inicial)
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 4)
		self.mes(frame=Abril, dias=totaldias, dia_da_semana_inicial=dia_inicial)
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 5)
		self.mes(frame=Maio, dias=totaldias, dia_da_semana_inicial=dia_inicial)
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 6)
		self.mes(frame=Junho, dias=totaldias, dia_da_semana_inicial=dia_inicial)
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 7) # acontece
		self.mes(frame=Julho, dias=totaldias, dia_da_semana_inicial=dia_inicial)
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 8)	# acontece
		self.mes(frame=Agosto, dias=totaldias, dia_da_semana_inicial=dia_inicial)
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 9)
		self.mes(frame=Setembro, dias=totaldias, dia_da_semana_inicial=dia_inicial)
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 10)
		self.mes(frame=Outubro, dias=totaldias, dia_da_semana_inicial=dia_inicial)
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 11)
		self.mes(frame=Novembro, dias=totaldias, dia_da_semana_inicial=dia_inicial)
		totaldias, dia_inicial = self.master.Co.parametros_mes(mes = 12)
		self.mes(frame=Dezembro, dias=totaldias, dia_da_semana_inicial=dia_inicial)

	def refresh(self):
		for widget in self.master.winfo_children():
			widget.destroy()
		self.start_menu()

	def mes(self, frame = 'frame Pai', nome_do_mês = 'sem nome', dias = 30, dia_da_semana_inicial = 0):
	    diaAtual = dia_da_semana_inicial+1
	    dia = 1
	    #Button(frame, text='♪┏ ( ･o･) ┛♪┗ (･o･ ) ┓♪').grid(row=0, column=0, columnspan=8, sticky='WE')
	    Label(frame, text='Segunda').grid(row=1, column=2)
	    Label(frame, text='Terça').grid(row=1, column=3)
	    Label(frame, text='Quarta').grid(row=1, column=4)
	    Label(frame, text='Quinta').grid(row=1, column=5)
	    Label(frame, text='Sexta').grid(row=1, column=6)
	    Label(frame, text='Sábado').grid(row=1, column=7)
	    Label(frame, text='Domingo').grid(row=1, column=1)

	    if dia_da_semana_inicial < 5: linha_maxima = 26
	    else: linha_maxima = 30

	    for linha in range(2, linha_maxima, 5):
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

	def professor(self):
		self.refresh()
		self.master.title("Professores")
		self.Prof = Frame(self.master).grid()
		Label(self.Prof, text='Cadastro de professores').grid(row=0, column=0, columnspan=2, sticky='WE')
		Label(self.Prof, text='Nome do professor:').grid(row=1, column=0, sticky='WE')
		Nome = StringVar()
		Entry(self.Prof, textvariable=Nome).grid(row=1, column=1, sticky='WE')
		Label(self.Prof, text='Matrícula:').grid(row=2, column=0, sticky='WE')
		Matricula = StringVar()
		Entry(self.Prof, textvariable=Matricula).grid(row=2, column=1, sticky='WE')
		Button(self.Prof, text='Adicionar Professor').grid(row=3, column=0, sticky='WE')
		Button(self.Prof, text='Deletar Professor').grid(row=3, column=1, sticky='WE')
		Label(self.Prof, text='Professores já cadastrados:').grid(row=4, column=0, columnspan=2, sticky='WE')
		linha = 4;
		for professor in self.master.Co.lista_de_professores():
			matp, nomep = professor
			Label(self.Prof, text='Matricula: %i'%matp).grid(row=linha, column=0, sticky='WE')
			Label(self.Prof, text='Professor(a): %s'%nomep).grid(row=linha, column=1, sticky='WE')
			linha+=1

	def turma(self):
		self.refresh()
		self.master.title("Turmas")
		self.Turma = Frame(self.master).grid()
		Label(self.Turma, text='Turma').grid(row=0, column=0)
		Turma = StringVar()
		Entry(self.Turma, textvariable=Turma).grid(row=0, column=1)
		Label(self.Turma, text='Turno').grid(row=1, column=0)
		Turno = StringVar()
		Entry(self.Turma, textvariable=Turno).grid(row=1, column=1)
		Label(self.Turma, text='Turno').grid(row=1, column=0)
		Label(self.Turma, text='Turmas já cadastradas:').grid(row=4, column=0, columnspan=2, sticky='WE')
		linha = 4
		for turma in self.master.Co.lista_de_turmas():
			nomet, turno = turma
			Label(self.Turma, text='Nome: %s'%nomet).grid(row=linha, column=0, sticky='WE')
			Label(self.Turma, text='Turno: %s'%turno).grid(row=linha, column=1, sticky='WE')
			linha+=1		


if __name__ == '__main__':
	JP = Tk()
	JP.grid()
	Visao(JP)
	JP.mainloop()
	exit()