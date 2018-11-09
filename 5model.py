#-*- coding: utf-8 -*-
# @Describe:
# @File    : word2vec-model.py

import logging
import os.path
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import time
begin = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # if len(sys.argv) < 4:
    #     print(globals()['__doc__'] % locals())
    #     sys.exit(1)
    # inp = "D:/soft/opencc-1.0.1-win64/wiki-jieba-test.txt"
    inp = "D:/soft/opencc-1.0.1-win64/wiki.jieba.txt"
    outp1 ='D:/soft/opencc-1.0.1-win64/wiki.model'
    outp2 = 'D:/soft/opencc-1.0.1-win64/wiki.vector'
    model = Word2Vec(LineSentence(inp),size=400,window=5,min_count=5,workers=multiprocessing.cpu_count())
    model.save(outp1)
    model.wv.save_word2vec_format(outp2,binary=False)

    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("begin",begin)
    print("end  ",end)

#python word2vec-model.py txt model wiki.zh.text.vector
#opencc -i wiki_text.txt -o test.txt -c t2s.json
