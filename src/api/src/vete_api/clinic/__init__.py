from flask import Blueprint

bp = Blueprint('api/clinic', __name__)
from . import routes