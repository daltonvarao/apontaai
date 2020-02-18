from ..accounts.views import accounts
from ..home.views import home
from ..auth.views import auth


def register_all_blueprints(app):
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(accounts, url_prefix='/account')
    app.register_blueprint(auth, url_prefix='/auth')
