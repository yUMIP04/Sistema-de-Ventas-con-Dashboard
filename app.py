from flask import Flask,redirect,url_for,render_template
from database import Create_DB, Create_Tables
app = Flask(__name__)

Create_DB()
Create_Tables()
@app.route("/", methods=['GET', 'POST'])

def index():
    
    return render_template("index.html") 

if __name__ == ('__main__'):
    app.run(debug=True)