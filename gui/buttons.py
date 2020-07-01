import tkinter as tk

class Commands:

    def __init__(self):
        pass

    def processaB1(self, window):
        window.label1.configure(text="Entrada de texto")
        window.label2.configure(text="Digite algo:")
        window.inputText = tk.Entry(window.frameMiddle, width=20)
        window.inputText.pack(side="right")

        window.botaoEnviar = tk.Button(window.frameBase, text="Enviar", command=lambda: self.submit(window))
        window.botaoEnviar.pack(side='left')
        window.botao1.destroy() 

        window.botaoLimpar = tk.Button(window.frameBase, text="Voltar", command=lambda: self.returnMain(window))
        window.botaoLimpar.pack(side='right')
        window.botao2.destroy() 

    def processaB2(self, window):
        window.label2.configure(text="Botão 2 foi clicado")

    def submit(self, window):
        text = window.inputText.get()
        window.labelResult["text"] = text
        
    def clear(self, window):
        window.labelResult.destroy()

    def returnMain(self, window):
        text = window.inputText.get()
        window.removeWidgets()
        window.initWidgets(window.window, text)
