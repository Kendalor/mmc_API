from flask_pymongo import PyMongo
from flask import jsonify
from flask import Flask
import argparse
import sys
from flask_restplus import Resource, Api, fields
app = Flask(__name__)
api = Api(app)



@api.route('/api/serverfilelink/latest/<string:name>',
           doc={'name': "Name of the Modpack",
            "description": "Returns the ServerFileLink of the latest Build for the given Modpack on Curseforge"})
class ModpackBuilds(Resource):
    def get(self, name):
        builds = mongo.db.ModpackBuilds
        print("Triggered")
        output = builds.find({'name': name}, {"_id": False, "name": 1, "version": 1, "release": 1,
                                                  "serverFileLink": 1})
        return jsonify({"result": sorted(list(output), key=lambda k: int(str(k['version']).replace(".", "")))[-1:]})


@api.route('/api/serverfilelink/latest/release/<string:name>',
           doc={'name': "Name of the Modpack",
            "description": "Returns the ServerFileLink of the latest Release Build for the given Modpack on Curseforge"})
class ModpackBuildsRelease(Resource):
    def get(self, name):
        builds = mongo.db.ModpackBuilds
        output = builds.find({'name': name, 'release': "R"}, {"_id": False, "name": 1, "version": 1, "release": 1,
                                                  "serverFileLink": 1})
        return jsonify({"result": sorted(list(output), key=lambda k: int(str(k['version']).replace(".", "")))[-1:]})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='mmc_api')
    parser.add_argument('-uri',
                        action="store",
                        type=str, dest="uri",
                        required=True,
                        help="URI of MongoDB")

    parsed_args = parser.parse_args(sys.argv[1:])
    app.config['MONGO_URI'] = parsed_args.uri
    app.config['MONGO_DBNAME'] = 'twitchCrawl'
    mongo = PyMongo(app)
    app.run(debug=True)