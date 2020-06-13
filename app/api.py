from flask import Blueprint, request, session
from sqlalchemy.exc import IntegrityError
from app.decorators import login_required
from app.models import db, User, Note

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
        user = User.query.filter_by(username=username, password=password).first()
        session['uid'] = user.uid
        session['username'] = user.username
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
    session['uid'] = user.uid
    session['username'] = user.username
    return {'success': True, 'message': '登录成功'}


@api.route('/user/logout', methods=['POST'])
def user_logout():
    session.clear()
    return {'success': True, 'message': '注销成功'}


@api.route('/notes/add', methods=['POST'])
@login_required
def notes_add():
    uid = session.get('uid')
    title = request.form.get('title', False)
    content = request.form.get('content', False)

    if not (title and content):
        return {'success': False, 'message': '传入数据不全'}

    new_note = Note(uid, title, content)
    db.session.add(new_note)
    db.session.commit()
    return {'success': True, 'message': '添加新笔记成功'}

