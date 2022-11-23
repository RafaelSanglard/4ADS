# INTERFACE GRÁFICA COM BANCO DE DADOS
from tkinter import *
from tkinter import messagebox
import os
import sqlite3

path = os.path.dirname(__file__)

#favicon = path+'\\computador.ico'

app = Tk()
app.title('CRUD Clientes')

#app.iconbitmap(favicon)
app.geometry('400x200')

# BANCO DE DADOS - SQLITE3
conn = sqlite3.connect('database.db')
c = conn.cursor()

def editar():
    

    #GRAVAR REGISTRO
    c.execute("Update clientes SET nome = value1, cep = value2 WHERE condition VALUES (:nome, :cep)",
    {
        
        'nome':vnome.get(),
        'cep':vcep.get()
    })

    conn.commit()
    conn.close()
    # CAIXA DE MENSAGEM
    messagebox.showinfo("MENSAGEM IMPORTANTE",
    "Informações gravadas com sucesso!")

    # LIMPA CAMPOS
    vnome.delete(0, END)
    vcep.delete(0, END)

    Entry.focus(vnome)


#CRIAÇÃO DE TABELA
c.execute("""CREATE TABLE IF NOT EXISTS clientes(

             id_cliente,
             nome text,
             cep text)""")

#Cria função visualizar
def exibir():
    c.execute("SELECT * FROM clientes")
    rowex = c.fetchall()
    messagebox.showinfo("Informações exibidas com sucesso!")
   

    
    

# CRIA FUNÇÃO BOTÃO DE COMANDO
def gravar():
    # BANCO DE DADOS - SQLITE3
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    #GRAVAR REGISTRO
    c.execute("INSERT INTO clientes VALUES ('',:nome, :cep)",
    {
        
        'nome':vnome.get(),
        'cep':vcep.get()
    })

    conn.commit()
    conn.close()
    # CAIXA DE MENSAGEM
    messagebox.showinfo("MENSAGEM IMPORTANTE",
    "Informações gravadas com sucesso!")

    # LIMPA CAMPOS
    vnome.delete(0, END)
    vcep.delete(0, END)

    Entry.focus(vnome)


    # VARIÁVEIS DE ENTRADA
vnome = Entry(app, width=30)
vnome.grid(row=0, column=1, padx=20)

vcep = Entry(app, width=30)
vcep.grid(row=1, column=1)

    # RÓTULOS PARA AS ENTRADAS
nomel = Label(app, text='Nome: ')
nomel.grid(row=0, column=0)

cepl = Label(app, text='CEP: ')
cepl.grid(row=1, column=0)



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



app.mainloop()