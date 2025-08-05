import tkinter as tk

janela = tk.Tk()
janela.geometry ('800x800')
mensagem = 'Faça coisas que você ama ❤️'



msg = tk.Message (janela, text = mensagem)
msg.config (bg = '#f5f5f5' , font = ('Shrikhand', 48), fg = '#ff1165')

msg.pack(expand = True, fill = 'both')

janela.mainloop()