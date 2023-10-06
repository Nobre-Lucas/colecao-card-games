from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

from app import app
from app.models.forms import LoginForm
from app.models.tables import User

import bcrypt

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        password = password.encode('utf-8')
        user = User.query.filter_by(email=email).first()
        if user:
            print(f'USER: {user}')
            password_hashed = user.password_hashed.encode('utf-8')
            password_is_correct = bcrypt.checkpw(password, password_hashed)
            if password_is_correct:
                login_user(user)
                print(type(current_user.is_authenticated))
                flash(f'Usuário {current_user.username} autenticado!')
                return redirect(url_for('index'))
            else:
                flash('Senha errada')
        else:
            flash('Email Inválido')
    return render_template('login.html', form=login_form)