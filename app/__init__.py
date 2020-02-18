import os
from flask import Flask
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from .app.db import db
from .app import views
from .app import commands


BASE_DIR = os.path.dirname(__file__)
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')

def config_by_app_mode(app_mode):
    return 'config.Development' if app_mode == 'development' else 'config.Production'

def create_app():
    app_mode = os.getenv('APP_MODE', 'development')

    app = Flask(
        __name__,
        static_url_path='',
        static_folder=STATIC_FOLDER,
        template_folder=TEMPLATE_FOLDER
        )
    
    app.config.from_object(config_by_app_mode(app_mode))

    ckeditor = CKEditor(app)

    views.register_all_blueprints(app)
    commands.register_commands(app)

    db.init_app(app)
    migrate = Migrate(app, db)
    
    return app
