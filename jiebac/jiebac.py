# -*- coding: utf-8 -*-

import os, sys, platform
system = platform.system()
if system == 'Linux':
	from _linux import JiebaC
elif system == 'Darwin':
	from _darwin import JiebaC
else: raise Exception('system not supported.')

get_abs_path = lambda fn: os.path.join(os.path.dirname(__file__),fn)
DICT_PATH      = get_abs_path('dict/jieba.dict.utf8')
HMM_PATH       = get_abs_path('dict/hmm_model.utf8')
USER_DICT_PATH = get_abs_path('dict/user.dict.utf8')
IDF_PATH       = get_abs_path('dict/idf.utf8')
STOP_WORD_PATH = get_abs_path('dict/stop_words.utf8')

jiebac = JiebaC(DICT_PATH,HMM_PATH,USER_DICT_PATH,IDF_PATH,STOP_WORD_PATH)
