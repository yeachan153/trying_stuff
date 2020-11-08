import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

# https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
# https://setuptools.readthedocs.io/en/latest/references/keywords.html


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


setup(
    name="my_package",  # Name to be used by pip (usually the same as package name)
    version="0.1.0",  # Version
    license="MIT",
    description="Example test package.",  # short, one-sentence summary of the package.
    long_description=read("readme.md"),  # detailed description of the package.
    author="Yeachan Park",
    author_email="yeachan153@gmail.com",
    url="",  # URL for the homepage of the project.
    packages=find_packages(
        "src"
    ),  #  list of all Python import packages that should be included in the Distribution Package. Instead of listing each package manually, we can use find_packages() to automatically discover all packages and subpackages.
    package_dir={
        "": "src"
    },  # keys to this dictionary are package names, and an empty package name stands for the root package. The values are directory names relative to your distribution root. In this case, when you say packages = ['foo'], you are promising that the file lib/foo/__init__.py exists.
    # py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,  # This tells setuptools to install any data files it finds in your packages. The data files must be specified via the distutils’ MANIFEST.in file.
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        "Topic :: Utilities",
    ],  # Provide a list of classifiers that categorize your project.
    project_urls={
        "Changelog": "https://github.com/ionelmc/python-nameless/blob/master/CHANGELOG.rst",
        "Issue Tracker": "https://github.com/ionelmc/python-nameless/issues",
    },  # List additional relevant URLs about your project.
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",  # runs on certain Python version
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],  # specification that is used to install its dependencies
    extras_require={
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
        "test": ["pytest"]
    },  # Extra requirements in certain situations, e.g. pip install -e .[rst]
    # tests_require=["pytest"],
    # entry_points={
    #     "console_scripts": [
    #         "nameless = nameless.cli:main",
    #     ]
    # } # Executes cmd namelss from nameless.cli:main,
    
)
