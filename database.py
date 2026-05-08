import sqlite3

#🌟 CREAR DB
def Create_DB():
    
    db = sqlite3.connect('AnalisisVentas.db')
    
    return db


#🌟 CREAR TABLA
def Create_Tables():
    
    conexion = Create_DB()
    
    cursor = conexion.cursor()
    
    try:
        
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS Usuarios( 
                       id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre_usuario VARCHAR,
                       clave VARCHAR(8)
                       )
                       ''')
        
        conexion.commit()
        conexion.close()
        
        print("📋 Se creo la tabla")
        
    except Exception as e:
        
        print(f"Hubo un error: {e}")
  
#🌟 INSERTAR USUARIO
def insert_user(nombre_usuario, clave):
    
    conexion = Create_DB()
    cursor = conexion.cursor()
    
    try:
        
        cursor.execute('''
                   INSERT INTO Usuarios (nombre_usuario, clave)
                   VALUES (?, ?) 
                   ''',(nombre_usuario, clave))
        
        print(f"☑️ Se inserto correctamente el usuario {nombre_usuario} con su clave {clave}")
        
    except Exception as e:
        print(f"Hubo un error {e}")
        
#🌟LOGUEAR USUARIO

def loguear_user(nombre):
    
    conexion = Create_DB()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("SELECT clave FROM Usuarios WHERE nombre_usuario = ?",(nombre,))
        
        resultado = cursor.fetchone()
        return resultado
    except Exception as e:
        print(f"Hubo un error al loguear usuario: {e}")
        
loguear_user("victoria")