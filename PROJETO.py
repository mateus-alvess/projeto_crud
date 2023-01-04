import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0202',
    database='bd_youtube'
)
cursor = conexao.cursor()
#crud

#CREATE
Nome_produto = ""
Valor = 30
comando = f'INSERT INTO vendas (Nome_produto , Valor) VALUES ("{Nome_produto}", {Valor})'
cursor.execute(comando)
conexao.commit() #edita o banco de dados

#READ
#comando = f'SELECT * FROM vendas;'
#cursor.execute(comando)
#resultado =cursor.fetchall()#ler o banco de dados
#print(resultado)

#UPDATE
#Nome_produto = "toddynho"
#Valor =6
#comando = f'UPDATE vendas SET Valor = {Valor} WHERE Nome_produto = "{Nome_produto}"'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados


#DELETE
#Nome_produto = "toddynho"
#comando = f'DELETE FROM vendas  WHERE Nome_produto = "{Nome_produto}"'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados

#final do codido
cursor.close()
conexao.close()