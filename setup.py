from setuptools import setup
import codecs
import os

try:
    f = codecs.open("README.rst", encoding="utf-8")
    long_description = f.read()
    f.close()
except:
    long_description = ""

version_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "VERSION")

setup(
    name="dockerignore-generate",
    version=open(version_file).read().rstrip(),
    author="Denis Khshaba",
    author_email="deniskhoshaba@gmail.com",
    scripts=["dockerignore-generate"],
    url="https://github.com/theden/dockerignore-generate",
    keywords=["docker", "dockerignore", "linux", "containers"],
    license="GPL-2.0",
    description="automatically generate dockerignore data",
    long_description=long_description,
)
