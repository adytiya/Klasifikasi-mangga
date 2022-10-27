#from ensurepip import bootstrap

from flask import (Flask,render_template,request,
                   redirect,url_for,session,flash)
import mysql.connector
import os 
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
connection= mysql.connector.connect(host = 'localhost',
                                    port='3306',
                                    database='db_mangga',
                                    user='root',
                                    password='')
# from flask_mysqldb import MySQL;
# import bcrypt
cursor = connection.cursor()
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] ='mySQL://root: @localhost/' 
# app.config["MYSQL_HOST"]="localhost"
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']=''
# app.config['MYSQL_DB']="flaskdb"
# app.config['MYSQL_CURSORCLASS']='DictCrusor'
# mysql=MySQL(app)
app.secret_key="1234567890!@#$%^&*()"
app.run()

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
  
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.')

@app.route("/")
def home ():
    return redirect('login')
@app.route('/home')
def homepage():
    return render_template('/page/index.html')

@app.route("/login", methods=["POST",'GET'])
def login():
    msg=''
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']
        
        cursor.execute('SELECT * FROM user WHERE username=%s AND password=%s',(email,password)) 
        record = cursor.fetchone()
        if record:
            session['loggedin']= True
            session['username']=record[1]
            session['role']=record[4]
            return redirect(url_for('homepage'))
       
        else :
            msg="Username Atau Password salah"
    if 'username' in session:  
        return redirect(url_for('homepage'))
    return render_template('/page/login.html',msg=msg)


    

@app.route('/logout')
def logout():
    session.pop('loggenin',None)
    session.pop('username',None)
    return redirect(url_for('login'))

    #     return'ini adalah method post' + request.form['email']
    # session["username"] = request.form['email']
    
    # return render_template("/page/login.html")
# @app.route('/home')
# def home():
#     return render_template("/page/home.html",username=session['username'])

@app.route("/forgot")
def forgot():
    return render_template("/page/forgot-password.html")

@app.route("/button")
def button():
    return render_template("/page/buttons.html")

@app.route("/card")
def card():
    return render_template("/page/cards.html")

@app.route("/table")
def table():
    return render_template("/page/tables.html")
@app.route('/data',methods=['GET','POST'])
def data():
     
    return render_template('/page/data.html')

