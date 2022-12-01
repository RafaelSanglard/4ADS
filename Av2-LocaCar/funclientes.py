from tkinter import *
from tkinter import ttk
import sqlite3
class funcs:
    def con_db(self):
        self.conn = sqlite3.connect("databse.db")
        self.cursor = self.conn.cursor()
        print("Conectado ao bd")

    def des_db(self):
        self.conn.close()
    
    def criarTabela(self):
        self.con_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "clientes" (
                "id_cliente" INTEGER PRIMARY KEY,
                "nome" TEXT,
                "cep" TEXT
                );
        """)
        print("Tabela criada");self.conn.commit()
        self.des_db()

    def inserir(self):
        self.variaveis()

        self.con_db()
        self.cursor.execute("""
            INSERT INTO "clientes" (id_cliente,nome,cep)
                   VALUES(?,?,?)""", (self.id_cliente, self.nome, self.cep))
        self.conn.commit()
        self.des_db()
        self.select()
        self.limp_jan()

    def select(self):
        self.listaCle.delete(*self.listaCle.get_children())
        self.con_db()
        lista = self.cursor.execute("""SELECT id_cliente,nome,cep FROM clientes
        ORDER BY nome""")
        for i in lista:
            self.listaCle.insert("",END,values=i)
        self.des_db()

    def variaveis(self):
        self.id_cliente = self.identry.get()
        self.nome=self.nomeentry.get()
        self.cep = self.cepentry.get()
        
    def doublec(self, event):
        self.limp_jan()
        self.listaCle.selection()
        for x in self.listaCle.selection():
            col1,col2,col3 = self.listaCle.item(x,'values')
            self.identry.insert(END, col1)
            self.nomeentry.insert(END, col2)
            self.cepentry.insert(END, col3)

    def deletar(self):
        self.variaveis()
        self.con_db()

        self.cursor.execute("""
            DELETE FROM clientes WHERE id_cliente  = ?       
        """, (self.id_cliente))
        self.conn.commit()
        self.des_db()
        self.limp_jan()
        self.select()

    def alterar(self):
        self.variaveis()
        self.con_db()

        self.cursor.execute("""
                UPDATE clientes SET nome = ?,  cep = ?
                WHERE id_cliente = ?""",(self.nome,self.cep,self.id_cliente))

        self.conn.commit()
        self.des_db()
        self.select()
        self.limp_jan()

    def buscar(self):
        self.con_db()
        self.listaCle.delete(*self.listaCle.get_children())

        self.nomeentry.insert(END,'%')
        nome = self.nomeentry.get()
        self.cursor.execute(
            """SELECT id_cliente, nome, cep FROM clientes 
            WHERE nome LIKE '%s' ORDER BY
        """%nome)
        buscanome = self.cursor.fetchall()
        for i in buscanome:
            self.listaCle.insert("", END, values = i)
        self.des_db()

    def limp_jan(self):
        self.identry.delete(0, END)
        self.nomeentry.delete(0, END)
        self.cepentry.delete(0, END)