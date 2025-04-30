from setuptools import setup, find_packages

setup(
    name='python-release-demo',
    version='0.4.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'release-demo=main:say_hello dolly',
        ],
    },
)
