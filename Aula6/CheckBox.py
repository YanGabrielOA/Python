from tkinter import *

tela = Tk()

tela.title("Cadastro de Clientes")
tela.config(background="#0A0E32", borderwidth=10)  # Fundo azul royal escuro
tela.geometry("800x600")
tela.resizable(False, False)

def show():
    Label(tela,text=var.get()).pack()
var = StringVar()

chkButton = Checkbutton(tela,text="Check Box", variable= var, onvalue="On", offvalue="Off")
chkButton.deselect()
chkButton.pack()

Button(tela,text="Show Me",command=show).pack()


tela.mainloop()