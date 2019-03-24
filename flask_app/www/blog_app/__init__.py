import os

from flask import Flask

from . import database
from . import mails
from . import logins
from .blog_controllers import blog_route


# コンフィグマップ
config_status = {
    'test': 'blog_app.config.Testing',
    'dev': 'blog_app.config.Development',
    'product': 'blog_app.config.Production'
}


def create_app(ENV_CONFIGMODE):
    # flask呼び出し
    app = Flask(__name__, instance_relative_config=True)
    # 環境変数より設定呼び出し
    conf_mode = config_status[ENV_CONFIGMODE]
    # 設定呼び出し
    app.config.from_object(conf_mode)
    # センシティブな設定の呼び出し。manage.pyと同じ階層にある、
    # instanceディレクトリ内のsensitive.cnfを読むが、存在しなければ適応されない。
    app.config.from_pyfile('sensitive.cnf', silent=True)
    # database初期化とmigration
    database.init_db(app)
    # Flask-mail初期化
    mails.init_mail(app)
    # Flask-loginmanager初期化
    logins.init_login(app)
    # BluePrintでルートを取得
    app.register_blueprint(blog_route)
    return app
