import os, sys
import os.path

from setuptools import setup, find_packages

root = os.path.abspath(os.path.dirname(__file__))
package_name = "tpubar"
packages = find_packages(
    include=[package_name, "{}.*".format(package_name)]
)

# Version info -- read without importing
_locals = {}
with open(os.path.join(package_name, "_version.py")) as fp:
    exec(fp.read(), None, _locals)

version = _locals["__version__"]
binary_names = _locals["binary_names"]

with open(os.path.join(root, 'README.md'), 'rb') as readme:
    long_description = readme.read().decode('utf-8')

setup(
    name=package_name,
    version=version,
    description="tpubar",
    long_description=long_description,
    author='Tri Songz',
    author_email='ts@scontentenginex.com',
    url='http://github.com/trisongz/tpubar',
    python_requires='>3.6',
    install_requires=[
        "tqdm>=4.50.0",
        "google-cloud-monitoring",
        "tensorflow",
        "psutil",
        "pysimdjson",
    ],
    packages=packages,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
    ],
)