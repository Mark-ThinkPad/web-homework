from functools import wraps
from flask import session, redirect, url_for


def login_required(f):
    @wraps(f)
    def isLogin(*args, **kwargs):
        username = session.get('username')
        if username is None:
            return redirect(url_for('views.user_login'))
        else:
            return f(*args, **kwargs)
    return isLogin
