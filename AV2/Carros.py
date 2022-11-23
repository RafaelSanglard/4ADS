
# INTERFACE GRÁFICA COM BANCO DE DADOS
from tkinter import *
from tkinter import messagebox
import os
import sqlite3

path = os.path.dirname(__file__)

#favicon = path+'\\computador.ico'

app = Tk()
app.title('CRUD Carros')

#app.iconbitmap(favicon)
app.geometry('400x200')

# BANCO DE DADOS - SQLITE3
conn = sqlite3.connect('database.db')
c = conn.cursor()

def editar():
    

    #GRAVAR REGISTRO
    c.execute("Update carros SET marca, modelo = value1, valor_dia = value2 WHERE condition VALUES (:marca, :modelo, :valor_dia)",
    {
        
        'marca':vmarca.get(), 
        'modelo':vmodelo.get(),
        'valor_dia':val_dia.get()
    })

    c.commit()
    c.close()
    # CAIXA DE MENSAGEM
    messagebox.showinfo("MENSAGEM IMPORTANTE",
    "Informações gravadas com sucesso!")

    # LIMPA CAMPOS
    vmarca.delete(0, END) 
    vmodelo.delete(0, END)
    val_dia.delete(0, END)

    Entry.focus(vmarca)
    Entry.focus(vmodelo)
    Entry.focus(val_dia)


#CRIAÇÃO DE TABELA
c.execute("""CREATE TABLE IF NOT EXISTS carros(

             id_carro integer,
             marca text,
             modelo text,
             valor_dia text)""")

#Cria função visualizar
def exibir():
    c.execute("SELECT * FROM carros")
    rowex = c.fetchall()
    messagebox.showinfo("Informações exibidas com sucesso!")
   

    
    

# CRIA FUNÇÃO BOTÃO DE COMANDO
def gravar():
    # BANCO DE DADOS - SQLITE3
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    #GRAVAR REGISTRO
    c.execute("INSERT INTO carros VALUES ('',:marca, :modelo, :valor_dia)",
    {
        
        'marca':vmarca.get(),
        'modelo':vmodelo.get(),
        'valor_dia':val_dia.get()
    })

    conn.commit()
    conn.close()
    # CAIXA DE MENSAGEM
    messagebox.showinfo("MENSAGEM IMPORTANTE",
    "Informações gravadas com sucesso!")

    # LIMPA CAMPOS
    vmarca.delete(0,END)
    vmodelo.delete(0, END)
    val_dia.delete(0, END)

    Entry.focus(vmarca)


    # VARIÁVEIS DE ENTRADA
vmarca= Entry(app, width=30)
vmarca.grid(row=0, column=1, padx=20)


vmodelo = Entry(app, width=30)
vmodelo.grid(row=1, column=1, padx=20)

val_dia = Entry(app, width=30)
val_dia.grid(row=2, column=1)

    # RÓTULOS PARA AS ENTRADAS
marcal = Label(app, text='marca: ')
marcal.grid(row=0, column=0)

modelol = Label(app, text='modelo: ')
modelol.grid(row=1, column=0)

val_dia1 = Label(app, text='val_dia: ')
val_dia1.grid(row=2, column=0)



# CRIANDO BOTÃO DE COMANDO
botao1 = Button(app, text='Adicionar registro',
command=gravar)
botao1.grid(row=6, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)

botao2 = Button(app, text='Visualizar registros',
command=exibir())
botao2.grid(row=7, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)

conn.commit()
conn.close()



#app.mainloop()