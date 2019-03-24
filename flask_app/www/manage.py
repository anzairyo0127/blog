import os

from blog_app import create_app

app = create_app(os.getenv('FLASK_CONFIG_STATUS'))
