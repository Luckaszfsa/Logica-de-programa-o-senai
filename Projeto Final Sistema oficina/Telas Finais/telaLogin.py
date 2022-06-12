<<<<<<< HEAD
from tkinter import *

class Tela_de_Login:
    def __init__(self):
        self.janela = Tk()
        self.janela.minsize(width=1200,height=600)
        self.janela.title("Sistema Automotivo Soluções")
        self.janela.resizable(False,False)
        self.LoginCanvas = Canvas(self.janela, width = 500, height=370)
        self.LoginCanvas.pack(expand=1,fill=BOTH)
        self.janela.state("zoomed")
     

        self.Back = PhotoImage(file="back.png")
        self.LoginCanvas.create_image(700,350,image=self.Back)

        
        self.logo = PhotoImage(file="logo.png")
        self.LoginCanvas.create_image(1000,300, image=self.logo)

        
        self.LoginCanvas.create_text(900,420,text="Login",font=("Arial",12,"bold"),fill="white")
        self.LoginUser = Entry(self.LoginCanvas,width=20,highlightcolor="blue")
        self.LoginCanvas.create_window(1000,420,window=self.LoginUser)
        self.LoginCanvas.create_text(900,480,text="Senha",font=("Arial",12,"bold"),fill="white")
        self.SenhaUser = Entry(self.LoginCanvas,width=20,highlightcolor="blue",show="*")
        self.LoginCanvas.create_window(1000,480,window=self.SenhaUser)
        self.ButtonAccept = Button(self.LoginCanvas,text="ENTRAR",width=10,bg="#4682B4",fg="black",relief=RAISED,command=self.verificaLogin)
        self.LoginCanvas.create_window(1000,550,window=self.ButtonAccept)
        
        self.ButtonAccept.bind("<Enter>", self.hoverIn)
        self.ButtonAccept.bind('<Leave>', self.hoverOut)
      

        mainloop()

    def hoverIn(self, event):
           event.widget.config(bg="#1E90FF",fg="white")

    def hoverOut(self, event):
            event.widget.config(bg="#4682B4", fg="black")
         

    def verificaCargo(self, cargo):

        if cargo == 'GERENTE':
            print('IMPORTA TELA GERENTE')
            from Tela_Recepcao import Recepcao
            return Recepcao.startJan(self)
        if cargo == 'MECANICO':
            print('IMPORTA TELA MECANICO')
            # return 'TELA_INICIAL_MECANICO'
        if cargo == 'RECEPCIONISTA':
            print('IMPORTA TELA RECEPCAO')
            # return 'TELA_INICIAL_RECEPCIONISTA'


    def verificaLogin(self):
        user = self.loginEnt.get()
        password = self.senhaEnt.get()
        row = searchLogin(user, password)
        for columns in row:
            pickLogin = columns[4]
            pickSenha = columns[5]
            pickCargo = columns[3]
        messagebox.showinfo('INFO:', f'SENHA = {pickSenha}\nLOGIN = {pickLogin}\nCARGO = {pickCargo}')
        return self.verificaCargo(pickCargo)

minhaTela = Tela_de_Login()
=======
from tkinter import *

class Tela_de_Login:
    def __init__(self):
        self.janela = Tk()
        self.janela.minsize(width=1200,height=600)
        self.janela.title("Sistema Automotivo Soluções")
        self.janela.resizable(False,False)
        self.LoginCanvas = Canvas(self.janela, width = 500, height=370)
        self.LoginCanvas.pack(expand=1,fill=BOTH)
        self.janela.state("zoomed")
     

        self.Back = PhotoImage(file="back.png")
        self.LoginCanvas.create_image(700,350,image=self.Back)

        
        self.logo = PhotoImage(file="logo.png")
        self.LoginCanvas.create_image(1000,300, image=self.logo)

        
        self.LoginCanvas.create_text(900,420,text="Login",font=("Arial",12,"bold"),fill="white")
        self.LoginUser = Entry(self.LoginCanvas,width=20,highlightcolor="blue")
        self.LoginCanvas.create_window(1000,420,window=self.LoginUser)
        self.LoginCanvas.create_text(900,480,text="Senha",font=("Arial",12,"bold"),fill="white")
        self.SenhaUser = Entry(self.LoginCanvas,width=20,highlightcolor="blue",show="*")
        self.LoginCanvas.create_window(1000,480,window=self.SenhaUser)
        self.ButtonAccept = Button(self.LoginCanvas,text="ENTRAR",width=10,bg="#4682B4",fg="black",relief=RAISED,command=self.verificaLogin)
        self.LoginCanvas.create_window(1000,550,window=self.ButtonAccept)
        
        self.ButtonAccept.bind("<Enter>", self.hoverIn)
        self.ButtonAccept.bind('<Leave>', self.hoverOut)
      

        mainloop()

    def hoverIn(self, event):
           event.widget.config(bg="#1E90FF",fg="white")

    def hoverOut(self, event):
            event.widget.config(bg="#4682B4", fg="black")
        
        

    def verificaLogin(self):
        return

minhaTela = Tela_de_Login()
>>>>>>> a61989a68e483bf4048d714092312fcfae0a4022