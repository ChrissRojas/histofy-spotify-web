from flask import Flask,session
from config import Config
from flask_session import Session, SqlAlchemySessionInterface
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
app.config['SESSION_SQLALCHEMY']=db
migrate = Migrate(app,db)
Session(app)


from app import routes