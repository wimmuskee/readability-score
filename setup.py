import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "readability-score",
    version = "0.2",
    author = "Wim Muskee",
    author_email = "wimmuskee@gmail.com",
    description = ("This tool can calculate the readability score of a Dutch text."),
    license = "GPL-2",
    keywords = "text difficulty Dutch readability score",
    packages=find_packages(),
    namespace_packages=['readability-score'],
    long_description=read('README')
)
