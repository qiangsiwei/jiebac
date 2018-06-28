# distutils: language = c++

from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp cimport bool
from Jieba cimport Jieba

cdef class JiebaC:
    cdef Jieba*jbc

    def __cinit__(self, const string& dict_path,
                        const string& model_path,
                        const string& user_dict_path,
                        const string& idfPath,
                        const string& stopWordPath):
        self.jbc = new Jieba(dict_path,model_path,user_dict_path,idfPath,stopWordPath)

    def cut(self, string& sentence, bool hmm):
        cdef vector[string] words
        self.jbc.Cut(sentence,words,hmm)
        return words

    def ucut(self, unicode sentence, bool hmm):
        cdef vector[string] words
        self.jbc.Cut(sentence.encode('utf-8'),words,hmm)
        return [word.decode('utf-8') for word in words]
