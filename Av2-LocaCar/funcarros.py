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
    
    def montaTabelas(self):
        self.con_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "carros" (
                "id_carro" INTEGER PRIMARY KEY,
                "marca"	TEXT,
                "modelo" TEXT,
                "valor_hr" NUMERIC
                );
        """)
        print("Tabela criada");self.conn.commit()
        self.des_db()

    def inserir(self):
        self.variaveis()

        self.con_db()
        self.cursor.execute("""
            INSERT INTO "carros" (id_carro,marca,modelo,valor_hr)
                   VALUES(?,?,?,?)""", (self.id_carro, self.marca, self.modelo, self.valor_hr))
        self.conn.commit()
        self.des_db()
        self.select()
        self.limp_jan()

    def select(self):
        self.listaCar.delete(*self.listaCar.get_children())
        self.con_db()
        lista = self.cursor.execute("""SELECT id_carro,marca,modelo,valor_hr FROM carros
        ORDER BY marca""")
        for i in lista:
            self.listaCar.insert("",END,values=i)
        self.des_db()

    def variaveis(self):
        self.id_carro = self.identry.get()
        self.marca=self.marcaentry.get()
        self.modelo=self.modelentry.get()
        self.valor_hr = self.valhrentry.get()
        
    def doublec(self, event):
        self.limp_jan()
        self.listaCar.selection()
        for x in self.listaCar.selection():
            col1,col2,col3,col4 = self.listaCar.item(x,'values')
            self.identry.insert(END, col1)
            self.marcaentry.insert(END, col2)
            self.modelentry.insert(END, col3)
            self.valhrentry.insert(END, col4)

    def deletar(self):
        self.variaveis()
        self.con_db()

        self.cursor.execute("""
            DELETE FROM carros WHERE id_carro  = ?       
        """, (self.id_carro))
        self.conn.commit()
        self.des_db()
        self.limp_jan()
        self.select()

    def alterar(self):
        self.variaveis()
        self.con_db()

        self.cursor.execute("""
                UPDATE carros SET marca = ?, modelo = ?, valor_hr = ?
                WHERE id_carro = ?""",(self.marca,self.modelo,self.valor_hr,self.id_carro))

        self.conn.commit()
        self.des_db()
        self.select()
        self.limp_jan()

    def buscar(self):
        self.con_db()
        self.listaCar.delete(*self.listaCar.get_children())

        self.marcaentry.insert(END,'%')
        marca = self.marcaentry.get()
        self.cursor.execute(
            """SELECT id_carro, marca, modelo, valor_hr FROM carros 
            WHERE marca LIKE '%s' ORDER BY modelo
        """%marca)
        buscaMarca = self.cursor.fetchall()
        for i in buscaMarca:
            self.listaCar.insert("", END, values = i)
        self.des_db()

    def limp_jan(self):
        self.identry.delete(0, END)
        self.marcaentry.delete(0, END)
        self.modelentry.delete(0, END)
        self.valhrentry.delete(0, END)
        
    
