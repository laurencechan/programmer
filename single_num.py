# coding=utf-8

"""
给定一个数组 AA，除了一个数出现一次之外，其余数都出现三次。找出出现一次的数。

如：\{1, 2, 1, 2, 1, 2, 7\}{1,2,1,2,1,2,7}，找出 77。
"""

n = int(raw_input())

mylist = [int(i) for i in raw_input()]


def fiter_single_num(mylist):
    """算法复杂的方法"""
    mylist_small = list(set(mylist))
    for i in mylist_small:
        mylist.remove(i)
        for j in range(len(mylist)):
            if mylist[j] != i and j < len(mylist) - 1:
                continue
            elif mylist[j] == i:
                break
            elif mylist[j] != i and j == len(mylist) - 1:
                return i


def fiter_single_num1(mylist):
    """算法简单的方法
    思路：对list求set,然后对set做循环i，每次用remove方法除掉原list中的第一个i,对剩下的list再set,如果这个set的长度与之前的set的长度发生了变化（变小）
    证明这个i 就是我们要的那个i
    """
    mylist_small = set(mylist)
    print mylist
    for i in mylist_small:
        mylist.remove(i)
        mylist_new = set(mylist)
        if len(mylist_new) < len(mylist_small):
            return i


if __name__ == '__main__':
    # print mylist
    # print set(mylist)
    # print list(set(mylist))
    # print fiter_single_num(mylist)
    print fiter_single_num1(mylist)
    pass
