import tkinter as tk
from tkinter import messagebox

def submit():
    nome = nome_entry.get()
    email = email_entry.get()

    # Verifica qual radiobutton está selecionado
    linguagem_preferida = linguagem_var.get()

    print ('Nome:', nome)
    print ('Email:', email)
    print ('Linguagem preferida:', linguagem_preferida)

    # Caixa de mensagem com os dados
    messagebox.showinfo(
        'Dados submetidos',
        f'Nome: {nome}\nEmail: {email}\nLinguagem Preferida: {linguagem_preferida}')

# Janela principal    
root = tk.Tk()
root.title ("Formulário")

# Frame dos widgets
frame = tk.Frame (root)
frame.pack (padx = 10, pady = 10)

# Campo de Nome
nome_label = tk.Label (frame, text = "Nome")
nome_label.grid (row = 0, column = 0, sticky = "e")
nome_entry = tk.Entry (frame)
nome_entry.grid (row = 0, column = 1)

# Campo de Email
email_label = tk.Label (frame, text = "Email")
email_label.grid (row = 1, column = 0, sticky = "e")
email_entry = tk.Entry (frame)
email_entry.grid (row = 1, column = 1)

# Variável que armazena a escolha da linguagem
linguagem_var = tk.StringVar (value = 'Python')

# radiobutton - 'Python'
python_radio = tk.Radiobutton (frame, text = 'Python', variable = linguagem_var, value = 'Python')
python_radio.grid (row = 2, column = 0)

# radiobutton - 'Java'
java_radio = tk.Radiobutton (frame, text = 'Java', variable = linguagem_var, value = 'Java')
java_radio.grid (row = 2, column = 1)

# Botão
submit_button = tk.Button (frame, text = "Salvar", command = submit)
submit_button.grid (row = 3, columnspan = 2, pady = 10)

# Inicia 
root.mainloop()