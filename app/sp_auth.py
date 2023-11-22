from os import environ
import spotipy
from spotipy.oauth2 import SpotifyOAuth


scopes = ['user-top-read']

class SP_HANDLER:
    CLIENT_ID = environ.get('SPOTIPY_CLIENT_ID')
    CLIENT_SECRET = environ.get('SPOTIPY_CLIENT_SECRET')
    CLIENT_REDIRECT = environ.get('SPOTIPY_REDIRECT_URI')

    def __init__(self,scopes):
        self.scopes=scopes
        self.combined_scope = ",".join(self.scopes)
        self.sp = None
    
    def create_sp(self):
        self.sp = SpotifyOAuth(
            client_id = self.CLIENT_ID,
            client_secret= self.CLIENT_SECRET,
            redirect_uri= self.CLIENT_REDIRECT,
            scope = self.combined_scope)
    
    def get_auth_url(self):
        self.create_sp()
        auth_url = self.sp.get_authorize_url()
        return auth_url
    
    def callback_token(self,code):
        self.create_sp()
        token_info = self.sp.get_access_token(code)
        return token_info
    
    def add_scope(self, scp):
        self.scopes.append(scp)
        self.combined_scope = ",".join(self.scopes)