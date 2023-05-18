import sqlite3

class  sqlite_db:

    def __init__(self,banco =None): #cria banco de dados 
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)

    def open(self,banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Não foi possivel estabelecer conexão!")
    
    def criar_tabela(self):
        cur = self.cursor
        cur.execute("""CREATE TABLE funcionarios(
            id  integer primary key autoincrement,
            nome text NOT NULL,
            documento INTEGER NOT NULL,
            endereco TEXT NOT NULL,
            admin integer)""")


    
    def inserir_apaga_atualiza(self,query):
        cur = self.cursor
        cur.execute(query)  
        self.conn.commit()

    def pega_dados(self,query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()

    


#db = sqlite_db("manager.db")



#nome = "marcelo"
#docu = 1123213323
#end = "teste teste"
#adm =1
#db.inserir_apaga_atualiza("INSERT INTO funcionarios (nome, documento,endereco,admin) VALUES ('{}', '{}', '{}', '{}')".format(nome,docu,end,adm))
#db.inserir_apaga_atualiza("INSERT INTO user (username, password, acesso)  VALUES ('igor', '1234', 'admin') ")
#db.inserir_apaga_atualiza("UPDATE funcionarios SET nome='MARCELO GOSTOSO', documento='marirla', endereco='aaaa' WHERE id='5'")
#db.inserir_apaga_atualiza("DELETE FROM funcionarios WHERE nome='MARCELO GOSTOSO'")
#print(db.pega_dados("SELECT * FROM  user")) #PEGA TUDO DE FUNCIONARIOS

#db.criar_tabela()
