from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class funcs:
    def con_db(self):
        self.conn = sqlite3.connect("database.db")
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
        
    

class Application(funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.framescarros()
        self.widgets()
        self.listarf2()
        self.montaTabelas()
        self.select()
        self.Menus()
        root.mainloop()

    def Menus(self):
        menubar = Menu(self.root)
        menu1 = Menu(menubar)
        menu2 = Menu(menubar)

        menubar.add_cascade(label="Opções",menu=menu1)
        menubar.add_cascade(label="Sobre",menu=menu2)


    def tela(self):
            self.root.title("Carros")
            self.root.configure(background='#1e3743')
            self.root.geometry("700x550")
            self.root.resizable(True,True)
    
    def framescarros(self):
        self.frame1 = Frame(self.root, bd=4, bg='#dfe3ee',
                            highlightbackground='#759de6', highlightthickness=2)
        self.frame1.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.4)

        self.frame2 = Frame(self.root, bd=4, bg='#dfe3ee',
                            highlightbackground='#759de6', highlightthickness=2)
        self.frame2.place(relx = 0.05, rely = 0.45,relwidth=0.9, relheight=0.5)
        
    def widgets(self):
        self.btn_lmp = Button(self.frame1,text="Limpar",bd=2,bg='#107db2',fg='white',command=self.limp_jan)
        self.btn_lmp.place(relx=.20,rely=.1,relheight=.1,relwidth=.15)

        self.btn_buscar=Button(self.frame1,text="Buscar", command=self.buscar)
        self.btn_buscar.place(relx=.35,rely=.1,relheight=.1,relwidth=.15)

        self.btn_ins = Button(self.frame1,text="Inserir",command=self.inserir)
        self.btn_ins.place(relx=.5,rely=.1,relheight=.1,relwidth=.15)

        self.btn_alt=Button(self.frame1,text="Alterar",command=self.alterar)
        self.btn_alt.place(relx=.65,rely=.1,relheight=.1,relwidth=.15)

        self.btn_del=Button(self.frame1,text="Deletar",command=self.deletar)
        self.btn_del.place(relx=.80,rely=.1,relheight=.1,relwidth=.15)

        self.lb_id = Label(self.frame1, text="Código",bg='#dfe3ee',fg='#107db2')
        self.lb_id.place(relx=.02,rely=.3,relheight=.1,relwidth=.15)

        self.lb_id = Label(self.frame1, text="Marca", bg='#dfe3ee', fg='#107db2')
        self.lb_id.place(relx=.02,rely=.5,relheight=.1,relwidth=.15)

        self.lb_id = Label(self.frame1, text="Modelo", bg='#dfe3ee', fg='#107db2')
        self.lb_id.place(relx=.02,rely=.7,relheight=.1,relwidth=.15)

        self.lb_id = Label(self.frame1, text="Val Hr", bg='#dfe3ee', fg='#107db2')
        self.lb_id.place(relx=.02,rely=.9,relheight=.1,relwidth=.15)

        #criando input
        self.identry = Entry(self.frame1)
        self.identry.place(relx=.2 ,rely=.3,relheight=.1,relwidth=.15)

        self.marcaentry = Entry(self.frame1)
        self.marcaentry.place(relx=.20 ,rely=.5,relheight=.1,relwidth=.40)

        self.modelentry = Entry(self.frame1)
        self.modelentry.place(relx=.20 ,rely=.7,relheight=.1,relwidth=.40)

        self.valhrentry = Entry(self.frame1)
        self.valhrentry.place(relx=.20 ,rely=.9,relheight=.1,relwidth=.40)

    def listarf2(self):
        self.listaCar = ttk.Treeview(self.frame2,height=3, columns=("col1","col2","col3","col4"))
        self.listaCar.heading("#0", text="")
        self.listaCar.heading("#1", text="Id")
        self.listaCar.heading("#2", text="Marca")
        self.listaCar.heading("#3", text="Modelo")
        self.listaCar.heading("#4", text="ValorHr")
        
        self.listaCar.column("#0", width=1)
        self.listaCar.column("#1", width=50)
        self.listaCar.column("#2", width=200)
        self.listaCar.column("#3", width=125)
        self.listaCar.column("#4", width=125)

        self.listaCar.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.85)
        
        self.scrool = Scrollbar(self.frame2, orient="vertical")
        self.listaCar.configure(yscroll = self.scrool.set)
        self.scrool.place(relx=.95,rely=.02,relwidth=.04,relheight=.85)

        self.listaCar.bind("<Double-1>",self.doublec)

Application()




