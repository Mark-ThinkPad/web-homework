from flask import Blueprint, render_template, session
from app.decorators import login_required
from app.models import Note, Message

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/user/login')
def user_login():
    return render_template('user_login.html')


@views.route('/user/add')
def user_add():
    return render_template('user_add.html')


@views.route('/notes')
@login_required
def notes_get():
    uid = session.get('uid')
    notes = Note.query.filter_by(uid=uid).order_by(Note.upload_time.desc())
    return render_template('notes_get.html', notes=notes)


@views.route('/notes/add')
@login_required
def notes_add():
    return render_template('notes_add.html')


@views.route('/messages')
@login_required
def messages():
    msgs = Message.query.order_by(Message.upload_time.desc())
    return render_template('messages.html', messages=msgs)
