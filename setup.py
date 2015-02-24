import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "readability-score",
    version = "1.0",
    author = "Wim Muskee",
    author_email = "wimmuskee@gmail.com",
    description = ("This tool can calculate the readability score of a text."),
    license = "GPL-2",
    keywords = "text difficulty readability score",
    packages=find_packages(),
    long_description=read('README')
)
