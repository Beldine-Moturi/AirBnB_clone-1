#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder
in the current working directory"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """genearates a .tdgz archive from contents of the web_static folder"""
    local("mkdir -p versions")
    path = "versions/web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    )
    result = local("tar -cvzf {} ./web_static/".format(path))
    if result.failed:
        return None
    return path
