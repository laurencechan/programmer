# coding=utf-8
"""给定由大写，小写字母和空格组成的字符串，返回 最后 一个单词的长度。

如果输入中不存在单词，返回 00。"""
sentence = raw_input()

def last_len(sentence):
    mylist = sentence.split()
    if mylist:
        return len(mylist[-1])
    return 0

if __name__ == '__main__':
    print last_len(sentence)
    pass