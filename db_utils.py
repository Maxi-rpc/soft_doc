## utils para db
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'db_python'
}

def test_conect():
    try:
        cnx = mysql.connector.connect(
            host= db_config['host'],
            user= db_config['user'], 
            database= db_config['database']
        )
        msj = f'Conexion OK {cnx}'
        print(msj)
        ## cerrar conexion
        cnx.close()
    except Exception as e:
        msj = f'No se pudo conectar a la base de datos: {e}'
        print(msj)

def querys():
    cnx = mysql.connector.connect(
        host= db_config['host'],
        user= db_config['user'], 
        database= db_config['database']
    )
    cursor = cnx.cursor()

    query = ("SELECT * FROM users")
    cursor.execute(query)

    for (id, user, password) in cursor:
        print(f'user: {user} - pass: {password}')

    cursor.close()    
    cnx.close() 

def run_query(query):
    cnx = mysql.connector.connect(
        host= db_config['host'],
        user= db_config['user'], 
        database= db_config['database']
    )
    cursor = cnx.cursor()
    cursor.execute(query)
    data = []
    for row in cursor:
        data.append(row)
    cursor.close()    
    cnx.close() 
    if len(data) > 1:
        return data
    return data[0]
