#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder
in the current working directory and distributes it to 2 web servers"""
from datetime import datetime
from fabric.api import local, put, run, cd, env
import os.path


env.user = "ubuntu"
env.hosts = ['34.148.201.37', '34.204.181.101']
env.key_filename = "~/.ssh/ssh_key"


def do_pack():
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """

    local("mkdir -p versions")
    path = "versions/web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    )
    result = local("tar -cvzf {} ./web_static/".format(path))
    if result.failed:
        return None
    return path


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """

    if not os.path.exists(archive_path):
        print("os: archive_path does not exist")
        return False
    archive_file = os.path.basename(archive_path)
    folder_name = archive_file.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)

    try:
        put(archive_path, "/tmp/{}".format(archive_file))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_file, folder_path))
        run("rm -rf /tmp/{}".format(archive_file))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print("New version deployed!")
    except Exception as e:
        print(e)
        return False
    return True


def deploy():
    """deploys static web pages to 2 web servers"""

    path = do_path()
    if not path:
        return False

    deploy_status = do_deploy(path)
    return deploy_status
