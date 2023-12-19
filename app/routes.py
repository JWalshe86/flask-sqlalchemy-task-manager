from flask import render_template
from app import app, db

from app.models import Category, Task

@app.route("/")
def home():
    return render_template("tasks.html")