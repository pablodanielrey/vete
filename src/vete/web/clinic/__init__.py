from flask import Blueprint

bp = Blueprint('clinic', __name__, template_folder='templates')
from . import routes