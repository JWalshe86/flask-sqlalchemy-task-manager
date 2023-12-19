import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Sunshine7!@localhost:5432/flaskChrisHawkesTutorial'
db = SQLAlchemy(app)
app.app_context().push()

from app import routes 
