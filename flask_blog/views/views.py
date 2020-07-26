from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import User

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(
        username=request.form['username'],
        password=request.form['password']
        )
        db.session.add(user)
        db.session.commit()
        flash('ユーザ登録を行いました')
        return redirect(url_for('login'))
    
    return render_template('register.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        # flash(user.password)
        # flash(password)
        if not user:
            flash('ユーザ名が異なります')
        elif password != user.password:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            session['username'] = user.username
            session['users_id'] = user.id
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))