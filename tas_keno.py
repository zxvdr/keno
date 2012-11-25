#!/usr/bin/env python

# http://wizardofodds.com/games/keno/calculator/

from __future__ import division
from math import factorial as f

def probability(n, k):
    return (f(60) * f(20) * f(n) * f(80 - n)) / \
            (f(80) * f(k) * f(20 - k) * f(n - k) * f(60 - n + k))

# These are the payout numbers for TAS Keno as of 1/3/2012.
payout = [\
        [0, 3],
        [0, 0, 12],
        [0, 0, 1, 44],
        [0, 0, 1, 4, 115],
        [0, 0, 0, 2, 20, 522],
        [0, 0, 0, 1, 5, 83, 1660],
        [0, 0, 0, 1, 2, 14, 153, 5000],
        [0, 0, 0, 0, 2, 7, 50, 840, 20000],
        [0, 0, 0, 0, 1, 2, 20, 155, 1000, 250000],
        [1, 0, 0, 0, 0, 1, 20, 150, 950, 7000, 50000],
        [3, 1, 0, 0, 0, 1, 5, 35, 260, 2500, 22000, 100000],
        [4, 1, 0, 0, 0, 1, 4, 15, 80, 610, 7000, 70000, 140000],
        [5, 1, 0, 0, 0, 1, 2, 8, 45, 350, 2000, 10000, 80000, 160000],
        [7, 1, 0, 0, 0, 0, 1, 7, 35, 220, 1000, 8500, 25000, 90000, 180000],
        [15, 2, 0, 0, 0, 0, 1, 5, 15, 50, 350, 3000, 20000, 50000, 100000, 200000]
        ]

for selections in range(1, len(payout)+1):
    print "Matches, Prize, Probability, Return"
    r = payout[selections - 1]
    total = 0.0
    for i in range(selections + 1):
        p = probability(selections, i)
        pay = r[i] * p
        print "%2d %6.d - %0.8f%% = %0.8f" % (i, r[i], p, pay)
        total += pay
    print "Total return:", total
    print
