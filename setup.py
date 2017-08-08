import os.path
from setuptools import setup, find_packages

meta_ns = {}
with open(os.path.join('airways', '__version__.py')) as f:
    exec(f.read(), meta_ns)

with open('requirements.txt') as f:
    __requirements__ = f.readlines()

setup(
    name='airways',
    description="A generic airways company management platform",
    version=meta_ns['__version__'],
    packages=find_packages(),
    install_requires=__requirements__
)
