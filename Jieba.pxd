# distutils: language = c++

from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp cimport bool

# Decalre the class with cdef
cdef extern from "cppjieba/Jieba.hpp" namespace "cppjieba":
    cdef cppclass Jieba:
        Jieba(const string&, const string&, const string&, const string&, const string&) except +
        void Cut(const string&, vector[string]&, bool) const