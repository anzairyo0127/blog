from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required

# flask呼び出し
app = Flask(__name__)
# 設定呼び出し
app.config.from_object('flaskr.config')

# loginマネージャ呼び出し
login_manager = LoginManager()
# SQLalchemy呼び出し
db = SQLAlchemy(app)

# loginマネージャの設定
login_manager.init_app(app)
# migraterの設定
migrate = Migrate(app, db)

import flaskr.views
