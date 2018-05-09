from __future__ import division
from __future__ import absolute_import

import numpy as np
from scipy import stats
import math


class DecisionTree:

    def __init__(self, val):
        self.val = val      # val is either a feature or a T/F leaf node
        self.children = {}  # val:tree mapping or just empty for a leaf

    def test(self, X_test, y_test, splits=[]):
        if self.children:
            res = []
            for v in self.children.keys():
                res.append(self.children[v].test(X_test, y_test, splits + [(self.val, v)]))
            return np.concatenate(res)
        else:
            idx = True
            for (x,val) in splits:
                idx = idx & (X_test[:,x] == val)
            return y_test[idx] == self.val


def get_significant_feature(X, y, used_features):
    allowed_features = set(range(X.shape[1])) - used_features
    n = X.shape[0]
    min_H = float('inf')
    sig_feature = None
    for f in allowed_features:
        vals, counts = np.unique(X[:,f], return_counts=True)
        # H = \sum prob_val * H(val)
        H = 0
        for i, val in enumerate(vals):
            prob = counts[i]/n
            ys = y[X[:,f] == val]
            counts_p = [ sum(ys == True), sum(ys == False) ]
            tot_p = len(ys)
            h = sum(-(p/tot_p) * math.log(p/tot_p, 2) for p in counts_p if p > 0)
            H += prob * h

        if H < min_H:
            sig_feature = f
            min_H = H
    return sig_feature


def _fit(X, y, prev_splits, depth):
    # filter first
    idx = np.tile(True, y.shape)
    for (x,val) in prev_splits:
        idx = idx & (X[:,x] == val)

    if depth == 1 or len(np.unique(y[idx])) <= 1:
        # get leaf node
        ans = stats.mode(y[idx])[0][0] if len(y[idx]) > 0 else 1
        dt = DecisionTree(ans)
    else:
        Xt = X.copy()[idx,:]
        yt = y.copy()[idx]
        used_features = set(split[0] for split in prev_splits)
        ftr = get_significant_feature(Xt, yt, used_features)
        dt = DecisionTree(ftr)
        vals = np.unique(X[:,ftr])
        for val in vals:
            dt.children[val] = _fit(X, y, prev_splits + [(ftr, val)], depth-1)
    return dt


def fit(X, y):
    dt = _fit(X, y, [], 4)
    # import ipdb; ipdb.set_trace()
    res = dt.test(X, y)
    print(sum(res)/len(res))
