from flask import render_template

from app import app

@app.route('/sign-in')
def signin():
    return render_template('signin.html')