# INTERFACE GRÁFICA COM BANCO DE DADOS
from tkinter import *
from tkinter import messagebox
import os

root = Tk()
path = os.path.dirname(__file__)
class main():
      
   def __init__(self):
         self.root = root
         self.tela()
         self.widgets()
         root.mainloop()


   def tela(self):
         self.root.title('Main')
         self.root.configure(background='#1e3743')
         self.root.geometry('330x300')
         img=PhotoImage(file = path+'/logo.png')      
         self.root.iconphoto(False,img)
         self.root.resizable(True,True)

   def fcliente(self):
      from clientes import Application
   
   def fcarro(self):
      from carros import Application
   
   def faluguel(self):
      from aluguel import Application

   
   def widgets(self):   
         self.botao = Button(self.root, text='Funcionalidades clientes',
         command=self.fcliente)
         self.botao.place(relx=.10,rely=.1,relheight=.1,relwidth=.8)
         

         self.botao1 = Button(self.root, text='Funcionalidades aluguéis ',
         command=self.faluguel)
         self.botao1.place(relx=.10,rely=.3,relheight=.1,relwidth=.8)

         self.botao2 = Button(self.root, text='Funcionalidades carro',
         command=self.fcarro)
         self.botao2.place(relx=.10,rely=.5,relheight=.1,relwidth=.8)

main()