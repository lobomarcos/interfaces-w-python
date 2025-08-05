import tkinter as tk

''' REDIMENSIONÁVEL
janela = tk.Tk()
janela.title ('Aplicação GUI')

janela.mainloop()
'''

# NÃO REDIMENSIONÁVEL
janela = tk.Tk()
janela.title ('App GUI Não Redimensionável')
janela.resizable (False, False)

janela.mainloop()
