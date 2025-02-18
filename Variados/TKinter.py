import tkinter as tk
def mude():
    mensagem = "BOTAO CLICADO"
        

janela = tk.Tk()
mensagem = ""
msg = tk.Label(janela,textvariable=mensagem)
msg.pack()
janela.title("JanelaPrincipal")
botao = tk.Button(janela,text="Botão1",command=mude())
botao.pack()


janela.mainloop()