# wiki-gensim-word2vector
维基百科语料库做词向量

### 说明

1. 源码github地址：https://github.com/datadevsh/wiki-gensim-word2vector

2. 如果遇到编码问题，参考《维基百科文件解析成中文遇到的变量类型、编码问题》      
https://my.oschina.net/datadev/blog/1836529


3. 如果使用pycharm，可能会发生内存不足。把两个pycharm64.exe.vmoptions文件的-Xmx参数调大。

### 执行时间

1 解析xml  		13分钟
2 繁体2简体  	比较快
3 jieba分词 	27分钟
4 模型训练		22分钟	


### 1. 下载文件
下载pages-articles.xml文件。打开下面的链接，选最近的日期，进入页面后，搜索“pages-articles.xml”。

下载地址：https://dumps.wikimedia.org/zhwiki/


### 2. 解析xml


### 3. 繁体转简体
使用opencc。下载地址如下，下载opencc-1.0.1-win64.7z。
https://bintray.com/package/files/byvoid/opencc/OpenCC
```
.\pencc -i wiki_text.txt -o test.txt -c t2s.json
-i 输入
-o 输出
```
### 4. jieba分词    
### 5. 模型训练    
### 6. 测试    

