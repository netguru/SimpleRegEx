# -*- coding: utf-8 -*-
from setuptools import setup

setup_info = dict(
    name="simpleregex",
    version="0.1.6",
    author="Netguru",
    author_email="hello@netguru.com",
    url="https://github.com/netguru/SimpleRegEx",
    download_url="https://pypi.org/project/simpleregex/",
    project_urls={
        "Documentation": "https://github.com/netguru/SimpleRegEx/blob/main/docs/index.md",
        "Source": "https://github.com/netguru/SimpleRegEx",
        "Tracker": "https://github.com/netguru/SimpleRegEx/issues",
    },
    description="Wrapper for RegEx, made so the RegEx code will be understandable",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="BSD-3-Clause",
    classifiers=[
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Developers",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

setup(**setup_info)
