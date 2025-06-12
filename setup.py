# setup.py
from setuptools import setup, Extension, find_packages
import os

# Define the C extension module using os.path.join for cross-platform compatibility.
c_calculator_extension = Extension(
    # The full name of the extension module, including the package name.
    'calculator._c_calculator',
    sources=[
        os.path.join('src', 'c', 'module.c'),
        os.path.join('src', 'c', 'addition', 'add.c'),
        os.path.join('src', 'c', 'subtraction', 'sub.c'),
        os.path.join('src', 'c', 'multiplication', 'multi.c'),
        os.path.join('src', 'c', 'division', 'div.c'),
        os.path.join('src', 'c', 'ophandler', 'op_handler.c')
    ],
    # Add include directories so C files can find each other's headers.
    include_dirs=[
        os.path.join('src', 'c'),
        os.path.join('src', 'c', 'addition'),
        os.path.join('src', 'c', 'subtraction'),
        os.path.join('src', 'c', 'multiplication'),
        os.path.join('src', 'c', 'division'),
        os.path.join('src', 'c', 'ophandler')
    ],
    language='c'
)

# Read the contents of the README file for the long description.
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='cli-calculator',
    version='1.0.0',
    author='Ali',
    author_email='alizayan684@gmail.com',
    description='A CLI calculator with a C backend as per the technical assessment.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    # Tell setuptools the root of the Python package source.
    package_dir={'': 'src/python'},
    # Automatically find all Python packages under src/python.
    packages=find_packages(where='src/python'),
    # Specify the C extensions to build.
    ext_modules=[c_calculator_extension],
    # Define the command-line script entry point.
    entry_points={
        'console_scripts': [
            'calc=calculator.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.8',
)
