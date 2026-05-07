import sqlite3

def Create_DB():
    
    db = sqlite3.connect('AnalisisVentas.db')
    
    return db


def Create_Tables():
    
    conexion = Create_DB()
    
    cursor = conexion.cursor()
    
    try:
        
        cursor.execute('''
                       id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre_usuario VARCHAR,
                       contraseña VARCHAR(8)
                       ''')
        
        conexion.commit()
        conexion.close()
        
        print("📋 Se creo la tabla")
        
    except Exception as e:
        
        print(f"Hubo un error: {e}")