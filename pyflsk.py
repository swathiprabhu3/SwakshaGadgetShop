from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql 
pymysql.install_as_MySQLdb()


app = Flask(__name__)

    
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/shoppingwebapp"
db = SQLAlchemy(app)



class Contacts(db.Model):
    ''' sno name email mes date                                  '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    mes = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
class Checkout(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(12), nullable=False)
    address= db.Column(db.String(120), nullable=False)
    postcode= db.Column(db.String(20), nullable=False)
    city= db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(12), nullable=True)



@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/cart')
def cart():
    return render_template('cart.html')
@app.route('/checkout', methods= ['GET', 'POST'])
def check():
    if(request.method=='POST'):
        name=request.form.get('name')
        phone=request.form.get('phone')
        email=request.form.get('email')
        country=request.form.get('country')
        address=request.form.get('address')
        postcode=request.form.get('postcode')
        city=request.form.get('city')

        entry=Checkout(name=name,phone=phone,email=email, country=country,address=address,postcode=postcode,city=city,date=datetime.now())
        db.session.add(entry)
        db.session.commit()

    return render_template('checkout.html')
database={'nachi':'123','james':'aac','karthik':'asdsf'}
@app.route('/login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('index.html',name=name1)
@app.route("/sign-up", methods=["GET", "POST"])
def register():
 
    return render_template("sign-up.html")

@app.route('/category')
def category():
    return render_template('category.html')
@app.route('/product_detail')
def productdetail():
    return render_template('product_detail.html')
@app.route('/search')
def search():
    return render_template('search.html')
@app.route('/contact', methods= ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''add entry to database'''
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('msg')

        entry=Contacts(name=name,email=email, mes=message,date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')

@app.route('/product')
def product():
    return render_template('product.html')


app.run(debug=True)
