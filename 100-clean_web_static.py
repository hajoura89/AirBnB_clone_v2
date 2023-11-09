#!/usr/bin/python3
# A fabric script (based on the file 3-deploy_web_static.py) that deletes
# out-of-date archives, using the function do_clean:

import os
from fabric.api import *

env.hosts = ["552.91.135.216", "204.236.241.26"]


def do_clean(number=0):
    """Delete out-of-date archives using do_clean

    Args:
        number (int): The number of archives to keep.

    - If number is 0 or 1, keeps only the most recent archive.
    - If number is 2, keeps the most and second-most recent archives,
    - etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
