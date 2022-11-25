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
def fcliente():
   # Clientes
   import Clientes
def fcarro():
   # Carros
   import Carros


botao = Button(app, text='Funcionalidades clientes',
command=fcliente)
botao.grid(row=0, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)

botao1 = Button(app, text='Funcionalidades aluguels',
)
botao1.grid(row=1, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)

botao3 = Button(app, text='Funcionalidades carro',
command=fcarro)
botao3.grid(row=2, column=0, columnspan=2, pady=10,
padx=10, ipadx=100)


app.mainloop()