from setuptools import setup
import sys


def forbid_publish():
    argv = sys.argv
    blacklist = ["register", "upload"]

    for command in blacklist:
        if command in argv:
            values = {"command": command}
            print('Command "%(command)s" has been blacklisted, exiting...' % values)
            sys.exit(2)


forbid_publish()

setup(
    name="levi-huddleston-pachama",
    version="0.0.1",
    description="A package to extract values from raster files.",
    author="Levi Huddleston",
    packages=["levi-huddleston-pachama"],
    url=None,
)