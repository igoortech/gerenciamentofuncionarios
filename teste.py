import sqlite3

class Sqlite_db:

    def __init__(self,namedb = None): #CRIAR BANCO DE DADOS
        self.conn = None
        self.cursor = None

        if namedb:#se tiver alguma coisa no "namedb" abra a função open
            self.open(namedb) 
	
    def open(self,namedb):
        try:
            self.conn = sqlite3.connect(namedb)
            self.cursor = self.conn.cursor()
            print(sqlite3.version)
        except sqlite3.Error as e:
            print("Não foi possível se connectar ao banco de dados")


    def criar_tabela(self): #CRIAR TABELA.
       cur = self.cursor
       cur.execute("""CREATE TABLE funcionarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    doc INTEGER NOT NULL,
                    end TEXT NOT NULL,
                    admin INTEGER 
                  )""")

    def Edit(self,query): #INSERIR E ATUALIZAR  DADOS;  INSERT AND UPDATE
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()
    
    def selecionar(self,query):#SELECIONAR OS DADOS SELECT
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()
 



#teste = Sqlite_db("TESTE.db")
#teste.criar_tabela()
    
#teste.Edit("INSERT INTO funcionarios (nome, doc, end, admin) VALUES ('IGOR','12345689','COMI CARNE', '0')")

#print(teste.selecionar("SELECT * FROM funcionarios"))

#teste.Edit("UPDATE funcionarios SET nome='marcelo' WHERE nome='IGOR' ")

#print(teste.selecionar("SELECT * FROM funcionarios")[0] [1])