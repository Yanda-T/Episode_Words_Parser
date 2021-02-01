本项目用于 看美剧积累生词 。

工作原理：myvocab.txt积累了一些自己预先加入的基础单词；过滤字幕时，如果发现存在myvocab.txt中不存在的单词，则根据其出现频数和一阈值进行比较，如果大于阈值，且在给定的目标生词库中，则输出到文件中。

使用流程：
1）当要精细观看某一部美剧/电影时，先在网上（https://www.addic7ed.com/）找到其字幕并放到【files-to-parse】下，然后运行脚本文件， 输出文件在output-files。 
2）检查output-files中的单词：将其中认识的单词补充到myvocab.txt中；不认识的单词添加到 【欧路词典】网页版的个人账号中（https://my.eudic.net/studylist/import/）
3) 将视频和对应的字幕（需要重命名）导入到iPad中，反复观看（1-1-2原则）；
4）（可选）每天早上用iPad上的【欧路词典】背单词

致谢：
感谢 https://github.com/kajweb/dict/ 提供的字典词库

