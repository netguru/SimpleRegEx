from setuptools import setup

setup_info = dict(
    name='Simple RegEx',
    version='0.1.2',
    author='Netguru',
    author_email='hello@netguru.com',
    url='https://test.pypi.org/project/simpleregex/',
    download_url='https://test.pypi.org/project/simpleregex/',
    project_urls={
        'Documentation': 'https://github.com/netguru/SimpleRegEx/blob/dev/docs/index.md',
        'Source': 'https://github.com/netguru/SimpleRegEx',
        'Tracker': 'https://github.com/netguru/SimpleRegEx/issues',
    },
    description='This tool is a wrapper for RegEx in Python, '
                'which introduces pattern functions in place of unreadable text patterns.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='BSD-3-Clause',
    classifiers=[
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

setup(**setup_info)
