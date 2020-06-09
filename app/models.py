from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)  # 默认为自增列
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    admin = db.Column(db.Boolean, default=False)  # 是否为管理员

    def __init__(self, name, pwd):
        self.username = name
        self.password = pwd
