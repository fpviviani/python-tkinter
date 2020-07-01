import tkinter as tk
from gui import buttons as b

class mainWindow:

    def __init__(self):
        self.window = tk.Tk()
        texto = ""
        self.initWidgets(self.window, texto)
        self.window.mainloop()

    def initWidgets(self, window, texto):
        self.title = self.window.title('Janela Principal')
        self.frameTopo = tk.Frame(self.window)
        self.frameBase = tk.Frame(self.window)
        self.frameInput = tk.Frame(self.window)
        self.frameMiddle = tk.Frame(self.window)

        self.label1 = tk.Label(self.frameTopo, text="Label do topo", font=("Arial Bold", 40))
        self.label2 = tk.Label(self.frameMiddle, text="Label da base", font=("Arial Bold", 20))
        self.label1.pack(side='top')
        self.label2.pack(side='left')

        self.frameTopo.pack()
        self.frameMiddle.pack()
        self.frameInput.pack()
        self.frameBase.pack()

        self.labelResult = tk.Label(self.frameInput, text=texto)
        self.labelResult.pack(side="left")

        self.commands = b.Commands()
        self.botao1 = tk.Button(self.frameBase, text="Entrar texto", command=lambda: self.commands.processaB1(self))
        self.botao2 = tk.Button(self.frameBase, text="Limpar", command=lambda: self.commands.clear(self))
        self.botao1.pack(side='left')
        self.botao2.pack(side='right')

    def removeWidgets(self):
        self.frameTopo.destroy()
        self.frameMiddle.destroy()
        self.frameInput.destroy()
        self.frameBase.destroy()
