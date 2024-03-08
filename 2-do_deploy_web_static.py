#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
"""
from fabric.api import put, run, env
import os


env.hosts = ['100.24.242.177', '54.165.77.224']


def do_deploy(archive_path):
    """fabric function"""
    tar_name = archive_path.split("/")[1]
    var = "/data/web_static/releases/"
    if not os.path.exists(archive_path):
        return False
    name_without_tgz = archive_path[:-4]
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(name_without_tgz))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            tar_name, name_without_tgz))
        run("rm /tmp/{}".format(tar_name))
        run("mv {}{}/web_static/* {}{}/".format(
            var, name_without_tgz, var, name_without_tgz))
        run("rm -rf {}{}/web_static".format(var, name_without_tgz))
        run("rm -f /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(
            var, name_without_tgz))
        return True
    except Exception:
        return False
