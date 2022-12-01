from funcaluguel import *
from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Application(funcs):
    def __init__(self):
        
        self.root = root
        self.tela()
        self.framesaluguel()
        self.widgets()
        self.listarframe2()
        self.criatabela()
        self.select()
        root.mainloop()

    def tela(self):
            self.root.title("aluguel")
            self.root.configure(background='#1e3743')
            self.root.geometry("700x550")
            self.root.resizable(True,True)
            
    
    def framesaluguel(self):
        self.frame1 = Frame(self.root, bd=4, bg='#dfe3ee',
                            highlightbackground='#759de6', highlightthickness=2)
        self.frame1.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.4)

        self.frame2 = Frame(self.root, bd=4, bg='#dfe3ee',
                            highlightbackground='#759de6', highlightthickness=2)
        self.frame2.place(relx = 0.05, rely = 0.45,relwidth=0.9, relheight=0.5)

    def framejoin(self):
        self.framejoin = Frame(self.root2, bd=4, bg='#dfe3ee',
                            highlightbackground='#759de6', highlightthickness=2)
        self.framejoin.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.95)

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

        self.lb_id = Label(self.frame1, text="id_carro", bg='#dfe3ee', fg='#107db2')
        self.lb_id.place(relx=.02,rely=.5,relheight=.1,relwidth=.15)

        self.lb_id = Label(self.frame1, text="id_cliente", bg='#dfe3ee', fg='#107db2')
        self.lb_id.place(relx=.02,rely=.7,relheight=.1,relwidth=.15)

        self.lb_id = Label(self.frame1, text="dt_aluguel", bg='#dfe3ee', fg='#107db2')
        self.lb_id.place(relx=.02,rely=.9,relheight=.1,relwidth=.15)

        self.lb_id = Label(self.frame1, text="dt_devolucao", bg='#dfe3ee', fg='#107db2')
        self.lb_id.place(relx=.5,rely=.9,relheight=.1,relwidth=.15)

        self.btn_exibir=Button(self.frame1,text="Exibir_rel",command=self.janela2)
        self.btn_exibir.place(relx=.65,rely=.7,relheight=.1,relwidth=.15)
        #criando input
        self.idAentry = Entry(self.frame1)
        self.idAentry.place(relx=.2 ,rely=.3,relheight=.1,relwidth=.15)

        self.id_carroentry = Entry(self.frame1)
        self.id_carroentry.place(relx=.20 ,rely=.5,relheight=.1,relwidth=.15)


        
        self.id_clienteentry = Entry(self.frame1)
        self.id_clienteentry.place(relx=.20 ,rely=.7,relheight=.1,relwidth=.15)

        self.dt_aluguelentry = Entry(self.frame1)
        self.dt_aluguelentry.place(relx=.20 ,rely=.9,relheight=.1,relwidth=.30)

        self.dt_devolucaoentry = Entry(self.frame1)
        self.dt_devolucaoentry.place(relx=.65 ,rely=.9,relheight=.1,relwidth=.30)


    def listarframe2(self):
        self.listaAlug = ttk.Treeview(self.frame2,height=3, columns=("col1","col2","col3","col4","col5"))
        self.listaAlug.heading("#0", text="")
        self.listaAlug.heading("#1", text="Id")
        self.listaAlug.heading("#2", text="id_carro")
        self.listaAlug.heading("#3", text="id_cliente")
        self.listaAlug.heading("#4", text="dt_aluguel")
        self.listaAlug.heading("#5", text="dt_devolucao")
        
        self.listaAlug.column("#0", width=1)
        self.listaAlug.column("#1", width=20)
        self.listaAlug.column("#2", width=50)
        self.listaAlug.column("#3", width=80)
        self.listaAlug.column("#4", width=200)
        self.listaAlug.column("#5", width=200)

        self.listaAlug.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.85)
        
        self.scrool = Scrollbar(self.frame2, orient="vertical")
        self.listaAlug.configure(yscroll = self.scrool.set)
        self.scrool.place(relx=.95,rely=.02,relwidth=.04,relheight=.85)
        self.listaAlug.bind("<Double-1>",self.doublec)


    def janela2(self):
        self.root2 = Toplevel()
        self.root2.title("Join")
        self.root2.configure(background='#1e3743')
        self.root2.geometry("900x550")
        self.root2.resizable(True,True)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()
        self.framejoin()
        self.listarFramejoin()
        self.selectframejoin()

    def listarFramejoin(self):
        self.listaFrame = ttk.Treeview(self.framejoin,height=3, columns=("col1","col2","col3","col4","col5","col6"))
        self.listaFrame.heading("#0", text="")
        self.listaFrame.heading("#1", text="Id")
        self.listaFrame.heading("#2", text="Mod_carro")
        self.listaFrame.heading("#3", text="Nome_cliente")
        self.listaFrame.heading("#4", text="Dias alugados")
        self.listaFrame.heading("#5", text="Valor_dia")
        self.listaFrame.heading("#6", text="Valor_total")

        self.listaFrame.column("#0", width=1)
        self.listaFrame.column("#1", width=20)
        self.listaFrame.column("#2", width=200)
        self.listaFrame.column("#3", width=200)
        self.listaFrame.column("#4", width=50)
        self.listaFrame.column("#5", width=100)
        self.listaFrame.column("#6", width=100)

        self.listaFrame.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.85)
        
        self.scrool = Scrollbar(self.framejoin, orient="vertical")
        self.listaFrame.configure(yscroll = self.scrool.set)
        self.scrool.place(relx=.95,rely=.02,relwidth=.04,relheight=.85)

        #self.listaFrame.bind("<Double-1>",self.doublec)
        


    
Application()




