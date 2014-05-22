#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import random
import myplot
import Pmf
import Cdf

def generate_random_sample(n=1000):
    return [random.random() for i in range(n)]

def main():
    ran = generate_random_sample(1000)
    pmf = Pmf.MakePmfFromList(ran)
    cdf = Cdf.MakeCdfFromPmf(pmf)

    myplot.Cdf(cdf)
    myplot.show()

    myplot.scatter(*cdf.Render())
    myplot.show()

    myplot.Hist(pmf)
    myplot.show()

    myplot.Pmf(pmf)
    myplot.show()




if __name__ == '__main__':
    main()

