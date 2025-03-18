from tkinter import *

tela = Tk()

tela.title("Cadastro de Clientes")
tela.config(background="#0A0E32", borderwidth=10)  # Fundo azul royal escuro
tela.geometry("800x600")
tela.resizable(False, False)
#LABELS
lbl_nome = Label(tela, text="Nome: ", background="#4682B4", font=("Courier New", 18, "bold"), fg="white",width=10,anchor="w")
lbl_nome.place(x=15, y=48)

lbl_telefone = Label(tela, text="Telefone: ", background="#4682B4", font=("Courier New", 18, "bold"), fg="white",anchor="w",width=10)
lbl_telefone.place(x=15, y=98)

lbl_endereco = Label(tela, text="Endereço: ", background="#4682B4", font=("Courier New", 18, "bold"), fg="white",anchor="w",width=10)
lbl_endereco.place(x=15, y=148)

lbl_Email = Label(tela, text="Email: ", background="#4682B4", font=("Courier New", 18, "bold"), fg="white",width=10,anchor="w")
lbl_Email.place(x=15, y=198)

#INSERTS
txt_nome = Entry(tela,width=50,font="18",fg="white",bg="#4682B4")
txt_nome.place(x=180,y=50)


txt_telefone = Entry(tela,width=50,font="18",fg="white",bg="#4682B4")
txt_telefone.place(x=180,y=100)


txt_endereco = Entry(tela,width=50,font="18",fg="white",bg="#4682B4")
txt_endereco.place(x=180,y=150)

txt_email = Entry(tela,width=50,font="18",fg="white",bg="#4682B4")
txt_email.place(x=180,y=200)


#BOTOES
def Cadastrar():
    lbl_dados = Label(tela, background="#f1f1f1",font=("Courier New", 18, "bold"),fg="black",text="Nome:"+txt_nome.get()+"\nTelefone:"+txt_telefone.get()+"\nEndereco:"+txt_endereco.get()+"\nEmail:"+txt_email.get())
    lbl_dados.place(x=180,y=400)
btn_button = Button(tela,text="Cadastrar",command=Cadastrar,fg="white",bg="#4682B4",font=14,border="5",relief="ridge")
btn_button.place(x=400,y=300)



tela.mainloop()