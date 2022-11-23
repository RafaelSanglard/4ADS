# INTERFACE GRÁFICA COM BANCO DE DADOS
from tkinter import *
from tkinter import messagebox
import os

path = os.path.dirname(__file__)

#favicon = path+'\\computador.ico'

app = Tk()
app.title('Main')

#app.iconbitmap(favicon)
app.geometry('330x300')
def addcliente():
   # Clientes
   import Clientes
def addcarros():
   # Clientes
   import Carros

botao = Button(app, text='Adicionar clientes',
command=addcliente)
botao.grid(row=0, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)

botao = Button(app, text='Visualizar clientes',
)
botao.grid(row=1, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)
botao = Button(app, text='Remover cliente',
)
botao.grid(row=2, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)

botao = Button(app, text='Editar cliente',
)
botao.grid(row=3, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)

botao = Button(app, text='Adicionar carro',
command=addcarros)
botao.grid(row=4, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)
#botao = Button(app, text='Visualizar registros',
#command=exibir)
#botao2.grid(row=7, column=0, columnspan=2, pady=10,
#padx=10, ipadx=100)

app.mainloop()