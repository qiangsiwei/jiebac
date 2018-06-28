# -*- coding: utf-8 -*-

import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

# for osx
os.environ['CFLAGS'] = '-std=c++11'
extensions = [Extension("jieba_cpy",["jieba_cpy.pyx"],include_dirs=\
    ["/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/"])]
setup(name="jieba_cpy",ext_modules=cythonize(extensions))

# setup(ext_modules=cythonize('jieba_cpy.pyx',language='c++'))

# python setup.py build_ext --inplace
