import sqlite3
import csv

datas_movies = sqlite3.connect("filmesN.db")
cursor=datas_movies.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS filmesN(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Unnamed INTEGER,
    Titulo VARCHAR(150),
    Ano VARCHAR(100),
    País VARCHAR(50),
    Diretor VARCHAR(100),
    Elenco VARCHAR(100),
    Nota INTEGER,
    Tipo_de_filme VARCHAR(100),
    Gênero VARCHAR(100) 
)''')


file = open("filmaffinity_dataset.csv", encoding= "UTF-8")
#next(file)

conteudo = csv.reader(file)
next(file)
#inserir dados 
inserir_conteudo = "INSERT INTO filmesN(Unnamed,Titulo,Ano,País, Diretor,Elenco,Nota,Tipo_de_filme, Gênero)\
VALUES (?, ?, ?, ?, ?, ?,?,?,?)"
cursor.executemany(inserir_conteudo, conteudo)
selecionar_tudo = "SELECT * FROM filmesN"

entradas = cursor.execute(selecionar_tudo).fetchall()

datas_movies.commit()
datas_movies.close()