# setup.py
from setuptools import setup, Extension, find_packages

# Define the C extension module
c_calculator_extension = Extension(
    'calculator._c_calculator',
    sources=[
        'src/c/module.c',
        'src/c/addition/add.c',
        'src/c/subtraction/sub.c',
        'src/c/multiplication/multi.c',
        'src/c/division/div.c',
        'src/c/ophandler/op_handler.c'
    ],
    include_dirs=[
        'src/c/addition',
        'src/c/subtraction',
        'src/c/multiplication',
        'src/c/division',
        'src/c/ophandler'
    ],
    language='c'
)

setup(
    name='cli-calculator-hossam',
    version='0.1.0',
    author='Hossam Ali',
    author_email='hossam.ali@well.ox.ac.uk',
    description='A CLI calculator with a C backend as per the technical assessment.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/calculator', # CHANGE THIS
    package_dir={'': 'src/python'},
    packages=find_packages(where='src/python'),
    ext_modules=[c_calculator_extension],
    entry_points={
        'console_scripts': [
            'calc=calculator.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: C',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    python_requires='>=3.8',
)