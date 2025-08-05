import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title ('Aplicação GUI com Label')

ttk.Label (janela, text = 'Componente Label').grid (row = 0, column = 0)

janela.mainloop()