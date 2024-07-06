import tkinter as tk
from tkinter import messagebox
import os

# Funções para os botões
def abrir_usuarios():
    root.destroy()
    os.system("python usuarios.py")

def abrir_registros():
    root.destroy()
    os.system("python index.py")

# Cria a janela principal
root = tk.Tk()
root.title("Tela Principal")
root.geometry("400x300")  # Defina o tamanho da janela conforme necessário

# Botões
btn_usuarios = tk.Button(root, text="Usuários", command=abrir_usuarios)
btn_usuarios.pack(pady=20)

btn_registros = tk.Button(root, text="Registros", command=abrir_registros)
btn_registros.pack()

# Texto de copyright
lbl_copyright = tk.Label(root, text="© 2024 Criadores: Ayrton, Gabriel, Julia & Tiago")
lbl_copyright.pack(side="bottom")

root.mainloop()