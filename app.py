from flask import Flask,redirect,url_for,render_template, request,flash,session
from database import Create_DB, Create_Tables, insert_user, loguear_user, insert_csv
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os 
from aux_pandas import ProcesamientoDatos_CSV
from graficas import Create_Graficas

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

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
        
    return render_template("index.html") 

#🌟INICIO DE SESION
@app.route("/login", methods=['GET', 'POST'])
def inicio_sesion():
      
      if request.method == 'POST':
        nombre = request.form.get('nombre')
        clave_txt = request.form.get('clave')

        loguear = loguear_user(nombre)

        if loguear is not None:
            clave_hash = loguear[0]

            if check_password_hash(clave_hash, clave_txt):
                print("¡Inicio de sesión exitoso! Redirigiendo...")

                session['nombre_usuario'] = nombre
                return redirect(url_for('Inicio_dashboard'))
            else:
                print("Contraseña incorrecta para este usuario.")
        else:
            print("El nombre de usuario no existe en la base de datos.")
      
      return render_template('inicio_sesion.html')


#🌟INICIO PAGINA

@app.route('/Inicio', methods=['GET', 'POST'])

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

    if request.method == 'POST':

        if 'btn-buscar' in request.form:

            filtro_fecha_inicio = request.form.get('filtro_fecha_inicio')
            filtro_fecha_fin = request.form.get('filtro_fecha_fin')
            filtro_producto = request.form.get('filtro_producto').lower()
            filtro_categoria = request.form.get('filtro_categoria').lower()

            if archivo_actual:
                carpeta_csv = os.path.join(app.root_path, 'static', 'uploads', 'CSV')
                ruta_final = os.path.join(carpeta_csv, archivo_actual)


                graf_pastel, graf_lineas, graf_barras = Create_Graficas(ruta_final, filtro_fecha_inicio, filtro_fecha_fin, filtro_categoria, filtro_producto)

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

                promedio_float = float(ticket_promedio)
                graf_pastel, graf_lineas, graf_barras = Create_Graficas(ruta_final, filtro_fecha_inicio, filtro_fecha_fin, filtro_categoria)

                
            else:
                print("Formulario enviado pero sin archivo seleccionados")
    
    return render_template('Inicio.html', totalVentas = total_ventas_dinero, totalProductosVendidos = total_productos_vendidos,
                           promedioVentas = ticket_promedio, categoriaMax = categoria_MaxIngresos, 
                           pastel=graf_pastel, lineas=graf_lineas, barras=graf_barras, filtro_fecha_inicio=filtro_fecha_inicio, 
                           filtro_fecha_fin = filtro_fecha_fin, filtro_categorias=filtro_categoria, filtro_producto=filtro_producto)


#🌟BASE

@app.route('/Base')

def Base():

    return render_template('Base.html')


#🌟CERRAR SESION

@app.route('/logout')
def logout():

    session.pop('nombre_usuario', None)

    return redirect(url_for('inicio_sesion'))

if __name__ == ('__main__'):
    app.run(debug=True)