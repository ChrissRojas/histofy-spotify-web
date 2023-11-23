from flask import render_template, flash, redirect, url_for, request, session
import spotipy
from app import app,sp_auth

scopes = sp_auth.scopes
spfy_oauth = sp_auth.SP_HANDLER(scopes,session)

@app.route('/')
@app.route('/index')
def index():
    user={}
    return render_template('index.html', login=user)

@app.route('/login', methods=['GET'])
def login():
    return redirect(spfy_oauth.get_auth_url())

@app.route('/api_callback')
def callback():
    # code = request.args.get('code')
    # session.clear()
    # tk_info = spfy_oauth.callback_token(code)
    # session['token_info'] = tk_info
    # # spotify=spotipy.Spotify(auth_manager=spfy_oauth.sp)
    # # print(spotify.me())
    # print(session['token_info'])
    # code = request.args.get('code')
    # if code:
        
    return redirect('/index')

@app.route('/logout', methods=['POST','GET'])
def logout():
    session.pop('token_info',None)
    return redirect('/index')

