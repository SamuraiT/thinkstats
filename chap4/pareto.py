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

def paretovariate(alpha, xm=1, n=1000):
    pareto = random.paretovariate
    y = lambda alpha,xm:((1.0/xm)**alpha)*pareto(alpha)+(1-(1.0/xm))
    return [y(alpha,xm) for i in xrange(n)]

def ccdf_list(cdf):
    return [1-p for x,p in cdf.Items()]

def main():
    pareto = paretovariate(1,0.5)
    cdf = Cdf.MakeCdfFromList(pareto)
    myplot.Cdf(cdf)
    myplot.show()

    ccdf = ccdf_list(cdf)
    plt = myplot.pyplot
    plt.plot(cdf.Values(), ccdf)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
if __name__ == '__main__':
    main()

