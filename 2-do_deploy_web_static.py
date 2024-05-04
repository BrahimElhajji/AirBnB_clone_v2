#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""

from fabric.api import env, put, run
import os

env.hosts = ['100.26.246.41', '54.166.60.69']
env.user = 'ubuntu'
env.key_filename = ['my_ssh_private_key']


def do_deploy(archive_path):
    """creates and distributes an archive to your web servers,
    using the function deploy"""

    if not os.path.exists(archive_path):
        return False

    try:
        filename = archive_path.split("/")[-1]
        folder_name = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, folder_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, folder_name))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, folder_name))
        run('rm -rf {}{}/web_static'.format(path, folder_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, folder_name))

        return True
    except Exception:
        return False
