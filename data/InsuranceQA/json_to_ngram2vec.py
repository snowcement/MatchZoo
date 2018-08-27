#!/usr/bin/env python
# -*- coding: utf-8 -*-


#https://github.com/zhezhaoa/ngram2vec
#将该json文件转化为ngram2vec toolkit中类似wiki.zh.text.jian.seg.utf-8格式，用该语料生成词向量

#使用HanLP进行中文分词，分词配置路径/home/ubuntu1/.conda/envs/tf/lib/python3.6/site-packages/pyhanlp/static/
import json
import codecs
from pyhanlp import *
import jieba
import string
from tqdm import tqdm

def Json_to_ngram2vec(corpusdir,outfiledir,maxLen,wtyle):

    fout = codecs.open(outfiledir, wtyle, encoding='utf8')#首次写入，如之前有同名文件则删除，非首次写入使用追加写入
    fcorpus = codecs.open(corpusdir, 'r', encoding='utf8')
    content = json.load(fcorpus)
    #answer.json中索引从1开始
    if r'answers.json' in corpusdir:
        ran = tqdm(range(1, maxLen+1))
    else:
        ran = tqdm(range(maxLen))
    for index in ran:
        oneqa = content[str(index)]
        sentence = oneqa['zh']#问题，中文
        # 去除\xa0(不间断空白符)等特殊符号
        sentence = "".join(sentence.split())

        doc1 = []
        doc = list(jieba.cut_for_search(sentence))
        add_punc = '，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥'
        all_punc = string.punctuation + add_punc
        for word in doc:
            if word not in all_punc:
                doc1.append(word)
        segwithoutpunc = " ".join(doc1)
        fout.write("%s " % segwithoutpunc)

        #print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
        # NLPTokenizer = JClass("com.hankcs.hanlp.tokenizer.NLPTokenizer")
        # #分词结果间由逗号+空格间隔开
        # segstr = str(NLPTokenizer.segment(sentence))
        # #去掉分词结果中的首位[]符号，去掉文本中自带的标点符号，剩余分词结果间用空格连接
        # segwithpunc = segstr.lstrip('[').rstrip(']').split(', ')#带标点的分词结果列表
        # temp = []
        # add_punc = '，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥'
        # all_punc = string.punctuation + add_punc
        # for word in segwithpunc:
        #     if word not in all_punc:
        #         temp.append(word)
        # segwithoutpunc = " ".join(temp)
        # fout.write("%s " % segwithoutpunc)

    fout.close()
    return

if __name__ == '__main__':
    basedir = '/home/ubuntu1/wtt/Code/MatchZoo/data/InsuranceQA/'
    Json_to_ngram2vec(basedir + r'/train.json', r'./insuranceqa.zh.text.jian.seg.utf-8', 12889,'w')
    Json_to_ngram2vec(basedir + r'./valid.json', r'./insuranceqa.zh.text.jian.seg.utf-8', 2000,'a+')
    Json_to_ngram2vec(basedir + r'./test.json', r'./insuranceqa.zh.text.jian.seg.utf-8', 2000,'a+')
    Json_to_ngram2vec(basedir + r'/answers.json', r'./insuranceqa.zh.text.jian.seg.utf-8', 27413, 'a+')
