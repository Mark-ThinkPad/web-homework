from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/user/login')
def user_login():
    return render_template('user_login.html')


@views.route('/user/add')
def add_user():
    return render_template('user_add.html')


@views.route('/notes')
def get_notes():
    return render_template('notes.html')


@views.route('/notes/add')
def add_notes():
    return render_template('notes_add.html')
