# -*-coding: utf-8 -*-
#参照右边网址修改而得 http://movecloud.me/2015/05/06/tsp-dp/
import math
import sys
import timeit

MAX_LENGTH = 5000000.0

# 构建可计算图
def build_graph(path):
    """ 读入各个城市的位置信息 """
    with open(path) as f:
        lines = f.readlines()
        pos_list = [ (float(line.split()[0]),float(line.split()[1])) for line in lines]
        N = len(pos_list)
        dist_dict = [ [ MAX_LENGTH for i in xrange(N+1) ] for j in xrange(N+1) ]
        for i in xrange(N):
            for j in xrange(i, N):
                dist_dict[j][i]=dist_dict[i][j] = math.sqrt((pos_list[i][0]-pos_list[j][0])**2 + (pos_list[i][1]-pos_list[j][1])**2)

        for i in xrange(N+1):
            dist_dict[i][N] ,dist_dict[i][0] =dist_dict[i][0] ,dist_dict[i][N]

    return dist_dict


def neighbor(count, N):
    for i in xrange(N):
        c = 1 << i
        if (c & count):
            yield (i+1, (c ^ count)) #记二进制最低位 index=1,而非index=0


# 具有相同结点数的下一个集合
def gosper_hack(x):
    """
    参见:
        (http://read.seas.harvard.edu/cs207/2012/?p=64)
        0111 => 1011
        0101 => 0110
        ...
    """
    c = (x & -x)
    r = x + c
    return (((r ^ x) >> 2) / c) | r


def tsp_dp(dist_dict):
    N = len(dist_dict)-1 #去除出发城市
    MAX_INDEX = 1 << N
    s = "1"

    records = [ {} for i in xrange(1 << N) ]    # 2**N == 1 << N
    count = int(s, 2)
    for i in xrange(1,N+1):
        if count >= MAX_INDEX:
            break
        records[count][i] = (dist_dict[0][i],[0,i]) # 对count代表的集合，从0出发，到达i点的单回路的距离
        count=gosper_hack(count)

    for i in range(2, N+1):
        s = s + "1"
        count = int(s, 2)
        while (count < MAX_INDEX):
            for (j, nb) in neighbor(count, N):
                for (__, dnb) in neighbor(nb, N):
                    records[dnb] = []   # 释放空间，虽然增大了一倍的运算时间

                for (end, (length,footprint)) in records[nb].iteritems():
                    if j != end:
                        new_len =  length + dist_dict[end][j]
                        if new_len < records[count].get(j,(MAX_LENGTH,))[0]:
                            records[count][j] = (new_len, footprint+[j])

            count = gosper_hack(count)

    return records[int(s,2)][N]


def tsp_prob():
    dd = build_graph("tsp.txt")
    print tsp_dp(dd)

if __name__ == "__main__":
    t = timeit.timeit("tsp_prob()", setup="from __main__ import tsp_prob", number = 1)
    print "time:", t
