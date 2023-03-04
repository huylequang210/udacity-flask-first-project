from flask import render_template, flash, redirect, request, session, url_for
from config import Config
from FlaskWebProject import app, db
from FlaskWebProject.models import Post

@app.route("/")
def home():
    Post.query.all()
    return "Hello, World!"