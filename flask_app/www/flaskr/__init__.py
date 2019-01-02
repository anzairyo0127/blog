'''
flaskr読み込み
'''

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user
from flask_mail import Mail, Message


config_status = {
    'test': 'flaskr.config.Testing',
    'dev': 'flaskr.config.Development',
    'product': 'flaskr.config.Production'
}

# flask呼び出し
app = Flask(__name__)
# 設定呼び出し
app.config.from_object(config_status[os.getenv('FLASK_CONFIG_STATUS')])

# loginマネージャ呼び出し
login_manager = LoginManager()
# SQLalchemy呼び出し
db = SQLAlchemy(app)
# Flask-mail呼び出し
mail = Mail(app)

# loginマネージャの設定
login_manager.init_app(app)
# migraterの設定
migrate = Migrate(app, db)

import flaskr.views
