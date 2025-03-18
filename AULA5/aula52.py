from tkinter import *

tela = Tk()

tela.title("Yan Gabriel")
tela.config(background="#0A0E32", borderwidth=10)  # Fundo azul royal escuro
tela.geometry("600x500")
tela.resizable(False, False)

lbl_nome = Label(tela, text="Nome: ", background="#4682B4", font=("Courier New", 18, "bold"), fg="white")
lbl_nome.place(x=15, y=50)

lbl_telefone = Label(tela, text="Telefone: ", background="#4682B4", font=("Courier New", 18, "bold"), fg="white")
lbl_telefone.place(x=15, y=100)

lbl_endereco = Label(tela, text="Endereço: ", background="#4682B4", font=("Courier New", 18, "bold"), fg="white")
lbl_endereco.place(x=15, y=150)

lbl_cpf = Label(tela, text="CPF: ", background="#4682B4", font=("Courier New", 18, "bold"), fg="white")
lbl_cpf.place(x=15, y=200)



btn_botao = Button(tela, text="Clicar")
btn_botao.pack()
tela.mainloop()
