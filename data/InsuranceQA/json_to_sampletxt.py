#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 14:29
# @Author  : wtt
# @Site    : 
# @File    : json_to_sampletxt.py
# @Software: PyCharm

#http://www.52nlp.cn/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E4%BF%9D%E9%99%A9%E8%A1%8C%E4%B8%9A%E9%97%AE%E7%AD%94%E5%BC%80%E6%94%BE%E6%95%B0%E6%8D%AE%E9%9B%86
#该中文语料库已划分好train.json;valid.json,test.json,且正负样本比例极其不均匀
#使用./MatchZoo/matchzoo/inputs/preparation.py中的split_train_valid_test进行集合划分,大部分label均为0,故不使用
import json
import codecs

#outfiledir,将所有.json生成一个sample.txt，为了生成一个corpus.txt
#outfiledir1，将不同.json分别生成对应的xxsample.txt，为了生成不同的relation_xx.txt
def Json_to_Sampletxt(questiondir, answerdir,outfiledir,outfiledir1,maxLen,wtyle):

    fout = codecs.open(outfiledir, wtyle, encoding='utf8')#首次写入，如之前有同名文件则删除，非首次写入使用追加写入
    fout1 = codecs.open(outfiledir1, 'w', encoding='utf8')
    fqu = codecs.open(questiondir, 'r', encoding='utf8')
    fanw = codecs.open(answerdir, 'r', encoding='utf8')
    content = json.load(fqu)
    answer = json.load(fanw)
    for index in range(maxLen):
        oneqa = content[str(index)]
        quzh = oneqa['zh']#问题，中文
        anwlst = oneqa['answers']#正确答案的序号列表
        anwnum = len(anwlst)
        negnum = knegsample*anwnum
        neglst = oneqa['negatives']#负样本的序号列表
        for ianw in range(len(anwlst)):
            i = anwlst[ianw]
            oneanw = answer[i]
            anwzh = oneanw['zh']#答案，中文
            #去除\xa0(不间断空白符)等特殊符号
            quzh = "".join(quzh.split())
            anwzh = "".join(anwzh.split())
            fout.write("1\t%s\t%s\n" %(quzh, anwzh))
            fout1.write("1\t%s\t%s\n" % (quzh, anwzh))
        for ineg in range(min(len(neglst), negnum)):
            i = neglst[ineg]
            oneneg = answer[i]
            negzh = oneneg['zh']#负样本，中文
            negzh = "".join(negzh.split())
            fout.write("0\t%s\t%s\n" %(quzh, negzh))
            fout1.write("0\t%s\t%s\n" % (quzh, negzh))
    fout.close()
    fout1.close()
    fqu.close()
    fanw.close()
    return

if __name__ == '__main__':
    #添加负采样频率
    knegsample = 10
    Json_to_Sampletxt(r'./train.json', r'./answers.json', r'./sample.txt', r'./trainsample.txt',12889,'w')
    Json_to_Sampletxt(r'./valid.json', r'./answers.json',r'./sample.txt', r'./validsample.txt',2000,'a+')
    Json_to_Sampletxt(r'./test.json', r'./answers.json', r'./sample.txt', r'./testsample.txt', 2000,'a+')
