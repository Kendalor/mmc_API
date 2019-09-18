import logging
from flask_restplus import Api
import settings

log = logging.getLogger(__name__)

api = Api(version='1.2', title='Modded Minecraft API (MMC)',
          description='A simple API used to provide latest release information for Modapcks hosted on Curseforge')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


