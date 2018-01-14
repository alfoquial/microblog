from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alfonso'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Maravilloso día de campo'
        },
        {   'author': {'username': 'Peter'},
            'body': 'la venganza de las zorras'

         }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_form('index'))
    return render_template('login.html', title='Sign In', form=form)
