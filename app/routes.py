from flask import render_template, flash, redirect, url_for, request, session
import spotipy, pprint
from app import app,sp_auth,Session

scopes = sp_auth.scopes
spfy_oauth = sp_auth.SP_HANDLER(scopes,session)
pp = pprint.PrettyPrinter()
@app.route('/')
@app.route('/index')
def index():
    user={}
    return render_template('index.html', login=user)

@app.route('/login', methods=['GET','POST'])
def login():
    print(session.get('token_info',None))
    if not spfy_oauth.valid_token():
        return redirect(spfy_oauth.get_auth_url())
    elif spfy_oauth.valid_token():
        return redirect(url_for('home'))
    
@app.route('/home')
def home():
    sp_auth = spfy_oauth.create_sp()
    if not sp_auth.validate_token(sp_auth.cache_handler.get_cached_token()):
        redirect(url_for('login'))
    spotify = spotipy.Spotify(auth_manager=sp_auth)
    # pp.pprint(spotify.current_user_top_tracks(limit=5,time_range='long_term')['items'][0])
    artist_items = spotify.current_user_top_artists(limit=5, time_range='long_term')['items']
    return render_template('home.html', artists=artist_items)

@app.route('/top_tracks', methods=['GET','POST'])
def top_tracks():
    sp_auth = spfy_oauth.create_sp()
    if not sp_auth.validate_token(sp_auth.cache_handler.get_cached_token()):
        redirect(url_for('login'))
    spotify = spotipy.Spotify(auth_manager=sp_auth)
    pp.pprint(spotify.current_user_top_tracks(limit=20,time_range='long_term')['items'][0])
    return redirect('/index')

@app.route('/top_artists', methods=['GET'])
def top_artists():
    sp_auth = spfy_oauth.create_sp()
    if not sp_auth.validate_token(sp_auth.cache_handler.get_cached_token()):
        redirect(url_for('login'))
    spotify = spotipy.Spotify(auth_manager=sp_auth)
    pp.pprint(spotify.current_user_top_artists(limit=10,time_range='long_term'))
    return redirect('/index')

@app.route('/api_callback')
def callback():
    # code = request.args.get('code')
    # session.clear()
    # tk_info = spfy_oauth.callback_token(code)
    # session['token_info'] = tk_info
    # # spotify=spotipy.Spotify(auth_manager=spfy_oauth.sp)
    # # print(spotify.me())
    # print(session['token_info'])
    code = request.args.get('code')
    if code:
        spfy_oauth.callback_token(code)
    if request.args.get('error'):
        return redirect(url_for('index'))
    print(session['token_info'])
    return redirect(url_for('index'))

@app.route('/logout', methods=['POST','GET'])
def logout():
    session.pop('token_info',None)
    session.modified = True
    return redirect(url_for('index'))

