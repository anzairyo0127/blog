from flask_login import LoginManager

login = LoginManager()


def init_login(app):
    login.init_app(app)
