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
    y = lambda alpha,xm:((1/xm)**alpha)*pareto(alpha)+(1-(1/xm))
    return [y(alpha,xm) for i in xrange(n)]


def main():
    pareto = paretovariate(1,0.5)
    cdf = Cdf.MakeCdfFromList(pareto)
    myplot.Cdf(cdf)
    myplot.show()

    ccdf = [1-p for x,p in cdf.Items()]
    plt = myplot.pyplot
    plt.plot(cdf.Values(), ccdf)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
if __name__ == '__main__':
    main()

