from setuptools import setup, find_packages

setup(
    name='pydeepmerge',
    version='0.1b',
    license='MIT',
    description='A lightway library to perform deep merges of python dictionaries',
    url='https://github.com/taliamax/deepmerge',
    maintainer='Natalia Maximo',
    maintainer_email='iam@natalia.dev',
    python_requires=">=3.5",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
