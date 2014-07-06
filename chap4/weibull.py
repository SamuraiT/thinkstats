#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import random
import Cdf
import myplot
import math
def weibullvariate(lamdb, k, n=1000):
    """lambd is a scale parameter
        k is a shape parameter"""
    return [random.weibullvariate(lamdb, k) for i in xrange(n)]


def ccdf_list(cdf):
    return [1-p for x,p in cdf.Items()]

def main():
    """when k=1 weibull would be liner"""
    weibull = weibullvariate(1,1)
    cdf = Cdf.MakeCdfFromList(weibull)
    myplot.Cdf(cdf)
    myplot.show()

    ccdf = ccdf_list(cdf)
    plt = myplot.pyplot
    plt.plot(cdf.Values(), ccdf)
    #plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
if __name__ == '__main__':
    main()

