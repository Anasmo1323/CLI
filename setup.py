# setup.py
from setuptools import setup, Extension, find_packages
import os
import sys

# Define the version in a single place for easier maintenance
VERSION = '1.0.0'

# Handle Windows compiler issues with a more robust approach
extra_compile_args = []
# Windows-specific configuration
if sys.platform == "win32":
    from distutils import cygwinccompiler

    # Force MinGW if available
    if os.system("gcc --version") == 0:
        cygwinccompiler.get_msvcr = lambda: []
        extra_compile_args = ['-fPIC', '-shared']
    else:
        extra_compile_args = ['/O2']

# Define source and include directories
SRC_DIR = os.path.join('src', 'c')
C_DIRS = [
    '',
    'addition',
    'subtraction',
    'multiplication',
    'division',
    'OpHandler'
]

# Validate source files exist to avoid compilation errors
sources = []
for c_dir in C_DIRS:
    if c_dir == '':
        source_file = os.path.join(SRC_DIR, 'module.c')
    else:
        filename = 'add.c' if c_dir == 'addition' else \
            'sub.c' if c_dir == 'subtraction' else \
                'multi.c' if c_dir == 'multiplication' else \
                    'div.c' if c_dir == 'division' else \
                        'op_handler.c'
        source_file = os.path.join(SRC_DIR, c_dir, filename)

    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Required source file not found: {source_file}")
    sources.append(source_file)

# Create include directories
include_dirs = [os.path.join(SRC_DIR, d) for d in C_DIRS]

# Define the C extension module
c_calculator_extension = Extension(
    'calculator._c_calculator',
    sources=sources,
    include_dirs=include_dirs,
    language='c',
    extra_compile_args=extra_compile_args
)

# Read the contents of the README file with error handling
readme_path = "README.md"
try:
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    print(f"Warning: {readme_path} not found. Using empty description.")
    long_description = ""

setup(
    name='cli-calculator',  # Match pyproject.toml
    version=VERSION,
    author='Ali',
    author_email='alizayan684@gmail.com',
    description='A robust CLI calculator with a C backend.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Anasmo1323/CLI',
    package_dir={'': 'src/python'},
    packages=find_packages(where='src/python'),
    ext_modules=[c_calculator_extension],
    entry_points={
        'console_scripts': [
            'calc=calculator.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.8',
    # Add development dependencies
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.12',
            'black>=21.5b2',
            'flake8>=3.9'
        ],
    },
)
