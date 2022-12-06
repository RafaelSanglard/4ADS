from tkinter import *
from tkinter import ttk
import sqlite3
from funclientes import *
import os

root = Tk()
path = os.path.dirname(__file__)

class Application(funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.framesclientes()
        self.widgets()
        self.listarf2()
        self.criarTabela()
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
            #img=PhotoImage(file= path+'/logo.png') 
            #self.root.iconphoto(False,img)
            self.root.title("clientes")
            self.root.configure(background='#1e3743')
            self.root.geometry("700x550")
            self.root.resizable(True,True)
    
    def framesclientes(self):
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

        self.lb_id = Label(self.frame1, text="ID-Cliente:",bg='#dfe3ee',fg='#107db2')
        self.lb_id.place(relx=.02,rely=.3,relheight=.1,relwidth=.15)

        self.lb_id = Label(self.frame1, text="Nome:", bg='#dfe3ee', fg='#107db2')
        self.lb_id.place(relx=.02,rely=.5,relheight=.1,relwidth=.15)

        #self.lb_id = Label(self.frame1, text=", bg='#dfe3ee', fg='#107db2')
        #self.lb_id.place(relx=.02,rely=.7,relheight=.1,relwidth=.15)

        self.lb_id = Label(self.frame1, text="CEP", bg='#dfe3ee', fg='#107db2')
        self.lb_id.place(relx=.02,rely=.7,relheight=.1,relwidth=.15)

        #criando input
        self.identry = Entry(self.frame1)
        self.identry.place(relx=.2 ,rely=.3,relheight=.1,relwidth=.15)

        self.nomeentry = Entry(self.frame1)
        self.nomeentry.place(relx=.20 ,rely=.5,relheight=.1,relwidth=.40)

        #self. = Entry(self.frame1)
        #self..place(relx=.20 ,rely=.7,relheight=.1,relwidth=.40)

        self.cepentry = Entry(self.frame1)
        self.cepentry.place(relx=.20 ,rely=.7,relheight=.1,relwidth=.40)

    def listarf2(self):
        self.listaCle = ttk.Treeview(self.frame2,height=3, columns=("col1","col2","col3"))
        self.listaCle.heading("#0", text="")
        self.listaCle.heading("#1", text="Id_cliente")
        self.listaCle.heading("#2", text="nome")
        self.listaCle.heading("#3", text="CEP")
        
        self.listaCle.column("#0", width=0)
        self.listaCle.column("#1", width=50)
        self.listaCle.column("#2", width=250)
        self.listaCle.column("#3", width=50)

        self.listaCle.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.85)
        
        self.scrool = Scrollbar(self.frame2, orient="vertical")
        self.listaCle.configure(yscroll = self.scrool.set)
        self.scrool.place(relx=.95,rely=.02,relwidth=.04,relheight=.85)

        self.listaCle.bind("<Double-1>",self.doublec)

Application()




