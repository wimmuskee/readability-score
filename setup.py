import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "avi-calculator",
    version = "0.0.1",
    author = "Wim Muskee",
    author_email = "wimmuskee@gmail.com",
    description = ("This tool can calculate the AVI score of a Dutch text."),
    license = "GPL-2",
    keywords = "text difficulty Dutch avi score",
    packages=['calculators'],
    long_description=read('README')
)
