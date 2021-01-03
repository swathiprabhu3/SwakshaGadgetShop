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

class Register(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(20), nullable=False)
    password=db.Column(db.String(20),nullable=False)

class Payment(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    card = db.Column(db.Integer, nullable=True)
    cvv = db.Column(db.Integer, nullable=False)

class Specification(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(25), nullable=True)
    delivery = db.Column(db.String(25), nullable=False)
    

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

@app.route("/register", methods=["GET", "POST"])
def register():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        phone=request.form.get('phone')

        entry=Register(name=name,email=email,password=password,phone=phone)
        db.session.add(entry)
        db.session.commit()

    return render_template("register.html")

@app.route('/specification',methods=['GET','POST'])
def specification():
    if(request.method=='POST'):
        size=request.form.get('size')
        color=request.form.get('color')
        delivery=request.form.get('delivery')
        

        entry=Specification(size=size,color=color,delivery=delivery)
        db.session.add(entry)
        db.session.commit()
    return render_template('specification.html')

@app.route('/payment',methods=['GET','POST'])
def payment():
    if(request.method=='POST'):
        name=request.form.get('name')
        card=request.form.get('card')
        cvv=request.form.get('cvv')
       
        
        entry=Payment(name=name,card=card,cvv=cvv)
        db.session.add(entry)
        db.session.commit()

    return render_template('payment.html')

@app.route('/category',methods=['GET','POST'])
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
