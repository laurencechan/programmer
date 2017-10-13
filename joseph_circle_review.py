# coding=utf-8

def joseph(n, k):
    if n == 1:
        print "The surviver is %s" % n
        return
    p = 0
    num_list = list(range(1, n + 1))
    while True:
        if len(num_list) == 1:
            break
        p = (p + (k - 1)) % len(num_list)
        kill_num = num_list[p]
        print "This time we kill number %s" % kill_num
        num_list.pop(p)
    print "The surviver is %s" % num_list[0]


if __name__ == '__main__':
    joseph(199, 4)
    pass
