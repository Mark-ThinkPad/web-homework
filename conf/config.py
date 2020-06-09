from conf.settings import DATABASE_DIR

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_DIR + '/models.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
