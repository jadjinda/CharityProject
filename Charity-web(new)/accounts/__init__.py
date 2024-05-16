from flask import Blueprint, render_template, request, redirect, url_for, flash
from accounts.models.User import User
from flask_login import login_user, logout_user, login_required
from extensions import db

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            nom = request.form['nom']
            prenom = request.form['prenom']
            username = request.form['username']
            password = request.form['password']
            new_user = User(nom=nom, prenom=prenom, username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash('Inscription échoué.', 'error')
    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('charity_web.index'))
        else:
            flash('Authentification échoué.', 'error')
            return render_template('login.html', error='Identifiants invalides.')
    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('charity_web.index'))
