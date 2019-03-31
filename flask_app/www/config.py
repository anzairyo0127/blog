import os


class Testing(object):
    TESTING = True


class Development(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lion:lion@172.19.0.2/db_blog?charset=utf8'
    SECRET_KEY = '\x10R8K\x94\xf4\xbaE\xea!\xca\xf8#\xa3e\xe6_\xad\xe6\xb5F\x95`\x90'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    DEFAULT_MAIL_SENDER = os.getenv('DEFAULT_MAIL_SENDER')


class Production(object):
    DEBUG = False
    TESTING = False
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{db_user}:{db_password}@127.0.0.1/db_blog?charset=utf8'.format(
        db_user=db_user,
        db_password=db_password
    )
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    DEFAULT_MAIL_SENDER = os.getenv('DEFAULT_MAIL_SENDER')
