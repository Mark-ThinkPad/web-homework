from conf.settings import DATABASE_DIR


class Config:
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_DIR + '/models.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # session设置
    SECRET_KEY = b'\x07\xb0\xa8wwGp\xb0l\x90\xfd|C!t\xf8'
