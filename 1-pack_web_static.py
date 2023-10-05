#!/usr/bin/python3
# i used the fabrrical scrited generates a .tgz archive from the
# contentsof the web_static folder of your AirBnB Clone repo
# contentsof the web_static
# all files ae inside a folder web_static
# archives were created

from fabric.api import *
from os import path
from datetime import datetime
from shlex import split

env.user = 'ubuntu'
env.hosts = ['34.74.70.205', '34.224.30.177']


def do_pack():
    """Packed the directory in .tgz"""
    print("Packing web_static to versions/web_static_20170314233357.tgz")
    if not path.exists('versions') or (
                                       path.exists('versions') and
                                       not path.isdir('versions')):
        local('mkdir -p versions')
    d_now = datetime.now()
    cmd_tar = 'tar -cvzf '
    p_name = 'versions/web_static_'
    p_name += '{:4}{:02}{:02}'.format(d_now.year, d_now.month, d_now.day)
    p_name += '{:02}{:02}{:02}'.format(d_now.hour, d_now.minute, d_now.second)
    p_name += '.tgz'
    cmd_tar += p_name
    cmd_tar += ' web_static'
    try:
        local(cmd_tar)
        return p_name
    except:
        return None
