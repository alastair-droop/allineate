from setuptools import setup, find_packages
import os.path

# Get the version:
version = {}
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'allineate', 'version.py')) as f: exec(f.read(), version)

setup(
    name = 'allineate',
    version = version['__version__'],
    description = 'Align lines in a file by the first occurrence of a given substring',
    author = 'Alastair Droop',
    author_email = 'alastair.droop@gmail.com',
    url = 'https://github.com/alastair.droop/allineate',
    classifiers = [
        'Programming Language :: Python :: 3'
    ],
    packages = find_packages(),
    install_requires = [
    ],
    python_requires = '>=3',
    entry_points = {
        'console_scripts': [
            'allineate=allineate.scripts:allineate'
        ]
    }
)
