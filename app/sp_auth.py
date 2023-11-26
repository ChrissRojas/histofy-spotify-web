from os import environ
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

scopes = ['user-top-read']

class SP_HANDLER:
    CLIENT_ID = environ.get('SPOTIPY_CLIENT_ID')
    CLIENT_SECRET = environ.get('SPOTIPY_CLIENT_SECRET')
    CLIENT_REDIRECT = environ.get('SPOTIPY_REDIRECT_URI')

    def __init__(self,scopes,session):
        self.scopes=scopes
        self.combined_scope = ",".join(self.scopes)
        self.session = session
    
    def create_sp(self, show_dialog=True):
        cache_handler = FlaskSessionCacheHandler(self.session)
        return SpotifyOAuth(
            client_id = self.CLIENT_ID,
            client_secret= self.CLIENT_SECRET,
            redirect_uri= self.CLIENT_REDIRECT,
            scope = self.combined_scope,
            cache_handler=cache_handler,show_dialog=show_dialog)

    def get_auth_url(self):
        auth_manager = self.create_sp()
        auth_url = auth_manager.get_authorize_url()
        return auth_url
    
    def valid_token(self):
        auth_manager = self.create_sp(show_dialog=False)
        return auth_manager.validate_token(auth_manager.cache_handler.get_cached_token())

    def callback_token(self,code):
        auth_manager = self.create_sp(show_dialog=False)
        auth_manager.get_access_token(code)
        
    
    def add_scope(self, scp):
        self.scopes.append(scp)
        self.combined_scope = ",".join(self.scopes)