import pyodbc

def verificar_credenciales(username, password):
    # Parámetros de conexión
    server = 'gsvwdb17\sql2014'
    database = 'Pruebas3'
    uid = 'gsvreportes'
    pwd = 'Ind2019&'

    # Cadena de conexión
    conn_str = f'Driver={{SQL Server}};Server={server};Database={database};UID={uid};PWD={pwd};Trusted_Connection=no;'

    try:
        # Establecer conexión
        conn = pyodbc.connect(conn_str)

        # Crear cursor
        cursor = conn.cursor()

        # Consulta para verificar las credenciales
        query = f"SELECT id_usuario FROM seguridad_usuarios WHERE id_usuario=? AND password=?"
        cursor.execute(query, (username, password))

        # Obtener el resultado de la consulta
        result = cursor.fetchone()

        # Cerrar cursor y conexión
        cursor.close()
        conn.close()

        # Verificar si se encontraron resultados
        if result:
            return True  # Credenciales válidas
        else:
            return False  # Credenciales inválidas

    except pyodbc.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return False  # Tratar como credenciales inválidas en caso de error