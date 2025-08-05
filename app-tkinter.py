import tkinter as tk

def submit():
    # Pega os valores dos campos de entrada
    nome = nome_entry.get()
    email = email_entry.get()

    # Imprime os dados no console
    print ("Nome:", nome)
    print ("Email:", email)

# Janela principal
root = tk.Tk()
root.title("Formulário")

# Frame dos widgets
frame = tk.Frame(root)
frame.pack (padx = 10, pady = 10)

# Campo de Nome
nome_entry = tk.Entry(frame)
nome_entry.grid (row = 0, column = 1)

# Campo de Email
email_entry = tk.Entry(frame)
email_entry.grid (row = 1, column = 1)

# Botão
submit_button = tk.Button(frame, text = "Salvar", command = submit)
submit_button.grid (row = 2, columnspan = 2, pady = 10)

# Inicia 
root.mainloop()