import sqlite3

# Conectando ao Banco de Dados
conn = sqlite3.connect("db_member.db")
cursor = conn.cursor()

# Recupera o nome de todas as tabelas no banco de dados
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

# Imprime o nome das tabelas
for tabela in tabelas:
    print(tabela[0])

# Fecha a conexão com o banco de dados
conn.close()
