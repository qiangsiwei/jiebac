# -*- coding: utf-8 -*-

import re, glob, time, jieba
from tqdm import tqdm
import __builtin__
from timeit import timeit
# from jieba_cpy import JiebaC

def test_package():
	from jiebac import jiebac as jieba
	text = u'分词对于研究和应用中文自然语言处理的童鞋来说，都是一个非常非常基础的部件，分词的质量直接影响到后续词性标注、命名实体识别、句法分析等部件的准确性。'
	print jieba.ucut(text,True)

def test_perf(dirn):
	DICT_PATH      = "dict/jieba.dict.utf8";
	HMM_PATH       = "dict/hmm_model.utf8";
	USER_DICT_PATH = "dict/user.dict.utf8";
	IDF_PATH       = "dict/idf.utf8";
	STOP_WORD_PATH = "dict/stop_words.utf8";
	jb = jieba; jb.cut('init',HMM=True)
	from jiebac import jiebac as jbc
	text = ''
	for fn in glob.glob(dirn)[:1000]:
		text += open(fn).read().decode('utf-8')
	for cmd in ('jb.lcut(sentence,HMM=False)',\
				'jbc.ucut(sentence,hmm=False)'):
		for length in (10,20,50,100,200,500,1000):
			sec = 0
			for i in tqdm(range(len(text)/length)):
				sentence = text[i*length:(i+1)*length]
				__builtin__.__dict__.update(locals())
				sec += timeit(stmt=cmd,number=1)
			print cmd, length, sec
	return sec

def plot_perf():
	import numpy as np
	import matplotlib.pyplot as plt
	fig,(ax1,ax2) = plt.subplots(1,2,figsize=(8,3))
	fig.subplots_adjust(left=0.1,bottom=0.18,wspace=0.1)
	x = [10,20,50,100,200,500,1000]
	rest = [[9.411,7.805,6.837,6.352,6.112,5.921,5.870],
			[1.671,1.302,1.004,0.894,0.843,0.767,0.744],
			[8.267,6.815,5.883,5.509,5.327,5.191,5.067],
			[1.779,1.303,0.945,0.861,0.769,0.672,0.649]]
	total_width,n = 0.8,2; width = total_width/n
	ax1.bar(np.arange(len(x))-.5*width,rest[0],width=width,fc='y',label='jieba',tick_label=x)
	ax1.bar(np.arange(len(x))+.5*width,rest[1],width=width,fc='g',label='jiebac')
	ax2.bar(np.arange(len(x))-.5*width,rest[2],width=width,fc='y',label='jieba',tick_label=x)
	ax2.bar(np.arange(len(x))+.5*width,rest[3],width=width,fc='g',label='jiebac')
	ax1.set_title('HMM=True'); ax2.set_title('HMM=False')
	ax1.set_ylim([0,10]); ax2.set_ylim([0,10])
	ax1.set(xlabel='num of char per sentence',ylabel='total time used (second)')
	plt.legend()
	plt.show()

if __name__ == '__main__':
	test_package()
	plot_perf()
	pass
