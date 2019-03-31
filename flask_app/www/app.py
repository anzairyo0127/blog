import os
from flask_migrate import Migrate

from factory import create_app
from objects.database import db

app = create_app(os.getenv('FLASK_CONFIG_STATUS'))
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
