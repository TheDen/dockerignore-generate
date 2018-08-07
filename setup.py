from setuptools import setup
import codecs

try:
    f = codecs.open("README.rst", encoding="utf-8")
    long_description = f.read()
    f.close()
except:
    long_description = ""

setup(
    name="dockerignore-generate",
    version="1.0.0",
    author="Denis Khshaba",
    author_email="deniskhoshaba@gmail.com",
    scripts=["dockerignore-generate"],
    url="https://github.com/theden/dockerignore-generate",
    keywords=["docker", "dockerignore", "linux", "containers"],
    license="GPL-2.0",
    description="automatically generate dockerignore data",
    long_description=long_description,
)
