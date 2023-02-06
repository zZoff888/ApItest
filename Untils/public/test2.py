import re
import csv
import jieba
import numpy as np
import pandas as pd

# 生成的字典
cont = {}
for txt in csv_reader:
    stopwords = get_stopwords_list()
    sentence_depart = seg_depart(txt[1])
    sentence_depart = move_stopwords(sentence_depart, stopwords)

    for s in sentence_depart:
        if s not in cont.keys():
            cont[s] = 1
        else:
            cont[s] += 1
# 提取字典中的两列值key是键值，value是cont【key】对应的值
key = list(cont.keys())
value = list(cont.values())

# 利用pandas模块先建立DateFrame类型，然后将两个上面的list存进去
result_excel = pd.DataFrame()
result_excel["词向量"] = key
result_excel["词频"] = value
# 写入excel
result_excel.to_excel(result_excel_location)
