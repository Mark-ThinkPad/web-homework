from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('base.html')


@views.route('/user/login')
def user_login():
    return '用户登录'


@views.route('/user/add')
def add_user():
    return '用户注册'


@views.route('/notes')
def get_notes():
    return '云笔记'


@views.route('/notes/add')
def add_notes():
    return '添加云笔记'
