# encoding: utf-8

import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

from snownlp import SnowNLP

text1 = "这个人脾气真坏，动不动就骂人"
text2 = "这个人脾气真好，经常笑"

s1 = SnowNLP(text1.encode('utf-8'))
s2 = SnowNLP(text2.encode('utd-8'))

print(text1, s1.sentiments)
print(text2, s2.sentiments)