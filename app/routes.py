from flask import render_template, flash, redirect, url_for, request, session
import spotipy
from app import app,sp_auth

scopes = sp_auth.scopes
spfy_oauth = sp_auth.SP_HANDLER(scopes)

@app.route('/')
@app.route('/index')
def index():

    user = {}
    return render_template('index.html', login=user)

@app.route('/login', methods=['POST','GET'])
def login():
    return redirect('/index')

@app.route('/api_callback')
def callback():
    code = request.args.get('code')
    spfy_oauth.callback_token(code)
    session.clear

@app.route('/logout', methods=['POST','GET'])
def logout():
    return redirect('/index')