#-*- coding: utf-8 -*-
# @Describe:
# @File    : test-model.py

from  gensim.models import Word2Vec
import time

begin = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
model = Word2Vec.load('D:/soft/opencc-1.0.1-win64/wiki.model')

# testwords = ['苹果','数学','学术','白痴','篮球']
# for i in range(5):
#     res = model.most_similar(testwords[i])
#     print(testwords[i])
#     print(res)

# 二级类目  '日用百货','收纳整理','家纺','家庭清洁','绿植园艺','厨房用品'
# 上级类目 '其它','床垫','枕头','被子','四件套',

# testwords = ['日用百货','收纳整理','家纺','家庭清洁','绿植园艺','厨房用品']
word = '被子'
# for i in testwords:
#     sim = model.n_similarity(word,i)
#     print(i,sim)


print(model.most_similar(word))

end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("begin",begin)
print("end  ",end)

# 收纳整理 0.16833255
# 家纺 0.14426242
# 家庭清洁 0.066685855
# 绿植园艺 0.028275765
# 厨房用品 0.2936325

# 苹果
# [('apple', 0.5410169363021851), ('苹果公司', 0.4918888807296753), ('咬一口', 0.4741284251213074), ('洋葱', 0.4696866571903229), ('冰淇淋', 0.4614587426185608), ('苹果电脑', 0.45998817682266235), ('黑莓', 0.4557930827140808), ('水果', 0.4546721577644348), ('iphone', 0.44593721628189087), ('草莓', 0.4437388479709625)]
# 数学
# [('微积分', 0.7083343267440796), ('算术', 0.6934097409248352), ('数学分析', 0.663016140460968), ('概率论', 0.6389687061309814), ('数论', 0.6296793222427368), ('逻辑学', 0.6191371083259583), ('几何学', 0.60764479637146), ('数理逻辑', 0.5989662408828735), ('物理', 0.5965093970298767), ('高等数学', 0.5895018577575684)]
# 学术
# [('学术研究', 0.7319201231002808), ('汉学', 0.5988526344299316), ('学术活动', 0.5887891054153442), ('科学研究', 0.5864561796188354), ('学术界', 0.5863242149353027), ('教学研究', 0.5767545700073242), ('教研', 0.5732147097587585), ('学术交流', 0.561274528503418), ('科研', 0.5595779418945312), ('医学教育', 0.5571168661117554)]
# 白痴
# [('疯子', 0.5986206531524658), ('书呆子', 0.5612877607345581), ('骗子', 0.538498044013977), ('怪胎', 0.5305827856063843), ('爱哭鬼', 0.5293511152267456), ('傻子', 0.5216787457466125), ('自恋', 0.5185167789459229), ('变态', 0.5165976285934448), ('自以为是', 0.516464114189148), ('蠢', 0.5106762051582336)]
# 篮球
# [('美式足球', 0.633753776550293), ('橄榄球', 0.6222437620162964), ('排球', 0.5964736938476562), ('棒球', 0.5949814319610596), ('男子篮球', 0.5927262306213379), ('冰球', 0.591292142868042), ('篮球员', 0.5610231161117554), ('篮球运动', 0.5576823353767395), ('足球', 0.5409365892410278), ('橄榄球队', 0.5348620414733887)]
