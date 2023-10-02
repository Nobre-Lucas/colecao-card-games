from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    database_url = app.config.get("SQLALCHEMY_DATABASE_URI")
    secret_key = app.config.get("SECRET_KEY")
    print(f'database_url: {database_url}\nsecret_key: {secret_key}')
    return render_template('home.html')
