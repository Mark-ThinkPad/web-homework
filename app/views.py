from flask import Blueprint, render_template, session
from app.decorators import login_required
from app.models import Note, Message

views = Blueprint('views', __name__)


@views.route('/')
def index():
    username = session.get('username')
    return render_template('index.html', username=username)


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
    username = session.get('username')
    notes = Note.query.filter_by(uid=uid).order_by(Note.upload_time.desc())
    return render_template('notes_get.html', username=username, notes=notes)


@views.route('/notes/add')
@login_required
def notes_add():
    username = session.get('username')
    return render_template('notes_add.html', username=username)


@views.route('/messages')
@login_required
def messages():
    username = session.get('username')
    return render_template('messages.html', username=username)
