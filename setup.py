import sys
from setuptools import setup, find_packages

install_requires = [
    'asn1crypto==1.3.0',
    'oscrypto==1.2.0',
    'pyOpenSSL==19.1.0',
]

if sys.version_info.minor == 6:
    install_requires += [
        'dataclasses==0.7'
    ]

tests_require = [
    'pytest==5.4.1',
    'pytest-cov==2.8.1',
    'coverage==5.0.4',
]

setup(
    name='pyas2lib',
    description="Python library for building and parsing AS2 Messages",
    license="GNU GPL v2.0",
    url="https://github.com/abhishek-ram/pyas2-lib",
    long_description="Docs for this project are maintained at "
                     "https://github.com/abhishek-ram/pyas2-lib/blob/"
                     "master/README.md",
    version='1.2.2',
    author="Abhishek Ram",
    author_email="abhishek8816@gmail.com",
    packages=find_packages(
        where='.',
        exclude=('test*',)
    ),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Security :: Cryptography",
        "Topic :: Communications",

    ],
    install_requires=install_requires,

    test_suite='nose.collector',
    tests_require=tests_require,
)
