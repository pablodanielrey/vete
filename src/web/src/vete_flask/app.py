import inject
from vete_flask.config import configure
inject.configure(configure)

import json
from vete_entities import Base

class EntitySerializer(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Base):
            return obj.to_dict()
        else:
            return json.JSONEncoder.default(self, obj)



from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask
webapp = Flask(__name__)
webapp.config['SECRET_KEY'] = 'you-will-never-guess'
webapp.wsgi_app = ProxyFix(webapp.wsgi_app)
webapp.json_encoder = EntitySerializer


from .index import bp as index_bp
webapp.register_blueprint(index_bp)

from .clinic import bp as clinic_bp
webapp.register_blueprint(clinic_bp, url_prefix='/clinic')
