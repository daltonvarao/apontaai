from flask import Blueprint, render_template
from ..app.utils import login_required, admin_required

home = Blueprint('home', __name__)


@home.route('/')
def index():
    return render_template('home/index.html')
