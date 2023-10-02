from flask import render_template

from app import app
from app.models.forms import SignupForm

@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()
    print(signup_form)
    if signup_form.validate_on_submit():
        print(signup_form.username.data)
    else:
        print(signup_form.errors)
    return render_template('signup.html', form=signup_form)