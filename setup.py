import os
from distutils.core import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="builtwith",
    version="1.4.0",
    packages=["builtwith"],
    package_dir={"builtwith": "src"},  # look for package contents in current directory
    data_files=[("builtwith", ["src/apps.json"])],
    author="Richard Penman",
    author_email="richard.penman@gmail.com",
    description="Detect the technology used by a website\
                , such as Apache, JQuery, and Wordpress.",
    long_description=read("README.rst"),
    url="https://github.com/richardpenman/builtwith",
    license="lgpl",
)
