# ChineseWord_seg


一、中文语料库与开发环境

训练集：人民日报98语料库   语言：编程语言为python3.6
CRF工具包：CRF++0.58 (windows)   评测数据：backoff2005

二、实验具体设计与实现

3.1 工具包的获取
本实验采用CRF++工具包，首先从网上下载CRF++0.58工具包 
(![ooops](https://github.com/hooser/ChineseWord_seg/blob/master/pictures/p1.png)

3.2 训练集的准备
CRF++需要下图所示的训练集合形式，故应该将原语料库按4-tag(B,E,S,M)方式标注词，得到最终的训练所需的熟语料。
处理函数如下：
![ooops](https://github.com/hooser/ChineseWord_seg/blob/master/pictures/p2.png)

得到的处理结果如下：
![ooops](https://github.com/hooser/ChineseWord_seg/blob/master/pictures/p3.png)

3.3 训练并得模型
将crf_learn.exe,crf_test.exe,libcrfpp.dll以及训练文件放置文件夹chunking下。
Cmd窗口下进入chunking中，调用crf_learn.exe训练生成crf模型。
![ooops](https://github.com/hooser/ChineseWord_seg/blob/master/pictures/p5.png)

![ooops](https://github.com/hooser/ChineseWord_seg/blob/master/pictures/p4.png)

3.4 测试
首先将测试语料处理成CRF++所需的数据格式，处理函数为：
![ooops](https://github.com/hooser/ChineseWord_seg/blob/master/pictures/p6.png)

利用CRF++的crf_test.exe进行分词处理

![ooops](https://github.com/hooser/ChineseWord_seg/blob/master/pictures/p7.png)

3.5  分词效果评估
使用backoff2005中的pku_test语料评测数据和评测脚本对crf的分词效果进行评测。
在ubuntu环境下测试：
![ooops](https://github.com/hooser/ChineseWord_seg/blob/master/pictures/p8.png)
准确率(precision)：93.8%
召回率（recall）：92.3%
