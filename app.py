from re import template
from flask import Flask, request,jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

# from sqlalchemy.sql.schema import PrimaryKeyConstraint


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///logindb.sqlite3'
app.config['SECRET_KEY']="randon string"

db=SQLAlchemy(app)

class logindb(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(100))
    lastname=db.Column(db.String(100))
    email=db.Column(db.String(100))
    password=db.Column(db.String(100))

def __init__(self, firstname, lastname, email, password):
    self.firstname=firstname
    self.lastname=lastname
    self.email=email
    self.password=password

db.create_all()
logindb = logindb.query.all()

@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html' )
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        # firstname=request.form['fname']
        # lastname=request.form['lname']
        # email=request.form['email']
        # password=request.form['password']
        data1 = logindb(firstname=request.form['fname'], lastname=request.form['lname'],
            email=request.form['email'], password=request.form['password'])
        db.session.add(data1)
        db.session.commit()
                #return render_template('home.html')
        msg="Signup Successfully"
        return redirect(url_for('home'))
    return render_template("Signup_page.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        return redirect(url_for('home'))
        #return render_template("home.html")
    return render_template("login_page.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/forgot')
def forgot():
    return render_template("Signup_page")

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)
