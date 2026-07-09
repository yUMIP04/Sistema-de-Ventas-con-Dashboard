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
        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS Usuarios( 
                       id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre_usuario VARCHAR,
                       clave VARCHAR(8)
                       )
                       ''')
        
        cursor.execute('''
                       
                       CREATE TABLE IF NOT EXISTS ArchivosPDF(
                       id_archivos_PDF INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre_archivo VARCHAR,
                       fecha DATE,
                       total_productos_vendidos INTEGER,
                       total_ventas REAL,
                       promedio_ventas REAL,
                       categoriaMax_ingresos VARCHAR,
                       nombre_creador VARCHAR,
                       id_usuario INTEGER,
                       FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)

                       )''')
        
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
        
        conexion.commit()
        conexion.close()
        
        print(f"☑️ Se inserto correctamente el usuario {nombre_usuario} con su clave {clave}")
        
    except Exception as e:
        print(f"Hubo un error {e}")

#🌟INSERTAR ARCHIVO CSV

def insert_PDFinfo(nombre_archivo, fecha, total_productos_vendidos, total_ventas, promedio_ventas, categoriaMax_ingresos, nombre_creador):

    conexion = Create_DB()
    cursor = conexion.cursor()

    try:

        cursor.execute('''
                       INSERT INTO ArchivosPDF (nombre_archivo,fecha,total_productos_vendidos, total_ventas, promedio_ventas, categoriaMax_ingresos, nombre_creador ) VALUES (?,?,?,?,?,?,?)''', (nombre_archivo, fecha, total_productos_vendidos, total_ventas, promedio_ventas, categoriaMax_ingresos, nombre_creador))
        
        conexion.commit()
        conexion.close()
        print(f"🥳 Se inserto correctamente el archivo {nombre_archivo}\n fecha:{fecha}\n total productos vendidos:{total_productos_vendidos} \n total ventas: {total_ventas} \n promedio ventas: {promedio_ventas} \n categoria con mas ingresos: {categoriaMax_ingresos} \n nombre creador: {nombre_creador} en la tabla")
        
    except Exception as e:

        print(f"❌Hubo un error al insertar el archivo CSV: {e}") 

#🌟MOSTRAR PDF EN HISTORIAL

def get_PDFs():

    conexion = Create_DB()
    cursor = conexion.cursor()

    try:

        cursor.execute('SELECT nombre_archivo, fecha, nombre_creador FROM archivosPDF')

        resultados = cursor.fetchall()
        return resultados

    except Exception as e:

        print(f"❌ Hubo un error al obtener de la BD la informacion de los pdfs {e}")
        return []
    
    finally:
        cursor.close()
        conexion.close()


#🌟VER PDF

def get_namePDF():

    conexion = Create_DB()
    cursor = conexion.cursor()

    try:

        cursor.execute('SELECT nombre_archivo FROM archivosPDF')

        resultados = cursor.fetchall()

        lista_nombre = []

        for names in resultados:

            for name_pdf in names:

                lista_nombre.append(name_pdf)

        return lista_nombre
    
    except Exception as e:

        print(f"❌ Hubo un error al ver los nombres de los pdfs")
        return []

    finally:
        conexion.close()

#🌟ELIMINAR PDF

def Delete_PDF(nombre):

    conexion = Create_DB()
    cursor =conexion.cursor()

    try:

        cursor.execute('DELETE FROM archivosPDF WHERE nombre_archivo = ?',(nombre,))

        conexion.commit()
       

        print("🥳 Se elimino correctamente la informacion del archivo")

        return True
    except Exception as e:

        print(f"❌Hubo un error al eliminar la informacion del archivo de la BD: {e}")

        return False

    finally:
         conexion.close()

#🌟FILTRAR POR FECHA

def fecha_PDF(fecha):

    conexion = Create_DB()
    cursor = conexion.cursor()
    try:

        cursor.execute('SELECT nombre_archivo, fecha, nombre_creador FROM archivosPDF WHERE fecha = ?', (fecha,))

        resultados = cursor.fetchall()

        lista_fechas = []

        for fechas_pdf in resultados:

            lista_fechas.append(fechas_pdf)

        return lista_fechas
            
    except Exception as e:
       print(f"Hubo un error al mostrar las fechas de la bd: {e}")

       return []
    

#🌟FILTRAR POR CREADOR

def Filtrar_CreadorPDF(nombre_creador):

    conexion = Create_DB()
    cursor = conexion.cursor()

    try:

        cursor.execute('SELECT nombre_archivo, fecha, nombre_creador FROM archivosPDF WHERE nombre_creador = ? ', (nombre_creador,))

        resultados = cursor.fetchall()

        lista_nombresCreador = []

        for nombre_creador in resultados:

            lista_nombresCreador.append(nombre_creador)

        return lista_nombresCreador
    
    except Exception as e:

        print(f"❌ Hubo un error al extraer los datos del creador en la BD")

        return []
    
    finally:

        conexion.close()
        print("🌟Finalizo la conexion con la BD")

#🌟FILTRAR POR NOMBRE_ARCHIVO

def Filtrar_nombreArchivo(nombre_archivo):

    conexion = Create_DB()
    cursor = conexion.cursor()

    try:

        cursor.execute('SELECT nombre_archivo, fecha, nombre_creador FROM archivosPDF WHERE nombre_archivo = ?', (nombre_archivo,))

        resultados = cursor.fetchall()
        Lista_nombreArchivos = []

        for nombre_archivo in resultados:

            Lista_nombreArchivos.append(nombre_archivo)

        return Lista_nombreArchivos
    
    except Exception as e:

        print(f"❌Hubo un error al obtener el nombre del archivo en la BD")

    finally:

        conexion.close()
        print("🌟Finalizo la conexion con la BD")


#🌟MOSTRAR USUARIOS

def get_usuarios():

    conexion = Create_DB()
    cursor = conexion.cursor()

    try:
        cursor.execute('SELECT nombre_usuario FROM Usuarios')

        resultados = cursor.fetchall()
        Lista_Usuarios = []

        for usuario in resultados:

            Lista_Usuarios.append(usuario)

        return Lista_Usuarios
    
    except Exception as e:

        print(f"Hubo un error al extraer la informacion de los usuarios de la BD: {e}")
        return []    
    
#🌟 ELIMINAR USUARIO

def Eliminar_Usuario(nombre):

    conexion = Create_DB()
    cursor = conexion.cursor()

    try:

        cursor.execute('DELETE FROM Usuarios WHERE nombre_usuario = ?', (nombre,))

        conexion.commit()

    except Exception as e:

        print(f"❌ Hubo un error al eliminar el usuario de la BD: {e}")

    finally:

        conexion.close()
        
#🌟LOGUEAR USUARIO

def loguear_user(nombre):
    
    conexion = Create_DB()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("SELECT id_usuario, nombre_usuario, clave FROM Usuarios WHERE nombre_usuario = ?",(nombre,))
        
        resultado = cursor.fetchone()

        return resultado
        
    except Exception as e:
        print(f"Hubo un error al loguear usuario: {e}")
        
    
    finally:
        conexion.close()

