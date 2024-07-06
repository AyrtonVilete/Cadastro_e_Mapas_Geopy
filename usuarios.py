import tkinter as tk
from tkinter import messagebox
import os
import sqlite3
from functools import cmp_to_key
from tkinter import *
from geopy.geocoders import Nominatim
import coordenadas
import folium
import webbrowser
import os
import tkinter.messagebox as tkMessageBox
import sqlite3

def Database():
    global conn, cursor
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, cnpj TEXT, endereco TEXT, nome TEXT, senha TEXT, vaga TEXT)")

def abrir_tela_principal():
    root.destroy()
    os.system("python Tela_principal.py")

def criar_mapa(latitude, longitude):
    return folium.Map(location=[latitude, longitude], zoom_start=12)

# Função para salvar os dados do usuário
def salvar_usuario():
    # Conectando ao Banco de Dados com os endereços
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()

    # Recupera dados de localização do banco de dados
    cursor.execute("SELECT endereco, nome, vaga FROM member")
    locations = cursor.fetchall()

    geolocator = Nominatim(user_agent="my_geocoder")

    # Entrada de dados
    nome_usuario = entry_nome.get()
    senha = entry_senha.get()
    endereco = entry_endereco.get()

    if not nome_usuario or not senha or not endereco:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    else:
        messagebox.showinfo("Sucesso", "Usuário salvo com sucesso!")

    # Converte o endereço do usuário para coordenada
        geolocator = Nominatim(user_agent="my_geocoder")
        location = geolocator.geocode(endereco)
        if location:
            latitude, longitude = location.latitude, location.longitude
            # Criar o mapa usando a função criar_mapa e as coordenadas do usuário
            m = criar_mapa(latitude, longitude)

             # Para cada localização, converte o endereço em coordenadas e adiciona um marcador ao mapa
            for loc in locations:
                latitude, longitude = coordenadas.obter_coordenadas(loc[0])
                if latitude and longitude:
                    folium.Marker([latitude, longitude], tooltip=f'{loc[1]} - Número de vagas:{loc[2]}').add_to(m)

    # Fecha a conexão com o banco de dados
    conn.close()

    # Salva o mapa em um arquivo HTML
    filepath = 'mapa.html'
    m.save(filepath)

   
    webbrowser.open('file://' + os.path.realpath(filepath))
 
#============================================================================================
# Cria a janela principal
root = tk.Tk()
root.title("Cadastro de Usuário")
root.geometry("640x480")  # Define o tamanho da janela

# Estilo visual
root.configure(bg="#f0f0f0")  # Cor de fundo

# Campos de entrada
label_nome = tk.Label(root, text="Nome de Usuário:", bg="#f0f0f0")
entry_nome = tk.Entry(root, bg="white")
label_nome.pack(pady=10)
entry_nome.pack()

label_senha = tk.Label(root, text="Senha:", bg="#f0f0f0")
entry_senha = tk.Entry(root, show="*", bg="white")  # Para ocultar a senha
label_senha.pack()
entry_senha.pack()

label_endereco = tk.Label(root, text="Seu Endereço:", bg="#f0f0f0")
entry_endereco = tk.Entry(root, bg="white")
label_endereco.pack()
entry_endereco.pack()

#==========================================BUTTON==================================================
# Botão para salvar os dados
btn_salvar = tk.Button(root, text="Mapa", command=salvar_usuario, bg="#007acc", fg="white")
btn_salvar.pack(pady=20)

btn_registros = tk.Button(root,  text="Voltar", command=abrir_tela_principal)
btn_registros.pack()
#==================================================================================================
# Texto de copyright
lbl_copyright = tk.Label(root, text="© 2024 Criadores: Ayrton, Gabriel, Julia & Tiago", bg="#f0f0f0")
lbl_copyright.pack(side="bottom")

root.mainloop()