from database import mongo
from flask import jsonify


def getModpackBuilds(name, release=False):
    builds = mongo.db.ModpackBuilds
    if release:
        output = builds.find({'name': name, 'release': "R"}, {"_id": False, "name": 1, "version": 1, "release": 1,
                                                              "serverFileLink": 1})
        return sorted(list(output), key=lambda k: int(str(k['version']).replace(".", "")))[-1:]
    else:
        output = builds.find({'name': name}, {"_id": False, "name": 1, "version": 1, "release": 1,
                                              "serverFileLink": 1})
        return sorted(list(output), key=lambda k: int(str(k['version']).replace(".", "")))[-1]
