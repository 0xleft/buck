from setuptools import setup, find_packages

setup(
    name='buck',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'buck = buck:main',
        ],
    },
)
