#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder
in the current working directory"""
from datetime import datetime
from fabric.api import local, put, run, cd
import os.path


def do_pack():
    """genearates a .tgz archive from contents of the web_static folder"""
    local("mkdir -p versions")
    path = "versions/web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    )
    result = local("tar -cvzf {} ./web_static/".format(path))
    if result.failed:
        return None
    return path


def do_deploy(arhive_path):
    """distributes an archive to 2 web servers"""

    env.user = "ubuntu"
    env.hosts = ['34.148.201.37'. '34.204.181.101']
    env.key_filename = "~/.ssh/ssh_key"

    if not os.path.exists(archive_path):
        return False
    # do_pack()
    archive_file = os.path.basename(archive_path)
    folder_name = archive_file.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)

    try:
        put("archive_path", "/tmp/{}".format(archive_file))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_file, folder_path))
        run("rm -rf /tmp/{}".format(archive_file))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print("New version deployed!")
    except Exception:
        return False
    return True
