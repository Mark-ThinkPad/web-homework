from flask import Blueprint, request, session
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename
from pypinyin import lazy_pinyin
from app.decorators import login_required
from app.models import db, User, Note, Message, Image
from app.utils import allowed_image
from conf.settings import UPLOAD_IMAGE_DIR, IMAGE_URL_PATH, ALLOWED_IMAGE_TYPE
import os

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


@api.route('/messages/add', methods=['POST'])
@login_required
def messages_add():
    uid = session.get('uid')
    content = request.form.get('content', False)

    if not content:
        return {'success': False, 'message': '传入数据不全'}

    new_msg = Message(uid, content)
    db.session.add(new_msg)
    db.session.commit()
    return {'success': True, 'message': '添加新留言成功'}


@api.route('/images/add', methods=['POST'])
@login_required
def images_add():
    uid = session.get('uid')
    files = request.files.getlist('images')
    if len(files) == 0:
        return {'success': False, 'message': '传入参数错误'}
    for file in files:
        if file.filename == '':
            return {'success': False, 'message': '没有文件传入'}
        if file and allowed_image(file.filename):
            filename = secure_filename(file.filename)
            if filename.startswith('.') or filename in ALLOWED_IMAGE_TYPE:
                name = file.filename.split('.')[0]
                ext = file.filename.split('.')[1]
                filename = '_'.join(lazy_pinyin(name)) + '.' + ext
            file.save(os.path.join(UPLOAD_IMAGE_DIR, filename))
            url = os.path.join(IMAGE_URL_PATH, filename)
            new_image = Image(uid, filename, url)
            db.session.add(new_image)
            db.session.commit()
        else:
            return {'success': False, 'message': '没有文件传入或文件类型不允许'}
    return {'success': True, 'message': '上传图片成功'}
