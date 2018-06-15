from __future__ import division
import numpy as np
import pandas as pd
import datetime
import operator
from sklearn.cluster import KMeans, MiniBatchKMeans
import sys
import json
from checkClass import checkClass
from nextFit import nextFit
from harmonicAlgo import harmonic
g = []


def k_means(X, n):
    mbk = MiniBatchKMeans(n_clusters=n, batch_size=10000)
    mbk = mbk.fit(X)
    labels = mbk.predict(X)
    C = mbk.cluster_centers_
    return C, mbk


def print_item(a, b):

    return [a, b]


def init(df):
    df = df[:10]
    X = np.array(
        list(zip(df['collection_longitude'], df['collection_latitude'])))
    centr, mb = k_means(X, 3)
    d = {i: X[np.where(mb.labels_ == i)] for i in range(mb.n_clusters)}
    d1 = {i: np.where(mb.labels_ == i)[0] for i in range(mb.n_clusters)}
    k = d.keys()
    v = list(d.values())
    vids = list(d1.values())
    date_time31 = []
    for i in range(0, len(vids)):
        date_time3 = {}
        for j in range(0, len(vids[i])):
            date_time3.update(
                {vids[i][j]: [df['delivery_date'].iloc[vids[i][j]], df['size'].iloc[vids[i][j]]]})
        date_time31.append(date_time3)
    date_time_sorted3 = []
    for diction in date_time31:
        sorted_z = sorted(diction.items(), key=operator.itemgetter(1))
        date_time_sorted3.append(sorted_z)
    c = []
    b = []
    for i in date_time_sorted3:
        e = {}
        for j in i:
            key = j[1][0]
            if key not in e:
                e[key] = []
            e[key].append([j[1][1], j[0]])
        c.append(e)
    for diction in c:
        sorted_x = sorted(diction.items(), key=operator.itemgetter(0))
        # print(len(sorted_x))
        b.append(sorted_x)
    for i in range(0, len(date_time_sorted3)):
        for j in range(0, len(b[i])):
            s = []
            for k in range(0, len(b[i][j][1])):
                s.append(b[i][j][1][k][1])
            g.append(s)


class Bin():
    def convert(self, dic):
        for key in dic:
            if type(dic[key]) == np.int64:
                dic[key] = int(dic[key])
        return dic

    def __init__(self, ids, item):
        self.items = []
        self.dicts = []
        self.attr = []
        self.sum = 0
        self.idv = ids

    def append(self, item, df, dfsize):
        self.dicts.append(df)
        self.sum += dfsize

    def __str__(self):
        return 'geotime_cluster= %s\n(items=%s)\n' % ((str(self.idv)), (str(self.items)))


def pack(values, maxValue, ids, df):
    #values = sorted(values, reverse=True)
    bins = []

    for item in values:
        # Try to fit item into a bin
        for bin in bins:
            if bin.sum + df['size'].iloc[item] <= maxValue:
                # print 'Adding', item, 'to', bin
                bin.append(item, bin.convert(
                    df.iloc[item].to_dict()), df['size'].iloc[item])
                break
        else:
            # item didn't fit into any bin, start a new bin
            # print 'Making new bin for', item
            bin = Bin(ids, item)
            bin.append(item, bin.convert(
                df.iloc[item].to_dict()), df['size'].iloc[item])
            bins.append(bin)

    return bins


def packAndShow(aList, maxValue, ids, df):
    """ Pack a list into bins and show the result """
    # print ('List with sum', sum(aList), 'requires at least', (sum(aList)+maxValue-1)/maxValue, 'bins'0

    bins = pack(aList, maxValue, ids, df)
    print('Total', len(bins), 'Trucks:')
    f = []
    for bin in bins:
        u = []
        u.append(bin.dicts)
        f.append(u)

    return f


def Show(aList, maxValue, ids, df):
    """ Pack a list into bins and show the result """
    # print ('List with sum', sum(aList), 'requires at least', (sum(aList)+maxValue-1)/maxValue, 'bins'0

    bins = pack(aList, maxValue, ids, df)
    print('Total', len(bins), 'Trucks:')

    return len(bins)


def listbhejo():
    a = ['vimal', 'anand', 'baghel']
    return a


def count(df):
    init(df)
    n = 0
    for i in range(0, len(g)):
        aList = g[i]
        n += Show(aList, 1, i, df)
    return n


def calculate(df):
    init(df)
    n = []
    for i in range(0, len(g)):
        aList = g[i]
        x = []
        x = packAndShow(aList, 1, i, df)
        n.append(x)
    print(n)
    return n
