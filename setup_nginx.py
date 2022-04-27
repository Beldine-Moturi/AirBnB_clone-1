#!/usr/bin/python3
"""Transfers script that sets up nginx for deployment of static web pages
runs it on remote hosts"""
from fabric.api import env, put, run

env.user = "ubuntu"
env.hosts = ['34.148.201.37', '34.204.181.101']
env.key_filename = "~/.ssh/ssh_key"

def upload_file():
    """upload script to remote hosts"""
    put("./0-setup_web_static.sh", "~/", mirror_local_mode=True)

def setup_nginx():
    """runs scrips that configures nginx"""
    upload_file()
    result = run("~/0-setup_web_static.sh")
    print(f"{result.succeeded}")
