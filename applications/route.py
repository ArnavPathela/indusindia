from flask import render_template
from main import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about_us')
def aboutus():
    return render_template('about_us.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/products')
def products():
    return render_template('products.html')
@app.route('/why_us')
def whyus():
    return render_template('why_us.html')