#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import random
import matplotlib.pyplot as plt
import math
import Cdf
import myplot
def sample(lambd,n):
    return [random.expovariate(lambd) for i in range(n)]


def main():
    n = 44
    mean = 32.6
    lambd = 1.0/mean
    data = sample(lambd, n)
    cdf = Cdf.MakeCdfFromList(data)
    ccdf = [1 - p for x, p in cdf.Items()]
    plt.plot(cdf.Values(),ccdf)
    plt.xscale('log')
    plt.show()
    

    myplot.Cdf(cdf, complement=True,xscale='linear',yscale='log')
    myplot.show()


if __name__ == '__main__':
    main()

