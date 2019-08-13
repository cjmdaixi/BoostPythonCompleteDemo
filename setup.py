from distutils.core import setup
from distutils.extension import Extension

hello_ext = Extension(
    'hello_ext',
    sources=['hello_ext.cpp'],
    libraries=['boost_python37-mt'],
    extra_link_args=['-static']
)

setup(
    name='hello-world',
    version='0.1',
    ext_modules=[hello_ext])