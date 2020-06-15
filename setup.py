from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

with open('VERSION', 'r') as f:
    version = f.read()

description = \
    'A lightweight library to perform deep merges of python dictionaries'

setup(
    name='pydeepmerge',
    version=version,
    license='MIT',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/taliamax/pydeepmerge',
    author='Natalia Maximo',
    author_email='iam@natalia.dev',
    python_requires=">=3.5",
    packages=find_packages(),
    keywords='mapping dictionary library merge',
    extras_require={
        'yaml': ['pyyaml'],
        'test': ['pytest', 'pytest-cov', 'coveralls', 'flake8']
    },
    entry_points={
        'pydeepmerge.config_parsers': [
            '.json = pydeepmerge.parsers.json:json_parser',
            '.yaml = pydeepmerge.parsers.yaml:yaml_loader [yaml]',
            '.yml = pydeepmerge.parsers.yaml:yaml_loader [yaml]'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
