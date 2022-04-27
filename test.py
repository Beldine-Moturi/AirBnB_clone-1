#!/usr/bin/python3
"""tests fabric"""
from fabric.api import env, put, run

env.user = "ubuntu"
env.hosts = ['34.148.201.37', '34.204.181.101']
env.key_filename = "~/.ssh/ssh_key"


def test_fab():
    """test fabric"""
    result = run("hostname && pwd")
    print(f"{result.succeeded}")
