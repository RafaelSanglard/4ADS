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
app.geometry('400x250')

# BANCO DE DADOS - SQLITE3
conn = sqlite3.connect('database.db')
c = conn.cursor()
#CRIAÇÃO DE TABELA
c.execute("""CREATE TABLE IF NOT EXISTS clientes(

             id_cliente,
             nome text,
             cep text)""")

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




#Cria função visualizar
def exibir():
    top = Tk()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clientes")
    myresult = c.fetchall()
    i=0
    for x in myresult:
        Lb = Listbox(top)
        Lb.insert(i, myresult)
        print(x)
    #    Lb.insert(2, 'Java')
    #    Lb.insert(3, 'C++')
    #    Lb.insert(4, 'Any other')
    #    Lb.pack()
        i+=1
    Lb.pack()
    conn.close


    #messagebox.showinfo("Informações exibidas com sucesso!")
   

def deletar():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute("DELETE FROM clientes WHERE nome = ':nome'"),
    {
        'nome':vnome.get()  
    }
    print(c.rowcount, "record(s) deleted")   
    conn.commit()
    conn.close()
    c.close()



    

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
    c.close()
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
command=exibir)
botao2.grid(row=7, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)

botao3=Button(app, text="Remover cliente por nome", 
command=deletar) #button to close the window
botao3.grid(row=8, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)

botao4=Button(app, text="Quit", command=app.destroy) #button to close the window
botao4.grid(row=9, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)

conn.commit()
conn.close()



#app.mainloop()