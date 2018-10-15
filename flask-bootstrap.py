# day2.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('flask-boot-home.html', var1='1', var2='2')

@app.route('/two')
def two():
    my_info = {
     'days': ['sun', 'mon', 'tues'],
     'flavors': ['sweet', 'sour'],
     'colors': ['blue', 'green', 'brown']
    }
    return render_template('flask-boot-home2.html', s_list = my_info)
