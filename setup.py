from setuptools import setup, find_packages
import codecs
import os

from sendchamp import __version__

here = os.path.abspath(os.path.dirname(__file__))

VERSION = __version__
DESCRIPTION = 'Sendchamp API wrapper'

# Setting up
setup(
    name="sendchamp-py",
    version=VERSION,
    author="Kenneth Gabriel",
    author_email="kennethgabriel78@gmail.com",
    description=DESCRIPTION,
    long_description="""
    **Github Repo**:  [https://github.com/keosariel/sendchamp-py](https://github.com/keosariel/sendchamp-py)
    **Documentation**: [https://github.com/keosariel/sendchamp-py/blob/master/README.md](https://github.com/keosariel/sendchamp-py/blob/master/README.md)
    """,
    long_description_content_type="text/markdown",
    url="https://github.com/keosariel/sendchamp-py",
    packages=find_packages(),
    license="MIT",
    install_requires=[
        "httpx==0.22.0"
    ],
    extras_require={
        "dotenv": ["python-dotenv"],
    },
    keywords=['python', 'sendchamp', 'httpx', 'client', 'wrapper'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)