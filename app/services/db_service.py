from flask_mysqldb import MySQL
from app import mysql

def fetch_insemination_data(nome_fazenda=None):
    cursor = mysql.connection.cursor()
    
    if nome_fazenda:
        query = "SELECT * FROM inseminacao WHERE fazenda = %s"
        cursor.execute(query, (nome_fazenda,))
    else:
        query = "SELECT * FROM inseminacao"
        cursor.execute(query)
    
    records = cursor.fetchall()
    db_info = "\n".join([f"ID: {row[0]}, Data: {row[1]}, Valor: {row[2]}, Fazenda: {row[3]}" for row in records])
    cursor.close()
    return db_info

def get_inseminacao_by_fazenda(nome_fazenda):
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM inseminacao WHERE fazenda = %s"
    cursor.execute(query, (nome_fazenda,))
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

