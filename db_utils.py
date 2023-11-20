## utils para db
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '', ## si es necesario
    'database': 'db_python'
}

def test_conect():
    try:
        cnx = mysql.connector.connect(
            host= db_config['host'],
            user= db_config['user'],
            password= db_config['password'], 
            database= db_config['database']
        )
        msj = f'Conexion OK {cnx}'
        print(msj)
        ## cerrar conexion
        cnx.close()
    except Exception as e:
        msj = f'No se pudo conectar a la base de datos: {e}'
        print(msj)

def run_query(query):
    cnx = mysql.connector.connect(
        host= db_config['host'],
        user= db_config['user'],
        password= db_config['password'], 
        database= db_config['database']
    )
    cursor = cnx.cursor()
    cursor.execute(query)
    data = []
    for row in cursor:
        data.append(row)
    cursor.close()    
    cnx.close() 
    return data

def query_example():
    query = "SELECT * FROM users"
    data = run_query(query)
    print(data)