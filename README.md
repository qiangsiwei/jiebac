jiebac
========

使用`cython`对cppjieba进行了封装    
https://github.com/yanyiwu/cppjieba    
相对python版本约有5~10倍速度提升，内存占用稳定

使用方法示例

```python
# encoding=utf-8

from jiebac import jiebac as jieba

text = u'分词对于研究和应用中文自然语言处理的童鞋来说，都是一个非常非常基础的部件，分词的质量直接影响到后续词性标注、命名实体识别、句法分析等部件的准确性。'
print jieba.ucut(text,True)
```

性能测试如下

对于python实现（https://github.com/fxsjy/jieba）

![https://github.com/qiangsiwei/jiebac/blob/master/data/perf.png](https://github.com/qiangsiwei/jiebac/blob/master/data/perf.png)
