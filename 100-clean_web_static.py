#!/usr/bin/python3
"""clean"""
from fabric.api import local, env, run
import os


env.hosts = ['54.165.77.224', '100.24.242.177']
env.warn_only = True


def do_clean(number=0):
    """fabric function"""
    versions = os.listdir("versions/")
    versions_date_time = []
    for ver in versions:
        versions_date_time.append(int(ver.split("_")[2][:-4]))
    versions_date_time.sort()
    if number == "0" or number == "1":
        for ver in versions:
            if str(versions_date_time[-1]) not in ver and str(versions_date_time[-2]) not in ver:
                local(f"rm -rf versions/{ver}")
                run(f"rm -rf /data/web_static/releases/versions/{ver[:-4]}")
                print(versions)
