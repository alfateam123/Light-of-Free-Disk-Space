#from distutils.core import setup
from setuptools import setup

setup(
    name='LightOfFreeDiskSpace',
    version='0.1.0',
    author='alfateam123',
    author_email='alfateam123@gmail.com',
    scripts=['bin/light_of_free_disk_space'],
    url='http://github.com/alfateam123/LightOfFreeDiskSpace',
    # license='LICENSE.txt',
    description='check how much space you have and light up the mouse',
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ]
)
