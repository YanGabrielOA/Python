from tkinter import *

tela = Tk()

tela.title("Yan Gabriel")
tela.config(background="#ADD8E6",borderwidth=10)
tela.geometry("600x500")
tela.resizable(False,False)
#tela.maxsize(width=, height=1080)

lbl_nome = Label(tela,text="Nome: ",background="#34849e",font=("Arial Bold",16)).place(x=15,y=50)
lbl_telefone= Label(tela,text="Telefone: ",background="#34849e",font=("Arial",16)).place(x=15,y=100)
lbl_endereco = Label(tela,text="endereco: ",background="#34849e",font=("Arial",16)).place(x=15,y=150)
lbl_cpf = Label(tela,text="CPF: ",background="#34849e",font=("Arial",16)).place(x=15,y=200)


btn_botao = Button(tela, text="Clicar")
btn_botao.pack()

tela.mainloop()