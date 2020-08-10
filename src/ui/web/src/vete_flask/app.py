import inject
from vete.config import configure
inject.configure(configure)

from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask
webapp = Flask(__name__)
webapp.config['SECRET_KEY'] = 'you-will-never-guess'
webapp.wsgi_app = ProxyFix(webapp.wsgi_app)

from .index import bp as index_bp
webapp.register_blueprint(index_bp)

from .clinic import bp as clinic_bp
webapp.register_blueprint(clinic_bp, url_prefix='/clinic')
