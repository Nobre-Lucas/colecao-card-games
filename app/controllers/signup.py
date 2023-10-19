from flask import render_template

from app import app
from app import db

from app.models.users import User
from app.models.forms import SignupForm

import bcrypt

@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        name = signup_form.fullname.data
        email = signup_form.email.data
        new_user = User(username, password, name, email)
        db.session.add(new_user)
        db.session.commit()
        return render_template('home.html')
    else:
        print(signup_form.errors)
    return render_template('signup.html', form=signup_form)