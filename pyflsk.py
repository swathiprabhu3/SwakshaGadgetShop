from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/shoppingwebapp'
db = SQLAlchemy(app)


class Contacts(db.Model):
    ''' sno name email mes date                                  '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    mes = db.Column(db.String(120), nullable=False)
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
@app.route('/checkout')
def check():
    return render_template('checkout.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/sign-up')
def signup():
    return render_template('sign-up.html')
@app.route('/order')
def order():
    return render_template('order.html')
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
@app.route('/order_confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')
@app.route('/product')
def product():
    return render_template('product.html')



app.run(debug=True)