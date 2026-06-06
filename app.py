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
    
    if request.method == 'POST':

       archivo_csv = request.files['file-csv']
       filtro_fecha_inicio = request.form['filtro_fecha_inicio']
       filtro_fecha_fin = request.form['filtro_fecha_fin']
       filtro_producto = request.form['filtro_producto']
       filtro_categoria = request.form['filtro_categoria']

       if archivo_csv and archivo_csv.filename != '':
           
           carpeta_csv = os.path.join(app.root_path, 'static', 'uploads', 'CSV')
           if not os.path.exists(carpeta_csv):
               
               os.makedirs(carpeta_csv)

           ruta_final = os.path.join(carpeta_csv, archivo_csv.filename)

           archivo_csv.save(ruta_final)
           insert_csv(archivo_csv.filename)

           print("🌟 Archivo insertado correctamente")

           ProcesamientoDatos_CSV(ruta_final)
           graf_pastel, graf_lineas, graf_barras = Create_Graficas(ruta_final, filtro_fecha_inicio, filtro_fecha_fin, filtro_categoria, filtro_producto)

           
       else:
           print("❌ El usuario envio el formulario pero no selecciono ningun archivo")
    
    return render_template('Inicio.html', pastel=graf_pastel, lineas=graf_lineas, barras=graf_barras, filtro_fecha_inicio=filtro_fecha_inicio, filtro_fecha_fin = filtro_fecha_fin, filtro_categorias=filtro_categoria, filtro_producto=filtro_producto)


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