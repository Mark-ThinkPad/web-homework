from flask import Blueprint, request, session
from sqlalchemy.exc import IntegrityError
from app.models import db, User

api = Blueprint('api', __name__)


@api.route('/user/add', methods=['POST'])
def user_add():
    username = request.form.get('username', False)
    password = request.form.get('password', False)

    if not (username and password):
        return {'success': False, 'message': '传入数据不全'}

    try:
        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        return {'success': True, 'message': '注册成功'}
    except IntegrityError:
        return {'success': False, 'message': '用户名已存在'}


@api.route('/user/login', methods=['POST'])
def user_login():
    username = request.form.get('username', False)
    password = request.form.get('password', False)

    if not (username and password):
        return {'success': False, 'message': '传入数据不全'}

    user = User.query.filter_by(username=username, password=password).first()
    if user is None:
        return {'success': False, 'message': '用户名错误或密码错误'}
    session.clear()
    session['username'] = username
    return {'success': True, 'message': '登录成功'}


@api.route('/user/logout', methods=['POST'])
def user_logout():
    session.clear()
    return {'success': True, 'message': '注销成功'}
