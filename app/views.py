from flask import Blueprint, render_template, session
from app.decorators import login_required
from app.models import User

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
    user = User.query.get(uid)
    print(user)
    for note in user.notes:
        print(note)
        print(note.upload_time, type(note.upload_time))
    return render_template('notes_get.html', username=username, notes=user.notes)


@views.route('/notes/add')
@login_required
def notes_add():
    username = session.get('username')
    return render_template('notes_add.html', username=username)
