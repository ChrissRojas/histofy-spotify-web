from flask import render_template, flash, redirect, url_for, request, session
import spotipy
from app import app

@app.route('/')
@app.route('/index')
def index():

    user = {}
    return render_template('index.html', login=user)

@app.route('/login', methods=['POST','GET'])
def login():
    return redirect('/index')

@app.route('/logout', methods=['POST','GET'])
def logout():
    return redirect('/index')