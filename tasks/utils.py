import pyodbc

def verificar_credenciales(username, password):
    # Parámetros de conexión
    server = 'gsvwdb17\\sql2014'  # Doble barra para escapar correctamente la barra invertida
    database = 'Pruebas3'
    uid = 'gsvreportes'
    pwd = 'Ind2019&'

    # Cadena de conexión
    conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={uid};PWD={pwd};Trusted_Connection=no;'

    try:
        # Establecer conexión
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Consulta para verificar las credenciales
        query = "SELECT id_usuario FROM seguridad_usuarios WHERE id_usuario=? AND password=?"
        cursor.execute(query, (username, password))

        # Obtener el resultado de la consulta
        result = cursor.fetchone()

        # Cerrar cursor y conexión
        cursor.close()
        conn.close()

        # Verificar si se encontraron resultados
        return result is not None

    except pyodbc.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return False  # Tratar como credenciales inválidas en caso de error
