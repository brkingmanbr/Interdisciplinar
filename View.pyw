from tkinter import *
from tkinter.ttk import *
from time import strftime
from PIL import Image, ImageTk
from Control import *

class Visao(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.master.Bd = Banco()
		#self.start_menu()
		#self.start_login()
		#self.homepage()
		#self.disciplina()
		self.admin_home()

	def homepage(self):
		self.master.resizable(False,False)
		self.refresh()
		self.master.title('Homepage - Seja Bem Vindo')
		self.refresh()
		self.Home = Frame(self.master).grid()
		load = Image.open('home.jpg')
		render = ImageTk.PhotoImage(load)
		img = Label(self.Home, image=render)
		img.image = render
		img.grid(row=0, column=0, columnspan=2)
		self.master.resizable(False,False)	

	def start_menu(self):
		self.master.MENU = Frame(self.master)
		self.master.MENU.grid()
		self.BarradeMenu = Menu(self.master.MENU)
		self.master.config(menu=self.BarradeMenu)
		self.editar = Menu(self.BarradeMenu)
		self.BarradeMenu.add_cascade(label="Home", command= self.homepage)
		self.BarradeMenu.add_cascade(label="Editar", menu=self.editar)
		self.editar.add_command(label="Editar Professores", command=self.professor)
		self.editar.add_command(label="Editar Turmas", command=self.turma)
		self.editar.add_command(label="Editar Disciplinas", command=self.disciplina)
		self.login = Menu(self.BarradeMenu)
		self.BarradeMenu.add_cascade(label="Login", menu=self.login)
		self.cronograma_menu = Menu(self.BarradeMenu)		
		self.BarradeMenu.add_cascade(label="Gerenciar Cronogramas", menu=self.cronograma_menu)
		self.cronograma_menu.add_command(label="Atribuir Aulas", command=self.gerenciador_de_cronograma)
		self.cronograma_menu.add_command(label="Cronograma de Professor", command=self.cronoprofessor)
		self.cronograma_menu.add_command(label="Cronograma de Turma", command=self.cronoturma)

	def start_login(self):
		self.master.title("Tela de Login")
		self.grid()
		load = Image.open('aang.png')
		render = ImageTk.PhotoImage(load)
		img = Label(self, image=render)
		img.image = render
		img.grid(row=0, column=0, columnspan=2)

		UsuarioL = Label(self, text='Username: ', anchor='w').grid(row=1, column=0, sticky='we')
		self.user = StringVar()
		UsuarioE = Entry(self, textvariable = self.user).grid(row=1, column=1, sticky='we')
		SenhaL = Label(self, text='Password: ', anchor='w').grid(row=2, column=0, sticky='we')
		self.senha = StringVar()
		SenhaE = Entry(self, textvariable = self.senha, show='*').grid(row=2, column=1, sticky='we')
		Login = Button(self, text='Login', command= self.verifica_login).grid(row=3, columnspan=2, sticky='we')
		self.master.title("Tela de Login")
		self.master.resizable(False,False)

	def verifica_login(self):
		if self.master.Bd.verifica_login(self.user.get(), self.senha.get()) == True:
			self.homepage()
		elif self.master.Bd.verifica_login(self.user.get(), self.senha.get()) == False:
			self.master.title("Senha ou Login incorretos tente novamente")
		elif self.master.Bd.verifica_login(self.user.get(), self.senha.get()) == 'admin':
			self.admin_home()

	def admin_menu(self):
		self.master.MENU = Frame(self.master)
		self.master.MENU.grid()
		self.BarradeMenu = Menu(self.master.MENU)
		self.master.config(menu=self.BarradeMenu)
		self.editar = Menu(self.BarradeMenu)
		self.BarradeMenu.add_cascade(label=" Gerenciar Coordenadores", command=self.admin_coordenador)
		self.BarradeMenu.add_cascade(label=" Banco de Dados", command=self.admin_resetar_banco)
		self.master.title("Voce está no modo Administrador tenha Cuidado!!")
	def admin_home(self):
		self.admin_refresh()
		self.Admin_Home = Frame(self.master)
		self.Admin_Home.grid()
		load = Image.open('admin.png')
		render = ImageTk.PhotoImage(load)
		img = Label(self.Admin_Home, image=render)
		img.image = render
		img.grid(row=0, column=0, columnspan=2)
		# Label(self.Administrador, text='TODAS AS OPERAÇÕES ABAIXO SERÃO EXECUTADAS NO COORDENADOR SELECIONADO').grid(row=0, column=0, columnspan=4)
		# Label(self.Administrador, text='Coordenador: ').grid(row=1, column=0)
		# Button(self.Administrador, text='Alterar Nome Para').grid(row=2, column=0)
		# self.NomeNovo = StringVar()
		# Entry(self.Administrador, textvariable= self.NomeNovo).grid(row=2, column=1)
		# Button(self.Administrador, text='Resetar Senha').grid(row=3,column=0)

	def admin_refresh(self):
		for widget in self.master.winfo_children():
			widget.destroy()
		self.admin_menu()

	def admin_resetar_banco(self):
		self.admin_refresh()
		self.Resetar = Frame(self.master)
		self.Resetar.grid()
		Label(self.Resetar, text='Senha Admin: ').grid(row=0,column=0, sticky='WE')
		self.SenhaAdmin = StringVar()
		Entry(self.Resetar, textvariable=self.SenhaAdmin).grid(row=0,column=1, sticky='WE')
		Button(self.Resetar, text='Resetar Todo o Banco de Dados').grid(row=1,column=0, columnspan=2, sticky='WE')
		
	def admin_coordenador(self):
		self.admin_refresh()
		self.AdicionaDeletaCoordenador = Frame(self.master)
		self.AdicionaDeletaCoordenador.grid()
		Label(self.AdicionaDeletaCoordenador, text ='Nome: ').grid(row=0,column=0,sticky='we')
		self.NomeCoordenador = StringVar()
		self.LoginCoordenador = StringVar()
		Entry(self.AdicionaDeletaCoordenador, textvariable= self.NomeCoordenador).grid(row=0,column=1,sticky='we')
		Label(self.AdicionaDeletaCoordenador, text = 'Login').grid(row=1,column=0,sticky='we')
		Entry(self.AdicionaDeletaCoordenador, textvariable= self.LoginCoordenador).grid(row=1,column=1,sticky='we')
		Button(self.AdicionaDeletaCoordenador, text = 'Adicionar', command = lambda: [self.master.Bd.adicionar_coordenador(nome = self.NomeCoordenador.get(), login=self.LoginCoordenador.get()), self.admin_coordenador()]).grid(row=2,column=0, columnspan=2 ,sticky='we')		
		Label(self.AdicionaDeletaCoordenador, text='Selecione um coordenador').grid(row=3,column=0, columnspan=2, sticky='we')
		self.Coordenador = StringVar()
		Combobox(self.AdicionaDeletaCoordenador, textvariable=self.Coordenador, state='readonly', values= self.master.Bd.nomes_coordenadores()).grid(row=4, column=0, columnspan = 2, sticky='we')
		Button(self.AdicionaDeletaCoordenador, text='Resetar Senha do coordenador', command=lambda:[self.master.Bd.resetar_senha_coordenador(nome = self.Coordenador.get()), self.admin_coordenador()]).grid(row=5,column=0, columnspan=1,sticky='we')
		Label(self.AdicionaDeletaCoordenador, textvariable=self.Coordenador).grid(row=5,column=1, columnspan=1,sticky='we')
		Button(self.AdicionaDeletaCoordenador, text = 'Remover', command = lambda: self.master.Bd.remover_coordenador(nome = self.NomeCoordenador.get())).grid(row=7,column=0, sticky='we')

	def cronoprofessor(self):
		self.refresh()
		self.master.title("Cronograma de Professor")
		self.ParamCronograma = Frame(self.master)
		self.ParamCronograma.grid()
		Label(self.ParamCronograma, text='Professores: ').grid(row=1, column=0)
		self.Professor = StringVar()
		Combobox(self.ParamCronograma, textvariable=self.Professor, state='readonly', values= self.master.Bd.nomes_professores()).grid(row=1, column=1)
		Button(self.ParamCronograma, text='Gerar Cronograma', command = lambda: self.cronograma(tipo='Professor', professor_ou_turma=self.Professor.get())).grid(row=1, column=3)

	def cronoturma(self):
		self.refresh()
		self.master.title("Cronograma de Turma")
		self.master.ParamCronograma = Frame(self.master)
		self.master.ParamCronograma.grid()
		Label(self.master.ParamCronograma, text='Turmas: ').grid(row=1, column=0)
		self.master.TurmaSelecionada = StringVar()
		Combobox(self.master.ParamCronograma, textvariable=self.master.TurmaSelecionada, state='readonly', values= self.master.Bd.nomes_turmas()).grid(row=1, column=1)
		Button(self.master.ParamCronograma, text='Gerar Cronograma', command= lambda: self.cronograma(tipo='Turma', professor_ou_turma=self.master.TurmaSelecionada.get())).grid(row=1, column=3)
	
	def gerenciador_de_cronograma(self):
		self.refresh()
		self.master.title("Gerenciador de Cronogramas")
		self.Gerenciador = Frame(self.master)
		self.Gerenciador.grid(row=0)
		Label(self.Gerenciador, text='Professor: ').grid(row=0, column=0)
		self.Professor = StringVar()
		Combobox(self.Gerenciador, textvariable=self.Professor, state='readonly', values= self.master.Bd.nomes_professores()).grid(row=0, column=1)
		Label(self.Gerenciador, text='Lecionara na Turma: ').grid(row=1, column=0)
		self.Turma = StringVar()
		Combobox(self.Gerenciador, textvariable=self.Turma, state='readonly', values= self.master.Bd.nomes_turmas()).grid(row=1, column=1)
		Label(self.Gerenciador, text='Apartir de: ').grid(row=2, column=0)
		self.diaInicial = StringVar()
		self.mesInicial = StringVar()
		self.anoInicial = StringVar()
		dias = ('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
		meses = ('01','02','03','04','05','06','07','08','09','10','11','12')
		anos = ('2016','2017','2018')
		Combobox(self.Gerenciador, textvariable=self.diaInicial, state='readonly', values=dias).grid(row=2, column=1)
		Combobox(self.Gerenciador, textvariable=self.mesInicial, state='readonly', values=meses).grid(row=2, column=2)
		Combobox(self.Gerenciador, textvariable=self.anoInicial, state='readonly', values=anos).grid(row=2, column=3)
		self.diaFinal = StringVar()
		self.mesFinal = StringVar()
		self.anoFinal = StringVar()
		Label(self.Gerenciador, text=' até ').grid(row=3, column=0)
		Combobox(self.Gerenciador, textvariable=self.diaFinal, state='readonly', values=dias).grid(row=3, column=1)
		Combobox(self.Gerenciador, textvariable=self.mesFinal, state='readonly', values=meses).grid(row=3, column=2)
		Combobox(self.Gerenciador, textvariable=self.anoFinal, state='readonly', values=anos).grid(row=3, column=3)
		self.GerenciadorCalendario = Frame(self.master)
		self.GerenciadorCalendario.grid(row=10, columnspan=100)
		Label(self.GerenciadorCalendario, text='Nos seguintes horários: ').grid(row=4, column=0, columnspan=100)
		Dias_da_semana = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado')
		self.v = IntVar()
		self.master.Semana = [[],[],[],[],[],[]]
		for dia in self.master.Semana: 
			for x in range(0,12): 
				x = IntVar()
				dia.append(x)
		y = 0
		for dias in range(0,12,2):
			Label(self.GerenciadorCalendario, text=Dias_da_semana[y]+str(dias), anchor='center').grid(row=5, column=dias, columnspan=2, sticky= 'WE')
			y+=1
		dia = 0
		hora = 0
		for h in range(0,12,2):
			for l in range(0,12):
				Checkbutton(self.GerenciadorCalendario, text = h, onvalue = 1, variable=self.master.Semana[dia][hora]).grid(row=l+6, column=h, sticky= 'WE')
				Label(self.GerenciadorCalendario, text = self.master.Bd.horarios()[l]).grid(row=l+6, column=h+1, sticky= 'WE')
				hora+=1
			dia+=1
			hora=0
		Button(self.GerenciadorCalendario, text='Marcar Aulas', command= lambda: self.master.Bd.atribuir_aulas(lista_de_checkbox=self.semana_em_inteiros(), professor=self.Professor.get(), turma= self.Turma.get(), ano_inicio= self.anoInicial.get(), mes_inicio=self.mesInicial.get(), dia_inicio=self.diaInicial.get(), ano_final=self.anoFinal.get(), mes_final=self.mesFinal.get(), dia_final=self.diaFinal.get())).grid(row=18, column=0, columnspan=100, sticky= 'WE')
		Button(self.GerenciadorCalendario, text='Apagar Aulas').grid(row=19, column=0, columnspan=100, sticky= 'WE')
		
	def semana_em_inteiros(self):
		lista_de_inteiros = [[],[],[],[],[],[]]
		for dia in range(0, len(self.master.Semana)):
			for x in range(0,12): 
				lista_de_inteiros[dia].append(self.master.Semana[dia][x].get())
		return lista_de_inteiros

	def cronograma(self, linha = 0, coluna = 0, tipo='', professor_ou_turma=''):
		ano = self.master.Bd.ano_atual()
		self.refresh()	
		self.master.title("Cronograma "+professor_ou_turma)
		self.Calendario = Frame(self.master)
		self.Calendario.grid(row=linha, column=coluna)
		Button(self.Calendario, text='Retroceder').grid(row=linha,column=0, columnspan=3, sticky='WE')
		Label(self.Calendario, text='Ano Atual: %i'%self.master.Bd.ano_atual()).grid(row=linha,column=3)
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
		
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 1)
		self.mes(frame=Janeiro, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes = '01', tipo=tipo, professor_turma=professor_ou_turma)
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 2)
		self.mes(frame=Fevereiro, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes ='02', tipo=tipo, professor_turma=professor_ou_turma)
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 3)
		self.mes(frame=Março, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes ='03', tipo=tipo, professor_turma=professor_ou_turma)
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 4)
		self.mes(frame=Abril, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes ='04', tipo=tipo, professor_turma=professor_ou_turma)
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 5)
		self.mes(frame=Maio, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes ='05', tipo=tipo, professor_turma=professor_ou_turma)
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 6)
		self.mes(frame=Junho, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes ='06', tipo=tipo, professor_turma=professor_ou_turma)
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 7)
		self.mes(frame=Julho, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes ='07', tipo=tipo, professor_turma=professor_ou_turma)
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 8)
		self.mes(frame=Agosto, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes ='08', tipo=tipo, professor_turma=professor_ou_turma)
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 9)
		self.mes(frame=Setembro, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes ='09', tipo=tipo, professor_turma=professor_ou_turma)
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 10)
		self.mes(frame=Outubro, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes ='10', tipo=tipo, professor_turma=professor_ou_turma)
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 11)
		self.mes(frame=Novembro, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes ='11', tipo=tipo, professor_turma=professor_ou_turma)
		totaldias, dia_inicial = self.master.Bd.parametros_mes(ano = ano, mes = 12)
		self.mes(frame=Dezembro, dias=totaldias, dia_da_semana_inicial=dia_inicial,numero_do_mes ='12', tipo=tipo, professor_turma=professor_ou_turma)

	def refresh(self):
		for widget in self.master.winfo_children():
			widget.destroy()
		self.start_menu()

	def mes(self, frame = 'frame Pai', nome_do_mês = 'sem nome',ano = '2016', dias = 30, dia_da_semana_inicial = 0, numero_do_mes = '06', tipo='', professor_turma=''):
		diaAtual = dia_da_semana_inicial+1
		dia = 1
		self.Turnos = Notebook(frame)
		Matutino = Frame(self.Turnos)
		Vespertino = Frame(self.Turnos)
		Noturno = Frame(self.Turnos)
		self.Turnos.add(Matutino, text='Matutino')
		self.Turnos.add(Vespertino, text='Vespertino')
		self.Turnos.add(Noturno, text='Noturno')
		Lista_Turnos = [Matutino, Vespertino, Noturno]
		self.Turnos.grid()

		horarios = self.master.Bd.horarios()
		lista_de_horarios = [[],[],[]]
		for num in range(0,4):
			lista_de_horarios[0].append(horarios[num])
			lista_de_horarios[1].append(horarios[num+4])
			lista_de_horarios[2].append(horarios[num+8])
		
		ele_in_horario = 0
		turnoooooooooo = ['turno1','turno2','turno3']

		for turno in Lista_Turnos:
			#Button(frame, text='♪┏ ( ･o･) ┛♪┗ (･o･ ) ┓♪').grid(row=0, column=0, columnspan=8, sticky='WE')
			Label(turno, text='Segunda').grid(row=1, column=2)
			Label(turno, text='Terça').grid(row=1, column=3)
			Label(turno, text='Quarta').grid(row=1, column=4)
			Label(turno, text='Quinta').grid(row=1, column=5)
			Label(turno, text='Sexta').grid(row=1, column=6)
			Label(turno, text='Sábado').grid(row=1, column=7)
			Label(turno, text='Domingo').grid(row=1, column=1)
			#print('asdadad')
			if dia_da_semana_inicial < 5: linha_maxima = 26
			else: linha_maxima = 30

			for linha in range(2, linha_maxima, 5):
				print(lista_de_horarios[ele_in_horario])
				if diaAtual <= dias:
					Label(turno, text=lista_de_horarios[ele_in_horario][0]).grid(row=linha+1, column=0, sticky='NSWE')
					Label(turno, text=lista_de_horarios[ele_in_horario][1]).grid(row=linha+2, column=0, sticky='NSWE')
					Label(turno, text=lista_de_horarios[ele_in_horario][2]).grid(row=linha+3, column=0, sticky='NSWE')
					Label(turno, text=lista_de_horarios[ele_in_horario][3]).grid(row=linha+4, column=0, sticky='NSWE')
					for coluna in range(diaAtual, 8):
						if dia <= dias:
							diaa = dia
							if diaa < 10: diaa = '0'+str(diaa)
							Button(turno, text='Dia: %i'%dia).grid(row=linha, column=coluna, sticky='NSWE')
							Button(turno, text=self.master.Bd.pesquisa_cronograma(ano = ano, mes = numero_do_mes, dia = diaa, horario = lista_de_horarios[ele_in_horario][0], tipo=tipo, professor_turma= professor_turma)).grid(row=linha+1, column=coluna, sticky='NSWE')
							Button(turno, text=self.master.Bd.pesquisa_cronograma(ano = ano, mes = numero_do_mes, dia = diaa, horario = lista_de_horarios[ele_in_horario][1], tipo=tipo, professor_turma= professor_turma)).grid(row=linha+2, column=coluna, sticky='NSWE')
							Button(turno, text=self.master.Bd.pesquisa_cronograma(ano = ano, mes = numero_do_mes, dia = diaa, horario = lista_de_horarios[ele_in_horario][2], tipo=tipo, professor_turma= professor_turma)).grid(row=linha+3, column=coluna, sticky='NSWE')
							Button(turno, text=self.master.Bd.pesquisa_cronograma(ano = ano, mes = numero_do_mes, dia = diaa, horario = lista_de_horarios[ele_in_horario][3], tipo=tipo, professor_turma= professor_turma)).grid(row=linha+4, column=coluna, sticky='NSWE')
							dia += 1
					diaAtual = 1
			diaAtual = dia_da_semana_inicial+1
			ele_in_horario += 1
			dia = 1

	def professor(self):
		self.refresh()
		self.master.title("Professores")
		self.Prof = Frame(self.master).grid()
		Label(self.Prof, text='Cadastro de professores', anchor='center').grid(row=0, column=0, columnspan=5, sticky='WE')
		Label(self.Prof, text='Nome do professor:').grid(row=1, column=0, sticky='WE')
		self.Nome = StringVar()
		Entry(self.Prof, textvariable=self.Nome).grid(row=1, column=1, columnspan=4, sticky='WE')

		Label(self.Prof, text='Matrícula:').grid(row=2, column=0, sticky='WE')
		self.Matricula = StringVar()
		Entry(self.Prof, textvariable=self.Matricula).grid(row=2, column=1, columnspan=4,  sticky='WE')
		
		Label(self.Prof, text='Disciplina:').grid(row=3, column=0, sticky='WE')
		self.Disciplina = StringVar()
		Combobox(self.Prof, textvariable=self.Disciplina, state='readonly', values= self.master.Bd.lista_disciplinas()).grid(row=3, column=1,  columnspan=4, sticky='WE')
		
		Label(self.Prof, text='Carga Horária:').grid(row=4, column=0, sticky='WE')
		self.CargaHoraria = StringVar()
		Entry(self.Prof, textvariable=self.CargaHoraria).grid(row=4, column=1, columnspan=4,  sticky='WE')

		Button(self.Prof, text='Adicionar Professor', command= lambda: [self.master.Bd.adicionar_professor(matricula = int(self.Matricula.get()),nome_prof = self.Nome.get(),disciplina = self.Disciplina.get(),carga_horaria = int(self.CargaHoraria.get())), self.refresh(), self.professor()]).grid(row=5, column=0, sticky='WE')
		Button(self.Prof, text='Deletar Professor', command= lambda: [self.master.Bd.remover_professor(nome_prof = self.Nome.get(), disciplina = self.Disciplina.get()), self.refresh(), self.professor()]).grid(row=5, column=1, sticky='WE')
		Label(self.Prof, text='Professores já cadastrados:', anchor='center').grid(row=6, column=0, columnspan=5, sticky='WE')
		
		campos = ['Matricula', 'Nome', 'Disciplina', 'Carga Horaria', 'Quantidade Dias']
		for ele in range(0,5):
			Label(self.Prof, text=campos[ele]).grid(row=7, column=ele, sticky='WE')
		linha = 8;
		for professor in self.master.Bd.lista_de_professores():
			coluna=0
			for ele in professor:
				Label(self.Prof, text=ele).grid(row=linha, column=coluna, sticky='WE')
				coluna+=1
			linha+=1
			coluna=0

	def disciplina(self):
		self.refresh()
		self.master.title("Disciplinas")
		self.Disciplinas = Frame(self.master).grid()
		Label(self.Disciplinas, text='Nome da Disciplina', anchor='center').grid(row=0, column=0, sticky='WE')
		self.Nome_Disciplina = StringVar()
		Entry(self.Disciplinas, textvariable=self.Nome_Disciplina).grid(row=0, column=1, sticky='WE')
		Button(self.Disciplinas, text='Cadastrar',command=lambda:[self.master.Bd.adicionar_disciplina(nome_disciplina = self.Nome_Disciplina.get()), self.refresh(), self.disciplina()]).grid(row=1, column=0, sticky='WE')
		Button(self.Disciplinas, text='Deletar',command=lambda:[self.master.Bd.remover_disciplina(nome_disciplina = self.Nome_Disciplina.get()), self.refresh(), self.disciplina()]).grid(row=1, column=1, sticky='WE')
		Label(self.Disciplinas, text='Disciplinas já cadastradas', anchor='center').grid(row=2, column=0, columnspan=2, sticky='WE')
		linha = 3
		for ele in self.master.Bd.lista_disciplinas():
			Label(self.Disciplinas, text=ele).grid(row=linha, column=0, columnspan=2, sticky='WE')
			linha+=1

	def turma(self):
		self.refresh()
		self.master.title("Turmas")
		self.Turma = Frame(self.master).grid()
		Label(self.Turma, text='Turma').grid(row=0, column=0, sticky='WE')
		self.Nome = StringVar()
		Entry(self.Turma, textvariable=self.Nome).grid(row=0, column=1, sticky='WE')
		Label(self.Turma, text='Turno').grid(row=1, column=0, sticky='WE')
		self.Turno = StringVar()
		Combobox(self.Turma, textvariable=self.Turno, state='readonly', values= self.master.Bd.lista_de_turnos()).grid(row=1, column=1, sticky='WE')
		Button(self.Turma, text='Adicionar Turma', command= lambda: [self.master.Bd.adicionar_turma(nome_turma = self.Nome.get(), turno = self.Turno.get()), self.refresh(), self.turma()]).grid(row=5, column=0, sticky='WE')
		Button(self.Turma, text='Deletar Turma', command= lambda: [self.master.Bd.remover_turma(nome_turma = self.Nome.get(), turno = self.Turno.get()), self.refresh(), self.turma()]).grid(row=5, column=1, sticky='WE')
		Label(self.Turma, text='Turmas já cadastradas:', anchor='center').grid(row=6, column=0, columnspan=2, sticky='WE')
		Label(self.Turma, text='Nome', anchor='center').grid(row=7, column=0, sticky='WE')
		Label(self.Turma, text='Turno', anchor='center').grid(row=7, column=1, sticky='WE')
		linha = 8
		for turma in self.master.Bd.lista_de_turmas():
			nome, turno = turma
			Label(self.Turma, text=nome, anchor='center').grid(row=linha, column=0, sticky='WE')
			Label(self.Turma, text=turno, anchor='center').grid(row=linha, column=1, sticky='WE')
			linha+=1

if __name__ == '__main__':
	JP = Tk()
	JP.grid()
	Visao(JP)
	JP.mainloop()
	exit()