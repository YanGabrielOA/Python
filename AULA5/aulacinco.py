from tkinter import *
tela = Tk()


txt_nome = Entry(tela,width=50, fg="black", bg="#C9A66B")
txt_nome.pack()
txt_nome.insert(0,"Insira seu nome aqui")     

def clicar():
    lbl_nome = Label(tela, text="BEM VINDO"+ txt_nome.get())
    lbl_nome.pack()

btn_botao = Button(tela, text="Clique",command=clicar)
btn_botao.pack()

tela.mainloop()