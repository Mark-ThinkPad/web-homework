from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)  # 默认为自增列
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    admin = db.Column(db.Boolean, default=False)  # 是否为管理员
    notes = db.relationship('Note', backref='user', lazy='dynamic')
    messages = db.relationship('Message', backref='user', lazy='dynamic')
    images = db.relationship('Image', backref='user', lazy='dynamic')

    def __init__(self, name, pwd):
        self.username = name
        self.password = pwd

    def __repr__(self):
        return '<User %r %r %r>' % (self.uid, self.username, self.admin)


# 云笔记
class Note(db.Model):
    nid = db.Column(db.Integer, primary_key=True)  # 默认为自增列
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))  # 关联用户id
    upload_time = db.Column(db.DateTime, server_default=db.func.now())
    title = db.Column(db.String(40))
    content = db.Column(db.Text)

    def __init__(self, uid, title, content):
        self.uid = uid
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Note %r %r %r %r>' % (self.nid, self.uid, self.upload_time, self.title)


# 留言
class Message(db.Model):
    mid = db.Column(db.Integer, primary_key=True)  # 默认为自增列
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))  # 关联用户id
    upload_time = db.Column(db.DateTime, server_default=db.func.now())
    content = db.Column(db.String(200))

    def __init__(self, uid, content):
        self.uid = uid
        self.content = content

    def __repr__(self):
        return '<Message %r %r %r>' % (self.mid, self.uid, self.upload_time)


# 图片
class Image(db.Model):
    pid = db.Column(db.Integer, primary_key=True)  # 默认为自增列
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))  # 关联用户id
    upload_time = db.Column(db.DateTime, server_default=db.func.now())
    filename = db.Column(db.String(100))
    url = db.Column(db.String(120))

    def __init__(self, uid, filename, url):
        self.uid = uid
        self.filename = filename
        self.url = url

    def __repr__(self):
        return '<Image %r %r %r %r>' % (self.pid, self.uid, self.upload_time, self.filename)
