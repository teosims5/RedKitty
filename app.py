from crypt import methods
from flask import Flask, redirect, url_for

app = Flask(__name__)

app.config.from_object('config')

cookies_data = {
    'chocolate-chip' : {'name' : 'Chocolate Chip', 'price' : '€1.50'},
    'oatmeal-raisin' : {'name' : 'Oatmeal Raisin', 'price' : '€1.00'},
    'sugar' : { 'name' : 'Sugar', 'price' : '€0,75'},
    'peanut-butter' : {'name' : 'Peanut Butter', 'price' : '€0,50'},
    'oatmeal' : {'name' : 'Oatmeal', 'price' : '€0,25'},
    'salted-caramel' : {'name' : 'Salted Caramel', 'price' : '€1,00'}
}

@app.route('/', methods=['GET', 'POST'])
def index():
    return '''<h1>Hello World!</h1>
    <a href="/about">About Page</a>'''

@app.route('/about')
def about():
    return 'I like cookies'

@app.route('/about-me')
def about_me():
    return redirect(url_for('/about'))

@app.route('/cookies/<slug>')
def cookie(slug):
    return slug

def apprun ():
    if __name__ == '__main__':
        app.run()

app.run()

