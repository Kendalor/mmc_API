from flask import jsonify
from flask import Flask, Blueprint
from api.modpackbuilds.endpoints.ModpackBuilds import ns as modpackbuilds_ns
from api.modpackbuilds.endpoints.ModpackBuildsRelease import ns as modpackbuildsrelease_ns
import logging.config
import os
from flask_restplus import Resource
import settings
from database import mongo
from api.restplus import api


app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['MONGODB_DATABASE_URI'] = settings.MONGODB_DATABASE_URI
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['HOST'] = settings.FLASK_HOST
    flask_app.config['PORT'] = settings.FLASK_PORT
    app.config['MONGO_URI'] = settings.MONGODB_DATABASE_URI
    app.config['MONGO_DBNAME'] = settings.MONGO_DBNAME

def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(modpackbuilds_ns)
    api.add_namespace(modpackbuildsrelease_ns)
    flask_app.register_blueprint(blueprint)

    mongo.init_app(flask_app)
    mongo.cx.server_info()



def main():
    try:
        initialize_app(app)
    except:
        log.info('Error while Initalizing, did you Configure the settings.py ?')
        exit()
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG, host=settings.FLASK_HOST)







if __name__ == '__main__':
    main()
