#!/usr/bin/env python3

import articles
import numpy as np
import matplotlib.image as mpimg


def normalize(*args):
    r = []
    for a in args:
        s = sum(a)
        if not s:
            r.append([0]*(len(a)-1) + [1])
        else:
            r.append(a/s)
    return r


def rgb_hist(fn):
    i = mpimg.imread(fn)
    k = [[j for j in px] for row in i for px in row if sum(px)<180*3 and px[0]!=px[1] and px[0]!=px[2]] # drop white and light-gray pixels
    r = [j[0] for j in k]
    g = [j[1] for j in k]
    b = [j[2] for j in k]
    rh,_ = np.histogram(r, range=(0,255))
    gh,_ = np.histogram(g, range=(0,255))
    bh,_ = np.histogram(b, range=(0,255))
    rh,gh,bh = normalize(rh,gh,bh)
    return [[int(v*100) for v in rgb] for rgb in zip(rh,gh,bh)]


if __name__ == '__main__':
    for artid,art in articles.all_articles.items():
        img_fn = art['imgs'][-1][1:]
        print('%s (%s)...' % (artid,img_fn))
        art['histogram'] = rgb_hist(img_fn)
    articles.save_articles()
