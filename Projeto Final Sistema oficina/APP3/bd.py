import sqlite3

class Database:
    def __init__(self,db):
        #cria conexão com o banco
        self.con = sqlite3.connect(db)
        #Cria o cursor para as operações no banco
        self.cursor = self.con.cursor()
        # Comando para criar tabela de funcionários
        sql = """CREATE TABLE IF NOT EXISTS funcionarios(id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, data TEXT, email TEXT, genero TEXT, telefone TEXT, endereço TEXT)"""
        #eXECUTANDO O COMANDO acima
        self.cursor.execute(sql)
        #persistindo
        self.con.commit()

    def insert(self,nome,idade,data,email,genero,telefone,endereço):
        self.cursor.execute("INSERT INTO funcionarios VALUES (NULL,?,?,?,?,?,?,?)",(nome,idade,data,email,genero,telefone,endereço))

        self.con.commit()

    def fetch(self):
        self.cursor.execute("SELECT* FROM funcionarios")
        linhas = self.cursor.fetchall()
        return linhas

    def remove(self,id):
        self.cursor.execute("DELETE FROM funcionarios WHERE id=?",(id,))
        self.con.commit()

    def update(self,id,nome,idade,data,email,genero,telefone,endereço):
        self.cursor.execute("UPDATE funcionarios SET nome=?, idade=?, data=?, email=?, genero=?,telefone=?,endereco=? WHERE id=?", (nome,idade,data,email,genero,telefone,endereço,id))
        self.con.commit()

        