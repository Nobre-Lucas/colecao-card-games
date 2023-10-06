from flask import flash, redirect, url_for
from flask_login import login_required, logout_user, current_user

from app import app

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Usuário deslogado!')
    return redirect(url_for('index'))