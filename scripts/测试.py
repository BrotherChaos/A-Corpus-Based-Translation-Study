import jieba,paddle
import jieba.posseg as pseg
txt = "这里桃李芬芳、人才辈出。"
import jieba.posseg as pseg
words = pseg.cut(txt) #jieba默认模式

for word, flag in words:    
    print('%s %s' % (word, flag))