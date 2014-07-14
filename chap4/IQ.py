#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import erf
import myplot
import matplotlib.pyplot as plt

def main():
    x = range(200)
    cdf = [erf.NormalCdf(_x,mu=100,sigma=15) for _x in x]
    print('{:.3f} of people have more than 190IQ '.format((1-cdf[189])*6*(10)**9))
    plt.plot(x, cdf)
    plt.show()
if __name__ == '__main__':
    main()

