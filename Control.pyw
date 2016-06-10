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
			


	def close(self):
		self.banco.close()

if __name__ == '__main__':
	BD = Banco()
	print(BD.pesquisa_cronograma(ano = '2016', mes = '06', dia = '09', horario = '07:30 - 08:30', tipo='Turma', professor_turma= 'TEC50419'))
	print(BD.pesquisa_cronograma(ano = '2016', mes = '06', dia = '09', horario = '07:30 - 08:30', tipo='Professor', professor_turma= 'Rasta de Shambalá 1'))
	BD.close()