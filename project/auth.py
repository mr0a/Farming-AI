from flask import Blueprint, render_template, redirect, url_for, request, flash, Markup
from . import db
from .models import User
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash(Markup('Email already exists. Go to <a href="'+url_for('auth.login')+'">login</a> page.'))
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=password)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()

    if not user or password != user.password:
        flash('Please check your login details and try again')
        return redirect(url_for('auth.login'))
    user.authenticated = True
    db.session.add(user)
    db.session.commit()
    login_user(user, remember=remember)

    return redirect(url_for('main.index'))
