from api.restplus import api
from flask_restplus import Resource
from api.modpackbuilds.dbOperations import getModpackBuilds
from database.models import create_modpack_build
from api.modpackbuilds.serializers import modpackbuilds

ns = api.namespace('modpackbuilds/latest',
                   description='Returns the latest modpackbuild for the given modpack on Curseforge')


@ns.route('/<string:name>')
@api.response(404, 'Name not found.')
class ModpackBuilds(Resource):
    @api.marshal_with(modpackbuilds)
    def get(self, name):
        """
        Returns the Latest build of the given Modpack
        """
        return create_modpack_build(getModpackBuilds(name, False))
