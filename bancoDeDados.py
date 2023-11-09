import sqlite3

#CREATE
#---------
# variável conn guarda instância de conexção com o banco
conn = sqlite3.connect('aulaDB.db')
# criar cursor para executar as instruções
cursor = conn.cursor()
cursor.execute("""
  INSERT INTO fornecedor (id_fornecedor, nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro) 
  VALUES ('Mathes LTDA', '11.111.111/0001-11', 'Salvador', 'BA', '40265-060', '29-08-2023')
""")
#grava as alterações com commit
conn.commit()

#READ
#------
cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()
for linha in resultado:
    print(linha)

#UPDATE
#------
cursor.execute("UPDATE fornecedor SET cidade='Belo Horizonte' WHERE id_fornecedor = 5")
conn.commit()

#DELETE
#------
cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = 2")
conn.commit()