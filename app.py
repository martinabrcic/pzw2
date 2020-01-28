from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, make_response
from data import Articles
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

Articles = Articles()

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html', id=id)

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=3, max=50)])
    username = StringField('Username', [validators.Length(min=5, max=25)])
    email = StringField('Email', [validators.Length(min=7, max=30)])
    password = PasswordField('Password', [validators.DataRequired(),
    validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('regsuc.html')
    return render_template('register.html', form=form)

@app.route("/set")
def setcookie():
    resp = make_response('Setting cookie!')
    resp.set_cookie('framework', 'flask')
    return resp

@app.route("/get")
def getcookie():
    framework = request.cookies.get('framework')
    return 'The framework is ' + framework + '.'

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
	
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)