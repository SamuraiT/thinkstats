#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import Pmf

def PmfMean(pmf):
    mu = 0
    for x,p in pmf.Items():
        mu += x*p
    return mu

def PmfVar(pmf, mu=None):
    if mu is None:
        mu = PmfMean(pmf)
    var = 0
    for x,p in pmf.Items():
        var += p*(x - mu)**2
    return var



if __name__ == '__main__':
    pass

