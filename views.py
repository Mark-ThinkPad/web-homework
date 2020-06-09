from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/user/login')
def user_login():
    return '用户登录'


@views.route('/user/add')
def add_user():
    return '用户注册'


@views.route('/notes')
def get_notes():
    return render_template('notes.html')


@views.route('/notes/add')
def add_notes():
    return render_template('notes_add.html')
