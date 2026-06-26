from flask import Flask,redirect,url_for,render_template, request,flash,session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os 
import datetime
import jwt

from database import Create_DB, Create_Tables, insert_user, loguear_user, insert_csv
from aux_pandas import ProcesamientoDatos_CSV
from graficas import Create_Graficas
from Generacion_PDF import Generar_PDF
from middlewares.auth import token_required


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
SecretKey_JWT = os.getenv("SECRET_KEYJWT")

load_dotenv()
Create_DB()
Create_Tables()

@app.route("/", methods=['GET', 'POST'])

#🌟REGISTRO
def index():  
    
    if request.method == 'POST':
        
        nombre_usuario = request.form['nombre']
        clave = request.form['clave']
        
        if nombre_usuario and clave:
            
            clave_hasheada = generate_password_hash(clave)
            
            insert_user(nombre_usuario, clave_hasheada)

            return redirect(url_for('inicio_sesion'))
        
    return render_template("index.html") 

#🌟INICIO DE SESION
@app.route("/login", methods=['GET', 'POST'])
def inicio_sesion():
      
      if request.method == 'POST':
        nombre = request.form.get('nombre')
        clave_txt = request.form.get('clave')

        loguear = loguear_user(nombre)

        if loguear is not None:
            clave_hash = loguear[2]

            if check_password_hash(clave_hash, clave_txt):
                print("¡Inicio de sesión exitoso! Redirigiendo...")

                session['nombre_usuario'] = nombre

                token = jwt.encode({"usuario_id": loguear[0], "Nombre_Usuario": loguear[1]},SecretKey_JWT, algorithm="HS256" )

                return redirect(url_for('Inicio_dashboard', token=token))
            else:
                print("Contraseña incorrecta para este usuario.")
        else:
            print("El nombre de usuario no existe en la base de datos.")
      
      return render_template('inicio_sesion.html')


#🌟INICIO PAGINA


@app.route('/Inicio', methods=['GET', 'POST'])
@token_required

def Inicio_dashboard():

    filtro_fecha_inicio = ""
    filtro_fecha_fin = ""
    filtro_producto = ""
    filtro_categoria = ""
    graf_pastel = ""
    graf_lineas = ""
    graf_barras = "" 

    total_ventas_dinero = 0.0
    total_productos_vendidos = 0
    ticket_promedio = 0.0
    categoria_MaxIngresos = ""

    archivo_actual = session.get('archivo_actual', '')
    total_ventas_dinero = session.get('total_ventas_dinero', 0.0)
    total_productos_vendidos = session.get('total_productos_vendidos', 0)
    ticket_promedio = session.get('ticket_promedio', 0.0)
    categoria_MaxIngresos = session.get('categoria_MaxIngresos', '')

    if request.method == 'POST':

        if 'btn-buscar' in request.form:

            filtro_fecha_inicio = request.form.get('filtro_fecha_inicio')
            filtro_fecha_fin = request.form.get('filtro_fecha_fin')
            filtro_producto = request.form.get('filtro_producto', '').lower()
            filtro_categoria = request.form.get('filtro_categoria', '').lower()

            if archivo_actual:
                carpeta_csv = os.path.join(app.root_path, 'static', 'uploads', 'CSV')
                ruta_final = os.path.join(carpeta_csv, archivo_actual)


                graf_pastel, graf_lineas, graf_barras,total_ventas_dinero, total_productos_vendidos, ticket_promedio, categoria_MaxIngresos = Create_Graficas(ruta_final, filtro_fecha_inicio, filtro_fecha_fin, filtro_categoria, filtro_producto)

            else:
                print("Intentaste filtrar pero no se ha subido algun archivo CSV todavia")
                
        elif 'btn-limpiar' in request.form:
            filtro_fecha_inicio = ""
            filtro_fecha_fin = ""
            filtro_producto = ""
            filtro_categoria = ""

            if archivo_actual:
                carpeta_csv = os.path.join(app.root_path, 'static', 'uploads', 'CSV')
                ruta_final = os.path.join(carpeta_csv, archivo_actual)


                graf_pastel, graf_lineas, graf_barras,total_ventas_dinero, total_productos_vendidos, ticket_promedio, categoria_MaxIngresos = Create_Graficas(ruta_final, filtro_fecha_inicio, filtro_fecha_fin, filtro_categoria, filtro_producto)

            else:
                print("Intentaste filtrar pero no se ha subido algun archivo CSV todavia")

                

        elif 'file-csv' in request.files:

            archivo_csv = request.files['file-csv']

            if archivo_csv and archivo_csv.filename != '':

                carpeta_csv = os.path.join(app.root_path, 'static', 'uploads', 'CSV')

                if not os.path.exists(carpeta_csv):

                    os.makedirs(carpeta_csv)

                ruta_final = os.path.join(carpeta_csv, archivo_csv.filename)
                archivo_csv.save(ruta_final)
                insert_csv(archivo_csv.filename)

                session['archivo_actual'] = archivo_csv.filename

                total_ventas_dinero, total_productos_vendidos, ticket_promedio, categoria_MaxIngresos = ProcesamientoDatos_CSV(ruta_final)

                
                session['total_ventas_dinero'] = float(total_ventas_dinero)
                session['total_productos_vendidos'] = int(total_productos_vendidos)
                session['ticket_promedio'] = float(ticket_promedio)
                session['categoria_MaxIngresos'] = str(categoria_MaxIngresos)

                promedio_float = float(ticket_promedio)

                graf_pastel, graf_lineas, graf_barras, _, _, _, _ = Create_Graficas(ruta_final, filtro_fecha_inicio, filtro_fecha_fin, filtro_categoria)

            else:
                print("Formulario enviado pero sin archivo seleccionados")

        elif 'generar-pdf' in request.form:

            if archivo_actual:

                nombre_limpio = os.path.splitext(archivo_actual)[0]
                nombre_pdf = f"Reporte_{nombre_limpio}.pdf"

                fecha_resultados = datetime.datetime.now().strftime('%A' + " " + '%B' + " " + '%Y')

                total_ventas_dinero = session.get('total_ventas_dinero', 0.0)
                total_productos_vendidos = session.get('total_productos_vendidos', 0.0)
                ticket_promedio = session.get('ticket_promedio', 0.0)

                pdf_descarga = Generar_PDF(nombre_pdf, archivo_actual, fecha_resultados,total_ventas_dinero, total_productos_vendidos,ticket_promedio)

                if pdf_descarga:
                    return pdf_descarga
                
    return render_template('Inicio.html', totalVentas = total_ventas_dinero, totalProductosVendidos = total_productos_vendidos,
                           promedioVentas = ticket_promedio, categoriaMax = categoria_MaxIngresos, 
                           pastel=graf_pastel, lineas=graf_lineas, barras=graf_barras, filtro_fecha_inicio=filtro_fecha_inicio, 
                           filtro_fecha_fin = filtro_fecha_fin, filtro_categorias=filtro_categoria, filtro_producto=filtro_producto)


#🌟HISTORIAL

@app.route("/Historial", methods=['GET', 'POST'])

def Historial():

    return render_template("Historial.html")

#🌟BASE

@app.route('/Base')
@token_required

def Base():

    return render_template('Base.html')


#🌟CERRAR SESION

@app.route('/logout')


def logout():

    respuesta = redirect(url_for('inicio_sesion'))

    respuesta.delete_cookie('token')

    session.clear()

    return respuesta

if __name__ == ('__main__'):
    app.run(debug=True)