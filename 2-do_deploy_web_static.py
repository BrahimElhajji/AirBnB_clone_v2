#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import env, put, run
import os

env.hosts = ['web-01.brahimelhajji.tech', 'web-02.brahimelhajji.tech']


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        filename = os.path.basename(archive_path)
        folder_name = filename.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(filename, folder_name))

        run('rm /tmp/{}'.format(filename))

        run('rm -f /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_name))

        return True
    except Exception as e:
        print(e)
        return False
