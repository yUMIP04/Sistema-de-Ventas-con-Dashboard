from flask import Flask,redirect,url_for,render_template, request,flash
from database import Create_DB, Create_Tables, insert_user, loguear_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'victoria_secret_key'

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
              
                return redirect(url_for('Inicio_dashboard'))
            else:
                print("Contraseña incorrecta para este usuario.")
        else:
            print("El nombre de usuario no existe en la base de datos.")
      
      return render_template('inicio_sesion.html')


#🌟INICIO PAGINA

@app.route('/Inicio')

def Inicio_dashboard():

    return render_template('Inicio.html')

if __name__ == ('__main__'):
    app.run(debug=True)