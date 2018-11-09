#-*- coding: utf-8 -*-
# @Describe:
# @File    : test-jieba.py

# hanlp

import jieba
import jieba.analyse
import codecs,sys
import time

begin = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  #

def cut_words(sentence):
    return " ".join(jieba.cut(sentence)).encode('utf-8')

f=codecs.open('D:/soft/opencc-1.0.1-win64/wiki-ts.txt','r',encoding='utf8')
target = codecs.open("D:/soft/opencc-1.0.1-win64/wiki.jieba.txt",'w',encoding='utf8')
print(" open file")
line_num = 1
line = f.readline()
while line:
    if(line_num % 10000 == 0):
        print('---------------processing',line_num,'articles------------')
    line_seg=" ".join(jieba.cut(line))
    target.writelines(line_seg)
    line_num=line_num + 1
    line = f.readline()
f.close()
target.close()
end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  #
print("begin",begin)
print("end  ",end)
exit()
