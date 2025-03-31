from tkinter import *

tela = Tk()

tela.title("Cadastro de Clientes")
tela.config(background="#0A0E32", borderwidth=10)  # Fundo azul royal escuro
tela.geometry("800x600")
tela.resizable(False, False)

var = StringVar()
var.set("m")

rdb_buttonm = Radiobutton(tela, text="M",variable=var, value="m").place(x=20,y=40)
rdb_buttonf = Radiobutton(tela,text="F",variable=var,value="f").place(x=20,y=60)

tela.mainloop()