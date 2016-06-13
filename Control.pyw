import pymysql as bd

class Banco():
	def __init__(self):
	    self.parametros = {'user':'root',#user.get(),
	                  'host':'localhost',#host.get(),
	                  'passwd':'40028922',#senha.get(),
	                  'autocommit':True}
	    self.banco = bd.connect(**self.parametros)
	    self.c = self.banco.cursor()
	    self.c.execute('USE SIS;')

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
	def parametros_mes(self, mes):
		return self.quant_dias_do_mes(mes = mes), self.primeiro_dia_do_mes(mes = mes)

	def ano_atual(self):
		self.c.execute('SELECT NOW();')
		ano = int(str(self.c.fetchone()[0])[:4])
		return ano
	def lista_de_professores(self):
		self.c.execute('SELECT matricula, nome_prof FROM Professor ORDER BY matricula;')
		profesores = self.c.fetchall()
		return profesores
	def lista_de_turmas(self):
		self.c.execute('SELECT nome_turma, turno FROM Turma ORDER BY nome_turma;')
		turmas = self.c.fetchall()
		return turmas
	def verifica_login(self, login, senha):
		self.c.execute("SELECT senha FROM Coordenador where login = '%s';"%login)
		Senha = self.c.fetchone()[0]
		if senha == Senha:
			return True
		else:
			return False

	def nomes_professores(self):
		self.c.execute("SELECT nome_prof FROM Professor;")
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

	def adicionar_no_cronograma(self, professor, data_reserva, horario, turma):
		self.c.execute("insert into Cronograma values(%i, '20160806', '07:30 - 08:30', 'TEC50419', 1);"%(id_professor, data_reserva, horario, turma, id_coordenador))

	def pesquisa_cronograma(self, ano, mes, dia, horario, tipo='', professor_turma=''):
		if tipo == 'Professor':
			self.c.execute("SELECT id_prof FROM Professor where nome_prof = '%s';"%professor_turma)
			id_professor = self.c.fetchone()[0]
			self.c.execute("select turma from Cronograma where data_reserva = '%s%s%s' and horario = '%s' and id_professor = '%i';"%(str(ano), mes, str(dia), horario, id_professor))
			turma = self.c.fetchone()
			if turma == None:
				return horario
			else:
				return turma[0]
		elif tipo == 'Turma':
			self.c.execute("select id_professor from Cronograma where data_reserva = '%s%s%s' and horario = '%s' and turma = '%s';"%(str(ano), mes, str(dia), horario, professor_turma))
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

	def atribuir_aulas(self, lista_de_checkbox, professor, turma, ano_inicio, mes_inicio, dia_inicio, ano_final, mes_final, dia_final):
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
		
			#dias = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
			#meses = ['01','02','03','04','05','06','07','08','09','10','11','12']
			#anos = ['2016','2017','2018']
			horario =  "00"
			lista_de_checkbox.insert(0,[0,0,0,0,0,0,0,0,0,0,0,0])
			dias_da_semana = []
			for dia in lista_de_checkbox:
				if 1 in dia:
					dias_da_semana.append(True)
				else:
					dias_da_semana.append(False)
			print(dias_da_semana)
			for ano in range(int(ano_inicio),int(ano_final)+1):
				print("ANO ############################### ",ano)
				if int(ano_inicio) == int(ano_final):
					print('==')
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
								if dia_da_semana != None and dia_da_semana < 7:
									print(dias_da_semana[dia_da_semana-1],dia_da_semana)
									if dias_da_semana[dia_da_semana-1]:
										if dia < 10 and mes <10: 
											print('''
												INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
												VALUES (%i, %s0%s0%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
										elif mes < 10:
											print('''
												INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
												VALUES (%i, %s0%s%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
										elif dia < 10:
											print('''
												INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
												VALUES (%i, %s%s0%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
										else:
											print('''
												INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
												VALUES (%i, %s%s%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
										
				elif ano == int(ano_inicio):
					print('==inicio')
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
							if dia_da_semana != None and dia_da_semana < 7:
								if dias_da_semana[dia_da_semana-1]:
									print(dias_da_semana[dia_da_semana-1],dia_da_semana)
									if dia < 10 and mes <10: 
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s0%s0%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
									elif mes < 10:
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s0%s%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
									elif dia < 10:
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s%s0%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
									else:
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s%s%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))

				elif ano >int(ano_inicio) and ano < int(ano_final):
					print('><')
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
							if dia_da_semana != None and dia_da_semana < 7:
								if dias_da_semana[dia_da_semana-1]:
									print(dias_da_semana[dia_da_semana-1],dia_da_semana)
									if dia < 10 and mes <10: 
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s0%s0%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
									elif mes < 10:
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s0%s%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
									elif dia < 10:
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s%s0%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
									else:
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s%s%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
				else:
					print('last')
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
							if dia_da_semana != None and dia_da_semana < 7:
								if dias_da_semana[dia_da_semana-1]:
									print(dias_da_semana[dia_da_semana-1],dia_da_semana)
									if dia < 10 and mes <10: 
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s0%s0%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
									elif mes < 10:
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s0%s%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
									elif dia < 10:
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s%s0%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))
									else:
										print('''
											INSERT INTO  cronograma (id_professor, data_reserva, horario, turma)
											VALUES (%i, %s%s%s, %s, %s);'''%(id_professor, str(ano), str(mes), str(dia), horario, turma))

			print("professor, turma, ano_inicio, mes_inicio, dia_inicio, ano_final, mes_final, dia_final\n",
				professor, turma, ano_inicio, mes_inicio, dia_inicio, ano_final, mes_final, dia_final)





			# self.c.execute('''
			# 	INSERT INTO 
			# 	cronograma (id_professor, data_reserva, horario, turma)
			# 	VALUES (%i, %s, %s, %s);'''%(id_professor, data_reserva, horario, turma))
			#def atribuir_aulas(self):

	def close(self):
		self.banco.close()

if __name__ == '__main__':
	BD = Banco()

	BD.atribuir_aulas(
		lista_de_checkbox=[
		[1,1,1,1,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		],
		professor='Rasta de Shambalá 1',
		turma='TEC50419',

		ano_inicio='2016',
		mes_inicio='06',
		dia_inicio='01',

		ano_final='2017',
		mes_final='11',
		dia_final='13')

	BD.close()