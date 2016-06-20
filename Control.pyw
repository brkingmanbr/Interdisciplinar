import pymysql as bd

class Banco():
	def __init__(self):
	    self.parametros = {'user':'root',#user.get(),
	                  'host':'localhost',#host.get(),
	                  'passwd':'40028922',#senha.get(),
	                  'autocommit':True}
	    self.banco = bd.connect(**self.parametros)
	    self.c = self.banco.cursor()
	    self.cria_banco()
	def cria_banco(self):
	    self.c.execute('''
	    	CREATE DATABASE IF NOT EXISTS SIS;
	    	USE SIS;
	    	CREATE TABLE IF NOT EXISTS Turno (
	    		turno VARCHAR(30) PRIMARY KEY
	    	);
	    	CREATE TABLE IF NOT EXISTS Disciplina (
	    	    nome VARCHAR(40) PRIMARY KEY
	    	);
	    	CREATE TABLE IF NOT EXISTS Professor (
		        id_prof INT AUTO_INCREMENT PRIMARY KEY,
		        matricula INT,
		        nome_prof VARCHAR(40),
		        disciplina VARCHAR(40),
		        carga_horaria INT,
		        quantidade_dias INT,
		        FOREIGN KEY (disciplina)
		            REFERENCES Disciplina (nome)
		    );
	    	CREATE TABLE IF NOT EXISTS Horario (
	    	    horario VARCHAR(13) PRIMARY KEY,
	    	    turno VARCHAR(30),
	    	    FOREIGN KEY (turno)
	    	        REFERENCES Turno (turno)
	    	);
	    	CREATE TABLE IF NOT EXISTS Turma (
	    	    nome_turma VARCHAR(10) PRIMARY KEY,
	    	    turno VARCHAR(30),
	    	    FOREIGN KEY (turno)
	    	        REFERENCES Turno (turno)
	    	);
	    	CREATE TABLE IF NOT EXISTS Coordenador (
	    	    id INT AUTO_INCREMENT PRIMARY KEY,
	    	    nome VARCHAR(40),
	    	    login VARCHAR(30),
	    	    senha VARCHAR(30)
	    	);
	    	CREATE TABLE IF NOT EXISTS Cronograma (
	    	    id_professor INT,
	    	    data_reserva DATE,
	    	    horario VARCHAR(13),
	    	    turma VARCHAR(30),
	    	    id_coordenador INT,
	    	    FOREIGN KEY (id_professor)
	    	        REFERENCES professor (id_prof),
	    	    FOREIGN KEY (horario)
	    	        REFERENCES Horario (horario),
	    	    FOREIGN KEY (turma)
	    	        REFERENCES Turma (nome_turma),
	    	    FOREIGN KEY (id_coordenador)
	    	        REFERENCES Coordenador (id)
	    	);
	    	''')
	    turnos = ['Matutino', 'Vespertino', 'Noturno', 'Matutino/Vespertino', 'Matutino/Noturno','Vespertino/Noturno']
	    for ele in turnos:
	    	self.c.execute("INSERT INTO Turno SELECT '%s' AS x WHERE NOT EXISTS (SELECT * FROM Turno WHERE turno = '%s') LIMIT 1;"%(ele, ele))
	    horarios = [
	    '07:30 - 08:30', '08:30 - 09:30', '09:30 - 10:30', '10:30 - 11:30',
	    '13:00 - 14:00', '14:00 - 15:00', '15:00 - 16:00', '16:00 - 17:00',
	    '18:00 - 19:00', '19:00 - 20:00', '20:00 - 21:00', '21:00 - 22:00']
	    for ind in range(0, 4):
	    	self.c.execute("INSERT INTO Horario SELECT '%s', '%s' AS x WHERE NOT EXISTS (SELECT * FROM Horario WHERE horario = '%s') LIMIT 1;"%(horarios[ind], turnos[0], horarios[ind]))
	    	self.c.execute("INSERT INTO Horario SELECT '%s', '%s' AS x WHERE NOT EXISTS (SELECT * FROM Horario WHERE horario = '%s') LIMIT 1;"%(horarios[ind+4], turnos[1], horarios[ind+4]))
	    	self.c.execute("INSERT INTO Horario SELECT '%s', '%s' AS x WHERE NOT EXISTS (SELECT * FROM Horario WHERE horario = '%s') LIMIT 1;"%(horarios[ind+8], turnos[2], horarios[ind+8]))

	def resetar_banco(self, senha):
		if senha == 'cimatec':
			self.c.execute("DROP DATABASE SIS;")
			self.cria_banco()

	def primeiro_dia_do_mes(self, mes, ano = '2016', dia = '1'):
	    self.c.execute('''
	    	SELECT WEEKDAY('%s-%s-%s');
	    	'''%(ano, mes, dia))
	    return self.c.fetchone()[0]

	def quant_dias_do_mes(self, mes, ano = '2016', dia = '1'):
	    self.c.execute("SELECT LAST_DAY('%s-%s-%s');"%(ano, mes, dia))
	    data = str(self.c.fetchone()[0])
	    data = int(data[len(data)-2:])
	    return data
	def parametros_mes(self, mes, ano):
		return self.quant_dias_do_mes(mes = mes), self.primeiro_dia_do_mes(mes = mes, ano = ano)

	def ano_atual(self):
		self.c.execute('SELECT YEAR(NOW());')
		ano = int(self.c.fetchone()[0])
		return ano
	def lista_de_professores(self):
		self.c.execute('SELECT matricula, nome_prof, disciplina, carga_horaria, quantidade_dias FROM Professor ORDER BY matricula;')
		profesores = self.c.fetchall()
		return profesores
	

	def lista_de_turmas(self):
		self.c.execute('SELECT nome_turma, turno FROM Turma ORDER BY nome_turma;')
		turmas = self.c.fetchall()
		return turmas
	def adicionar_turma(self, nome_turma, turno):
		self.c.execute("INSERT INTO Turma(nome_turma, turno) SELECT '%s','%s' AS x WHERE NOT EXISTS (SELECT * FROM Turma WHERE nome_turma = '%s' AND turno = '%s') LIMIT 1;"%(nome_turma, turno, nome_turma, turno))
	def remover_turma(self, nome_turma, turno):
		self.c.execute("DELETE FROM Turma WHERE nome_turma = '%s' AND turno = '%s';"%(nome_turma, turno))
	def lista_de_turnos(self):
		self.c.execute('SELECT *FROM Turno ORDER BY turno;')
		turnos = self.c.fetchall()
		lista_turnos = []
		for ele in turnos:
			lista_turnos.append(ele[0])
		return lista_turnos
	def adicionar_disciplina(self, nome_disciplina):
		self.c.execute("INSERT INTO Disciplina(nome) SELECT '%s' AS x WHERE NOT EXISTS (SELECT * FROM Disciplina WHERE nome = '%s') LIMIT 1;"%(nome_disciplina, nome_disciplina))
	def remover_disciplina(self, nome_disciplina):
		self.c.execute("DELETE FROM Disciplina WHERE nome = '%s';"%(nome_disciplina))
	def lista_disciplinas(self):
		self.c.execute("SELECT * FROM Disciplina")
		lista_de_disciplinas =  []
		for ele in self.c.fetchall():
			lista_de_disciplinas.append(ele[0])
		return lista_de_disciplinas
	
	def adicionar_coordenador(self, nome, login):		
		self.c.execute("INSERT INTO Coordenador(nome, login, senha) SELECT '%s', '%s', '123456' AS x WHERE NOT EXISTS (SELECT * FROM Coordenador WHERE nome = '%s' OR login = '%s') LIMIT 1;"%(nome, login, nome, login))
	def id_coordenador(self, usuario):
		self.c.execute("SELECT id FROM Coordenador WHERE login = '%s';"%usuario)
		return self.c.fetchone()[0]
	def remover_coordenador(self, nome):
		self.c.execute("DELETE FROM Coordenador WHERE nome = '%s';"%(nome))
	def resetar_senha_coordenador(self, nome):
		self.c.execute("UPDATE Coordenador SET senha = '123456' WHERE nome = '%s';"%nome)

	def alterar_senha_coordenador(self, id_coord, senha_velha, senha_nova):
		self.c.execute("UPDATE Coordenador SET senha = '%s' WHERE id = '%i' AND senha = '%s';"%(senha_nova, id_coord, senha_velha))

	def nome_coordenador(self, id):
		self.c.execute('SELECT nome FROM Coordenador WHERE id = %i;'%id)
		return self.c.fetchone()[0]
	def nomes_coordenadores(self):
		self.c.execute('SELECT nome FROM Coordenador ORDER BY nome;')
		coordenadores = self.c.fetchall()
		lista_de_coordenadores = []
		for ele in coordenadores:
			lista_de_coordenadores.append(ele[0])
		return lista_de_coordenadores

	def verifica_login(self, login, senha):
		if login == 'admin' and senha == 'cimatec':
			return 'admin'
		else:
			self.c.execute("SELECT senha FROM Coordenador where login = '%s';"%login)
			Senha = self.c.fetchone()[0]
			if senha == Senha:
				return True
			else:
				return False
	def adicionar_professor(self, matricula, nome_prof, disciplina, carga_horaria):
		self.c.execute("INSERT INTO Professor(matricula, nome_prof, disciplina, carga_horaria, quantidade_dias) SELECT %i ,'%s','%s', %i, %i AS x WHERE NOT EXISTS (SELECT * FROM Professor WHERE  matricula = %i AND nome_prof = '%s' AND disciplina = '%s') LIMIT 1;"%(matricula, nome_prof, disciplina, carga_horaria, carga_horaria/4, matricula, nome_prof, disciplina))
	def remover_professor(self, nome_prof, disciplina):
		self.c.execute("DELETE FROM Professor WHERE  nome_prof = '%s' AND disciplina = '%s';"%(nome_prof, disciplina))
	def nomes_professores(self):
		self.c.execute("SELECT nome_prof FROM Professor ORDER BY (nome_prof);")
		professores = []
		for ele in self.c.fetchall():
			professores.append(ele[0])
		return professores	
	def nomes_turmas(self):
		self.c.execute("SELECT nome_turma FROM Turma;")
		turmas = []
		for ele in self.c.fetchall():
			turmas.append(ele[0])
		return turmas

	def pesquisa_cronograma(self, ano, mes, dia, horario, tipo, professor_turma, id_coord):
		if tipo == 'Professor':
			self.c.execute("SELECT id_prof FROM Professor where nome_prof = '%s';"%professor_turma)
			id_professor = self.c.fetchone()[0]
			self.c.execute("select turma from Cronograma where data_reserva = '%s%s%s' and horario = '%s' and id_professor = '%i' AND id_coordenador = %i;"%(str(ano), mes, str(dia), horario, id_professor, id_coord))
			turma = self.c.fetchone()
			if turma == None:
				return horario
			else:
				return turma[0]
		elif tipo == 'Turma':
			self.c.execute("select id_professor from Cronograma where data_reserva = '%s%s%s' and horario = '%s' and turma = '%s' AND id_coordenador = %i;"%(str(ano), mes, str(dia), horario, professor_turma, id_coord))
			id_professor = self.c.fetchone()
			if id_professor == None:
				return horario
			else:
				self.c.execute("SELECT nome_prof FROM Professor where id_prof = %i;"%id_professor[0])
				return  self.c.fetchone()[0]

	def horarios(self):
		self.c.execute("select horario from Horario order by(horario)")
		lista_de_horarios = []
		for h in self.c.fetchall():
			lista_de_horarios.append(h[0])
		return lista_de_horarios

	def atribuir_aulas(self, horarios_das_aulas, professor, turma, ano_inicio, mes_inicio, dia_inicio, ano_final, mes_final, dia_final, id_coord):
		executar = True
		
		if int(ano_final) < int(ano_inicio):
			executar = False
		elif int(ano_final) == int(ano_inicio):
			if int(mes_final) < int(mes_inicio):
				executar = False
			elif int(mes_final) == int(mes_inicio):
					if int(dia_final) < int (dia_inicio): 
						executar = False

		if executar == True:
			self.c.execute("SELECT id_prof FROM Professor WHERE nome_prof = '%s';"%professor)
			id_professor = self.c.fetchone()[0]
			
			self.c.execute("SELECT horario FROM Horario ORDER BY (horario);")
			resultado = self.c.fetchall()
			horarios = []
			for ele in resultado:
				horarios.append(ele[0])
			
			horarios_das_aulas.insert(0,[0,0,0,0,0,0,0,0,0,0,0,0])

			dias_da_semana = []
			for dia in horarios_das_aulas:
				if 1 in dia:
					dias_da_semana.append(True)
				else:
					dias_da_semana.append(False)

			for ano in range(int(ano_inicio),int(ano_final)+1):
				
				if int(ano_inicio) == int(ano_final):
					
					for mes in range(int(mes_inicio), int(mes_final)+1):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						ultimo_dia = int(str(self.c.fetchone()[0])[8:])
						if mes == int(mes_final):
							ultimo_dia = int(dia_final)
						for dia in range(1, ultimo_dia+1):
							if mes <= int(mes_final):
								if dia < 10 and mes <10: 
									self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
								elif mes < 10:
									self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
								elif dia < 10:
									self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
								else:
									self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
								dia_da_semana = self.c.fetchone()[0]
								if dia_da_semana != None and dia_da_semana <= 7:
									if dias_da_semana[dia_da_semana-1]:
										for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
											if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
												if dia < 10 and mes <10:
													self.c.execute('''
														INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s0%s0%s', '%s', '%s', %i AS x 
														WHERE NOT EXISTS (SELECT * FROM Cronograma
														WHERE (id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
												elif mes < 10:
													self.c.execute('''
														INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s0%s%s', '%s', '%s', %i AS x 
														WHERE NOT EXISTS (SELECT * FROM Cronograma
														WHERE (id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
												elif dia < 10:
													self.c.execute('''
														INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s%s0%s', '%s', '%s', %i AS x 
														WHERE NOT EXISTS (SELECT * FROM Cronograma
														WHERE (id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
												else:
													self.c.execute('''
														INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s%s%s', '%s', '%s', %i AS x 
														WHERE NOT EXISTS (SELECT * FROM Cronograma
														WHERE (id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
				elif ano == int(ano_inicio):
					
					for mes in range(int(mes_inicio), 13):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						for dia in range(1, int(str(self.c.fetchone()[0])[8:])+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s0%s0%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s0%s0%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif mes < 10:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s0%s%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif dia < 10:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s%s0%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											else:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s%s%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))										
				elif ano >int(ano_inicio) and ano < int(ano_final):
					
					for mes in range(1, 13):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						for dia in range(1, int(str(self.c.fetchone()[0])[8:])+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s0%s0%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif mes < 10:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s0%s%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif dia < 10:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s%s0%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											else:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s%s%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))						
				else:
					
					for mes in range(1, int(mes_final)+1):
						for dia in range(1, int(dia_final)+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s0%s0%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif mes < 10:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s0%s%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif dia < 10:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s%s0%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											else:
												self.c.execute('''
													INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT %i, '%s%s%s', '%s', '%s', %i AS x 
													WHERE NOT EXISTS (SELECT * FROM Cronograma
													WHERE (id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i)) LIMIT 1;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord, id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
	def desatribuir_aulas(self, horarios_das_aulas, professor, turma, ano_inicio, mes_inicio, dia_inicio, ano_final, mes_final, dia_final, id_coord):
		executar = True		
		if int(ano_final) < int(ano_inicio):
			executar = False
		elif int(ano_final) == int(ano_inicio):
			if int(mes_final) < int(mes_inicio):
				executar = False
			elif int(mes_final) == int(mes_inicio):
					if int(dia_final) < int (dia_inicio): 
						executar = False
		if executar == True:
			self.c.execute("SELECT id_prof FROM Professor WHERE nome_prof = '%s';"%professor)
			id_professor = self.c.fetchone()[0]
			
			self.c.execute("SELECT horario FROM Horario ORDER BY (horario);")
			resultado = self.c.fetchall()
			horarios = []
			for ele in resultado:
				horarios.append(ele[0])
			
			horarios_das_aulas.insert(0,[0,0,0,0,0,0,0,0,0,0,0,0])

			dias_da_semana = []
			for dia in horarios_das_aulas:
				if 1 in dia:
					dias_da_semana.append(True)
				else:
					dias_da_semana.append(False)
			for ano in range(int(ano_inicio),int(ano_final)+1):
				if int(ano_inicio) == int(ano_final):
					for mes in range(int(mes_inicio), int(mes_final)+1):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						ultimo_dia = int(str(self.c.fetchone()[0])[8:])
						if mes == int(mes_final):
							ultimo_dia = int(dia_final)
						for dia in range(1, ultimo_dia+1):
							if mes <= int(mes_final):
								if dia < 10 and mes <10: 
									self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
								elif mes < 10:
									self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
								elif dia < 10:
									self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
								else:
									self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
								dia_da_semana = self.c.fetchone()[0]
								if dia_da_semana != None and dia_da_semana <= 7:
									if dias_da_semana[dia_da_semana-1]:
										for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
											if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
												if dia < 10 and mes <10:
													self.c.execute('''
														DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
												elif mes < 10:
													self.c.execute('''
														DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
												elif dia < 10:
													self.c.execute('''
														DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
												else:
													self.c.execute('''
														DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))

				elif ano == int(ano_inicio):
					for mes in range(int(mes_inicio), 13):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						for dia in range(1, int(str(self.c.fetchone()[0])[8:])+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif mes < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif dia < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											else:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											
										
				elif ano >int(ano_inicio) and ano < int(ano_final):
					
					for mes in range(1, 13):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						for dia in range(1, int(str(self.c.fetchone()[0])[8:])+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif mes < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif dia < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											else:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
				else:
					for mes in range(1, int(mes_final)+1):
						for dia in range(1, int(dia_final)+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif mes < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif dia < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											else:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))

	def desatribuir_qualquer_professor(self, horarios_das_aulas, turma, ano_inicio, mes_inicio, dia_inicio, ano_final, mes_final, dia_final, id_coord):
		executar = True		
		if int(ano_final) < int(ano_inicio):
			executar = False
		elif int(ano_final) == int(ano_inicio):
			if int(mes_final) < int(mes_inicio):
				executar = False
			elif int(mes_final) == int(mes_inicio):
					if int(dia_final) < int (dia_inicio): 
						executar = False
		if executar == True:
			self.c.execute("SELECT horario FROM Horario ORDER BY (horario);")
			resultado = self.c.fetchall()
			horarios = []
			for ele in resultado:
				horarios.append(ele[0])
			horarios_das_aulas.insert(0,[0,0,0,0,0,0,0,0,0,0,0,0])

			dias_da_semana = []
			for dia in horarios_das_aulas:
				if 1 in dia:
					dias_da_semana.append(True)
				else:
					dias_da_semana.append(False)
			for ano in range(int(ano_inicio),int(ano_final)+1):
				if int(ano_inicio) == int(ano_final):
					for mes in range(int(mes_inicio), int(mes_final)+1):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						ultimo_dia = int(str(self.c.fetchone()[0])[8:])
						if mes == int(mes_final):
							ultimo_dia = int(dia_final)
						for dia in range(1, ultimo_dia+1):
							if mes <= int(mes_final):
								if dia < 10 and mes <10: 
									self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
								elif mes < 10:
									self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
								elif dia < 10:
									self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
								else:
									self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
								dia_da_semana = self.c.fetchone()[0]
								if dia_da_semana != None and dia_da_semana <= 7:
									if dias_da_semana[dia_da_semana-1]:
										for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
											if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
												if dia < 10 and mes <10:
													self.c.execute('''
														DELETE FROM Cronograma WHERE data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
														'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
												elif mes < 10:
													self.c.execute('''
														DELETE FROM Cronograma WHERE data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
														'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
												elif dia < 10:
													self.c.execute('''
														DELETE FROM Cronograma WHERE data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
														'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
												else:
													self.c.execute('''
														DELETE FROM Cronograma WHERE data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
														'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))

				elif ano == int(ano_inicio):
					for mes in range(int(mes_inicio), 13):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						for dia in range(1, int(str(self.c.fetchone()[0])[8:])+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif mes < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif dia < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											else:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											
										
				elif ano >int(ano_inicio) and ano < int(ano_final):
					
					for mes in range(1, 13):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						for dia in range(1, int(str(self.c.fetchone()[0])[8:])+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif mes < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif dia < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											else:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
				else:
					for mes in range(1, int(mes_final)+1):
						for dia in range(1, int(dia_final)+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s0%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif mes < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s0%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											elif dia < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s%s0%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))
											else:
												self.c.execute('''
													DELETE FROM Cronograma WHERE data_reserva = '%s%s%s' AND horario = '%s' AND turma = '%s' AND id_coordenador = %i;
													'''%( str(ano), str(mes), str(dia), horarios[ele-1], turma, id_coord))

	def desatribuir_qualquer_turma(self, horarios_das_aulas, professor, ano_inicio, mes_inicio, dia_inicio, ano_final, mes_final, dia_final, id_coord):
		executar = True		
		if int(ano_final) < int(ano_inicio):
			executar = False
		elif int(ano_final) == int(ano_inicio):
			if int(mes_final) < int(mes_inicio):
				executar = False
			elif int(mes_final) == int(mes_inicio):
					if int(dia_final) < int (dia_inicio): 
						executar = False
		if executar == True:
			self.c.execute("SELECT id_prof FROM Professor WHERE nome_prof = '%s';"%professor)
			id_professor = self.c.fetchone()[0]
			
			self.c.execute("SELECT horario FROM Horario ORDER BY (horario);")
			resultado = self.c.fetchall()
			horarios = []
			for ele in resultado:
				horarios.append(ele[0])
			
			horarios_das_aulas.insert(0,[0,0,0,0,0,0,0,0,0,0,0,0])

			dias_da_semana = []
			for dia in horarios_das_aulas:
				if 1 in dia:
					dias_da_semana.append(True)
				else:
					dias_da_semana.append(False)
			for ano in range(int(ano_inicio),int(ano_final)+1):
				if int(ano_inicio) == int(ano_final):
					for mes in range(int(mes_inicio), int(mes_final)+1):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						ultimo_dia = int(str(self.c.fetchone()[0])[8:])
						if mes == int(mes_final):
							ultimo_dia = int(dia_final)
						for dia in range(1, ultimo_dia+1):
							if mes <= int(mes_final):
								if dia < 10 and mes <10: 
									self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
								elif mes < 10:
									self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
								elif dia < 10:
									self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
								else:
									self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
								dia_da_semana = self.c.fetchone()[0]
								if dia_da_semana != None and dia_da_semana <= 7:
									if dias_da_semana[dia_da_semana-1]:
										for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
											if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
												if dia < 10 and mes <10:
													self.c.execute('''
														DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s'  AND id_coordenador = %i;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
												elif mes < 10:
													self.c.execute('''
														DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s'  AND id_coordenador = %i;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
												elif dia < 10:
													self.c.execute('''
														DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s'  AND id_coordenador = %i;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
												else:
													self.c.execute('''
														DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s'  AND id_coordenador = %i;
														'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))

				elif ano == int(ano_inicio):
					for mes in range(int(mes_inicio), 13):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						for dia in range(1, int(str(self.c.fetchone()[0])[8:])+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s'  AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
											elif mes < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s'  AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
											elif dia < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s'  AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
											else:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s'  AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
											
										
				elif ano >int(ano_inicio) and ano < int(ano_final):
					
					for mes in range(1, 13):
						if mes < 10: 
							self.c.execute("SELECT LAST_DAY('%s-0%s-01')"%(str(ano), str(mes)));
						else:
							self.c.execute("SELECT LAST_DAY('%s-%s-01')"%(str(ano), str(mes)));
						for dia in range(1, int(str(self.c.fetchone()[0])[8:])+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s'  AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
											elif mes < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s'  AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
											elif dia < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s'  AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
											else:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s'  AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
				else:
					for mes in range(1, int(mes_final)+1):
						for dia in range(1, int(dia_final)+1):
							if dia < 10 and mes <10: 
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-0%s')"%(str(ano), str(mes), str(dia)));
							elif mes < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-0%s-%s')"%(str(ano), str(mes), str(dia)));
							elif dia < 10:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-0%s')"%(str(ano), str(mes), str(dia)));
							else:
								self.c.execute("SELECT DAYOFWEEK('%s-%s-%s')"%(str(ano), str(mes), str(dia)));
							dia_da_semana = self.c.fetchone()[0]
							if dia_da_semana != None and dia_da_semana <= 7:
								if dias_da_semana[dia_da_semana-1]:
									for ele in range(0, len(horarios_das_aulas[dia_da_semana-1])+1):
										if horarios_das_aulas[dia_da_semana-1][ele-1] == 1:
											if dia < 10 and mes <10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s0%s' AND horario = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
											elif mes < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s0%s%s' AND horario = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
											elif dia < 10:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s0%s' AND horario = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))
											else:
												self.c.execute('''
													DELETE FROM Cronograma WHERE id_professor = %i AND data_reserva = '%s%s%s' AND horario = '%s' AND id_coordenador = %i;
													'''%(id_professor, str(ano), str(mes), str(dia), horarios[ele-1], id_coord))



	def close(self):
		self.banco.close()

if __name__ == '__main__':
	BD = Banco()
	#BD.resetar_banco()	
	print(BD.nome_coordenador(id = 1))
	#remover_professor(self, nome_prof, disciplina):
	# BD.desatribuir_aulas(
	# 	horarios_das_aulas=[
	# 	[1,1,1,1,0,0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0,0,0,0,0,0],
	# 	],
	# 	professor='Rasta de Shambalá 1',
	# 	turma='TEC50419',

	# 	ano_inicio='2016',
	# 	mes_inicio='06',
	# 	dia_inicio='01',

	# 	ano_final='2017',
	# 	mes_final='11',
	# 	dia_final='13')

	# BD.atribuir_aulas(
	# 	horarios_das_aulas=[
	# 	[1,1,1,1,0,0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0,0,0,0,0,0],
	# 	],
	# 	professor='Professor do Teste1',
	# 	turma='TESTE0001',

	# 	ano_inicio='2016',
	# 	mes_inicio='06',
	# 	dia_inicio='01',

	# 	ano_final='2017',
	# 	mes_final='11',
	# 	dia_final='13',
	# 	id_coord = 1)

	# BD.desatribuir_todas_aulas(
	# 	horarios_das_aulas=[
	# 	[1,1,1,1,1,1,1,1,1,1,1,1],
	# 	[1,1,1,1,1,1,1,1,1,1,1,1],
	# 	[1,1,1,1,1,1,1,1,1,1,1,1],
	# 	[1,1,1,1,1,1,1,1,1,1,1,1],
	# 	[1,1,1,1,1,1,1,1,1,1,1,1],
	# 	[1,1,1,1,1,1,1,1,1,1,1,1],
	# 	],
	# 	turma='Turma1',
	# 	ano_inicio='2016',
	# 	mes_inicio='01',
	# 	dia_inicio='01',

	# 	ano_final='2016',
	# 	mes_final='12',
	# 	dia_final='31',
	# 	id_coord = 1)

	BD.close()