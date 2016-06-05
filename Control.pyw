import pymysql as bd

class Controle():
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

	def close(self):
		self.banco.close()
if __name__ == '__main__':
	Cont = Controle()

	print(Cont.lista_de_turmas())

	Cont.close()