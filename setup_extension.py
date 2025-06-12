from setuptools import setup, Extension
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

extension = Extension(
    'calculator._c_calculator',
    sources=[
        os.path.join(base_dir, 'src', 'c', 'addition', 'add.c'),
        os.path.join(base_dir, 'src', 'c', 'subtraction', 'sub.c'),
        os.path.join(base_dir, 'src', 'c', 'multiplication', 'multi.c'),
        os.path.join(base_dir, 'src', 'c', 'division', 'div.c'),
        os.path.join(base_dir, 'src', 'c', 'OpHandler', 'op_handler.c'),
        os.path.join(base_dir, 'src', 'c', 'module.c')
    ],
    include_dirs=[os.path.join(base_dir, 'src', 'c')]
)

setup(
    name='c_extension_builder',
    version='0.1',
    ext_modules=[extension],
)
