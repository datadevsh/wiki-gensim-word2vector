# -*- coding: utf-8 -*-
# @Author  :
# @Email   :
# @Describe:

# 1、解析xml

import logging
import os.path
import sys
from gensim.corpora import WikiCorpus
import time
begin = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s"% ' '.join(sys.argv))

    # if len(sys.argv) > 1:
    #     print(globals()['__doc__'] % locals())
    #     sys.exit(1)
    inp,outp = sys.argv[1:3]
    space = ' '
    i = 0
    output = open(outp,'w',encoding='utf-8')
    wiki = WikiCorpus(inp,lemmatize=False,dictionary={ })
    for text in wiki.get_texts():
        s = space.join(text)+"\n"
        output.write(s)
        i = i+1
        if(i% 10000 == 0):
            logger.info("Saved "+str(i) + " articles")
    output.close()
    logger.info("Finished Saved "+ str(i) +" articles")

    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("begin",begin)
    print("end  ",end)

# python 1process-xml.py zhwiki-20180620-pages-articles.xml.1.49G.bz2 wiki.zh.1.49G.text
