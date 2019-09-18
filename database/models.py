
def create_modpack_build(data):
    print(data)
    name = data["name"]
    version = data["version"]
    serverfilelink = data["serverFileLink"]
    release = data["release"]

    return dict(name=name, release=release, serverFileLink=serverfilelink, version=version)
