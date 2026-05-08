from flask import Flask,redirect,url_for,render_template, request
from database import Create_DB, Create_Tables, insert_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

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
    
    return render_template('inicio_sesion.html')

if __name__ == ('__main__'):
    app.run(debug=True)