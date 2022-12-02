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
    
    def criatabela(self):
        self.con_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "aluguel" (
                "id_aluguel" INTEGER PRIMARY KEY,
                "id_carro"	INTEGER,
                "id_cliente" INTEGER,
                "dt_aluguel"DATA,
                "dt_devolucao"DATA
                );
        """)
        print("Tabela criada");self.conn.commit()
        self.des_db()

    def inserir(self):
        self.variaveis()

        self.con_db()
        self.cursor.execute("""
            INSERT INTO "aluguel" (id_aluguel,id_carro,id_cliente,dt_aluguel,dt_devolucao)
                   VALUES(?,?,?,?,?)""", (self.id_aluguel, self.id_carro, self.id_cliente, self.dt_aluguel,self.dt_devolucao))
        self.conn.commit()
        self.des_db()
        self.select()
        self.limp_jan()

    def select(self):
        self.listaAlug.delete(*self.listaAlug.get_children())
        self.con_db()
        lista = self.cursor.execute("""SELECT id_aluguel, id_carro, id_cliente, dt_aluguel, dt_devolucao FROM aluguel
        ORDER BY id_aluguel""")
        for i in lista:
            self.listaAlug.insert("",END,values=i)
        self.des_db()

    def selectframejoin(self):
        self.listaFrame.delete(*self.listaFrame.get_children())
        self.con_db()
        #DATEDIFF não presente no sqlite3
        listaj = self.cursor.execute("""
        SELECT 
            aluguel.id_aluguel, 
            carros.modelo, 
            clientes.nome, 
            (JULIANDAY(aluguel.dt_devolucao) - JULIANDAY(aluguel.dt_aluguel))+1,
            carros.valor_hr, 
            (JULIANDAY(aluguel.dt_devolucao) - JULIANDAY(aluguel.dt_aluguel)+1) * carros.valor_hr
        FROM
            aluguel
        INNER JOIN
           clientes
            ON 
                aluguel.id_cliente = clientes.id_cliente
        INNER JOIN
            carros
            ON 
                aluguel.id_carro = carros.id_carro
  """)
        for i in listaj:
            self.listaFrame.insert("",END,values=i)
        self.des_db()

    def variaveis(self):
        self.id_aluguel = self.idAentry.get()
        self.id_carro=self.id_carroentry.get()
        self.id_cliente=self.id_clienteentry.get()
        self.dt_aluguel=self.dt_aluguelentry.get()
        self.dt_devolucao = self.dt_devolucaoentry.get()
        
    def doublec(self, event):
        self.limp_jan()
        self.listaAlug.selection()
        for x in self.listaAlug.selection():
            col1,col2,col3,col4,col5 = self.listaAlug.item(x,'values')
            self.idAentry.insert(END, col1)
            self.id_carroentry.insert(END, col2)
            self.id_clienteentry.insert(END, col3)
            self.dt_aluguelentry.insert(END, col4)
            self.dt_devolucaoentry.insert(END, col5)

    def deletar(self):
        self.variaveis()
        self.con_db()

        self.cursor.execute("""
            DELETE FROM aluguel WHERE id_aluguel  = ?       
        """, (self.id_aluguel))
        self.conn.commit()
        self.des_db()
        self.limp_jan()
        self.select()

    def alterar(self):
        self.variaveis()
        self.con_db()

        self.cursor.execute("""
                UPDATE aluguel SET id_carro = ?, id_cliente = ?, dt_aluguel= ?, dt_devolucao = ?
                WHERE id_aluguel = ?""",(self.id_carro,self.id_cliente,self.dt_aluguel,self.dt_devolucao,self.id_aluguel))

        self.conn.commit()
        self.des_db()
        self.select()
        self.limp_jan()

    def buscar(self):
        self.con_db()
        self.listaAlug.delete(*self.listaAlug.get_children())

        self.id_carroentry.insert(END,'%')
        id_carro = self.id_carroentry.get()
        self.cursor.execute(
            """SELECT id_aluguel, id_carro, id_cliente, dt_aluguel,self.dt_devolucao FROM aluguel 
            WHERE id_carro LIKE '%s' ORDER BY id_cliente
        """%id_carro)
        buscaid_carro = self.cursor.fetchall()
        for i in buscaid_carro:
            self.listaAlug.insert("", END, values = i)
        self.des_db()

    def limp_jan(self):
        self.idAentry.delete(0, END)
        self.id_carroentry.delete(0, END)
        self.id_clienteentry.delete(0, END)
        self.dt_aluguelentry.delete(0, END)
        self.dt_devolucaoentry.delete(0,END)
        