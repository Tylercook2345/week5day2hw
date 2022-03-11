from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def iCanNameThisAnything():
    return render_template('about.html')


@app.route('/signup')
def signMeUp():
    return {'hi' : 'there'}


@app.route('/getUser')
def getUser():
    return {
        'name' : 'Tyler',
        'age' : '300',
        'email' : 'Doodieclipjr@CODleague'
    }