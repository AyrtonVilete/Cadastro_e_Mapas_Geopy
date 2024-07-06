from functools import cmp_to_key
from tkinter import *
from geopy.geocoders import Nominatim
import folium
import webbrowser
import os
import tkinter.messagebox as tkMessageBox
import sqlite3

root = Tk()
root.title("Formulário de registro do estacionamento")

#=======================================TELA PRINCIPAL================================

width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#=======================================VARIABLES=====================================

CNPJ = StringVar()
ENDERECO = StringVar()
NOME = StringVar()
SENHA = StringVar()
VAGA = StringVar()

#=======================================METHODS=======================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, cnpj TEXT, endereco TEXT, nome TEXT, senha TEXT, vaga TEXT)")


def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Register():
    Database()
    if CNPJ.get == "" or ENDERECO.get() == "" or NOME.get() == "" or SENHA.get == "" or VAGA.get == "":
        lbl_result.config(text="Por favor, complete o formulário!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `cnpj` = ?", (CNPJ.get(),))
        if cursor.fetchone() is not None:
            lbl_result.config(text="CNPJ já existente", fg="red")
        else:
            cursor.execute("INSERT INTO `member` (cnpj, endereco, nome, senha, vaga) VALUES(?, ?, ?, ?, ?)", (str(CNPJ.get()), str(ENDERECO.get()), str(NOME.get()), str(SENHA.get()), str(VAGA.get())))
            conn.commit()
            CNPJ.set("")
            ENDERECO.set("")
            NOME.set("")
            SENHA.set("")
            VAGA.set("")
            lbl_result.config(text="Enviado com sucesso!", fg="green")
        cursor.close()
        conn.close()

def abrir_tela_principal():
    root.destroy()
    os.system("python Tela_principal.py")


#=====================================FRAMES====================================
TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)
RegisterFrame.pack(side=LEFT, pady=20)



#=====================================LABEL WIDGETS=============================
lbl_title = Label(TitleFrame, text="Formulário de registro", font=('arial', 18), bd=1, width=640)
lbl_title.pack()
lbl_cnpj = Label(RegisterFrame, text="CNPJ:", font=('arial', 18), bd=18)
lbl_cnpj.grid(row=1)
lbl_endereco = Label(RegisterFrame, text="Endereço do estacionamento:", font=('arial', 18), bd=18)
lbl_endereco.grid(row=2)
lbl_nome = Label(RegisterFrame, text="Nome do responsável:", font=('arial', 18), bd=18)
lbl_nome.grid(row=3)
lbl_senha = Label(RegisterFrame, text="Criar senha:", font=('arial', 18), bd=18)
lbl_senha.grid(row=4)
lbl_vaga = Label(RegisterFrame, text="Vagas disponíveis:", font=('arial', 18), bd=18)
lbl_vaga.grid(row=5)
lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
lbl_result.grid(row=6, columnspan=2)


#=======================================ENTRY WIDGETS===========================
cnpj = Entry(RegisterFrame, font=('arial', 20), textvariable=CNPJ, width=15)
cnpj.grid(row=1, column=1)
endereco = Entry(RegisterFrame, font=('arial', 20), textvariable=ENDERECO, width=15)
endereco.grid(row=2, column=1)
nome = Entry(RegisterFrame, font=('arial', 20), textvariable=NOME, width=15)
nome.grid(row=3, column=1)
senha = Entry(RegisterFrame, font=('arial', 20), textvariable=SENHA, width=15, show="*")
senha.grid(row=4, column=1)
vaga = Entry(RegisterFrame, font=('arial', 20), textvariable=VAGA, width=15)
vaga.grid(row=5, column=1)
#========================================BUTTON WIDGETS=========================
btn_register=Button(RegisterFrame, font=('arial', 20), text="Registrar", command=Register)
btn_register.grid(row=7, columnspan=2)

btn_registros = Button(root, text="Voltar", command=abrir_tela_principal)
btn_registros.pack()

#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


#========================================INITIALIZATION===================================
# Texto de copyright
lbl_copyright = Label(root, text="© 2024 Criadores: Ayrton, Gabriel, Julia & Tiago", bg="#f0f0f0")
lbl_copyright.pack(side="bottom")

if __name__ == '__main__':
    root.mainloop()
   
