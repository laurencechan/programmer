# coding=utf-8

"""
类似n 个小孩子围成一圈，数数（1，2，3）数到3的就退出去，一直数一直数，最后剩下的那个孩子的编号

"""


def joseph(n, k):
    if n == 1:
        print "The surviver's number is %s" % n
        return
    p = 0
    chd_list = [i for i in range(1, n + 1)]
    while True:
        if len(chd_list) == 1:
            break
        p = (p + (k - 1)) % len(chd_list)
        kill_num = chd_list[p]
        print "kill number %s" % kill_num
        chd_list.pop(p)
    print "number %s is the surviver" % chd_list[0]


if __name__ == '__main__':
    joseph(19, 4)
    pass
