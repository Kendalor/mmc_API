from flask_restplus import fields
from api.restplus import api

modpackbuilds = api.model('Modpack Build', {
    'name': fields.String(required=True, description='Modpack Name'),
    'release': fields.String(required=True, description='release type identifier A,B,R'),
    'serverFileLink': fields.String(description='Link to the serverfile if available'),
    'version': fields.String(required=True, description= 'Buildversion')
})

