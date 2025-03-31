from tkinter import *
from time import *

nomes =[]
telefones = []
enderecos = []
emails = []
tela = Tk()
pagina = False

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
def criar_registro(window,I,posx,posy):
        
        lbl_dados = Label(window, background="#f1f1f1",font=("Courier New", 18, "bold"),fg="black",text="Nome:"+nomes[I]+"\nTelefone:"+telefones[I]+"\nEndereco:"+enderecos[I]+"\nEmail:"+emails[I])
        lbl_dados.place(x=posx,y=posy)
        posx +=(100*I)
        posy +=(100*I)
        
def Cadastrar():
    I = 0
    
    nomes.append(txt_nome.get())
    telefones.append(txt_telefone.get())
    enderecos.append(txt_endereco.get())
    emails.append(txt_email.get())
    if(pagina == False):
        tela_registro = Toplevel(tela)
        tela_registro.geometry("800x600")
        tela_registro.config(background="#0A0E32", borderwidth=10)
    pagina = True
    criar_registro(tela_registro,I,100,100)
    I+=1


    
    
btn_button = Button(tela,text="Cadastrar",command=Cadastrar,fg="white",bg="#4682B4",font=14,border="5",relief="ridge")
btn_button.place(x=400,y=300)




tela.mainloop()