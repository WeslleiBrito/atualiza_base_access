import sqlite3 as sql
caminho_banco = r"D:\Usuário\wesll\Desktop\base_precos.db"
banco = sql.connect(caminho_banco)
cursor = banco.cursor()

tabela = cursor.execute("SELECT * FROM sub_grupos")

print(tabela.fetchall())

