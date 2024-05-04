#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():

    local("mkdir -p versions")

    now = datetime.utcnow()
    filename = 'web_static_' + now.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'

    result = local("tar -cvzf versions/{} web_static".format(filename))

    if result is not None:
        return filename
    else:
        return None
