#!/usr/bin/python3
"""clean"""
# from fabric.api import local, env, run
import os


def do_clean(number=0):
    """fabric function"""
    versions = os.listdir("versions/")
    versions_date_time = []
    for ver in versions:
        versions_date_time.append(ver.split("_")[2][:-4])
    versions_date_time.sort()
    print(versions_date_time)
do_clean()
