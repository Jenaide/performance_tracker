from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#DATABASE MODEL
"""class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpNumber = db.Column(db.Integer(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)

class Tracker(db.Model):
    id = db.Column(db.Integer, foreignkey=True)
    ceoCredit = db.Column(db.Integer(200))
    creditCards = db.Column(db.Interger(200))
    insureTakeUp = db.Column(db.Interger(200))
    insureEst = db.Column(db.Interger(200))
    Do = db.Column(db.Interger(200))
    sim = db.Column(db.Interger(200))
    simRecharge = db.Column(db.Interger(200))
    apps = db.Column(db.Interger(200))
    lbsa = db.Column(db.Interger(200))
    qrCode = db.Column(db.Interger(200))
    cetsPerformed = db.Column(db.Interger(200))
    nonCreditTickets = db.Column(db.Interger(200))
    cetsDeclined = db.Column(db.Interger(200))
    appointments = db.Column(db.Interger(200))
    cetTakenUp = db.Column(db.Interger(200))"""
    

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add', methods=['POST'])
def add_item():
    return render_template('add.html')

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

# error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)