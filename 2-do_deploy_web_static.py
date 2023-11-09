#!/usr/bin/python3
"""
A fabric script that distributes an archive to web servers
using the function do_deploy
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["552.91.135.216", "204.236.241.26"]
env.user = "ubuntu"


def do_pack():
    """
        return the archive path if archive has generated correctly.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_path))

    if t_gzip_archive.succeeded:
        return archived_path
    else:
        return None


def do_deploy(archive_path):
    """
        Distribute archive to web server
    """
    if os.path.exists(archive_path):
        file = archive_path[9:]
        new_version = "/data/web_static/releases/" + file[:-4]
        file = "/tmp/" + file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_version))
        run("sudo tar -xzf {} -C {}/".format(file,
                                             new_version))
        run("sudo rm {}".format(file))
        run("sudo mv {}/web_static/* {}".format(new_version,
                                                new_version))
        run("sudo rm -rf {}/web_static".format(new_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_version))

        print("New version deployed!")
        return True

    return False
