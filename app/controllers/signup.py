from flask import render_template

from app import app

@app.route('/sign-up')
def signup():
    return render_template('signup.html')