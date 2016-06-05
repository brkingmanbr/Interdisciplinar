import pymysql
class mysql():
    parametros = {'user': 'root',
                  'host': 'localhost',
                  'passwd': '',
                  'database': 'pfcteste'}
                  
    Banco = pymysql.connect(**parametros)
    c = Banco.cursor()
    def teste(self):
        self.c.execute('SELECT * FROM login')
        self.c.fetchone()
        print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()
if __name__ == '__main__':
    x = mysql()
    x.teste()
