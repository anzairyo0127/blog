from flask import Flask
from controllers.blog_controllers import blog_route
from objects.database import db
from objects.logins import init_login

# コンフィグマップ
config_status = {
    'test': 'config.Testing',
    'dev': 'config.Development',
    'product': 'config.Production'
}


def create_app(config_mode='test'):
    app = Flask(__name__)
    # 設定呼び出し
    app.config.from_object(config_status[config_mode])
    db.init_app(app)
    init_login(app)
    app.register_blueprint(blog_route)

    return app
