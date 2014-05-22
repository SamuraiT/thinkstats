#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import survey
import sample
gram = 28.3495

def Median(cdf):
    return cdf.Value(0.5)

def percentile(cdf, rank):
    return cdf.Value(rank)

def Interquartile(cdf):
    return percentile(cdf, .75) - percentile(cdf, .25)


def birth_weight():
    data_dir = '../chap1/'
    preg = survey.Pregnancies()
    preg.ReadRecords(data_dir)
    cdf = sample.weight_cdf(preg)
    print Median(cdf)*gram
    print Interquartile(cdf)*gram
    print percentile(cdf, .25)*gram, percentile(cdf, .75)*gram
    print Median(cdf)
    print Interquartile(cdf)
    print percentile(cdf, .25), percentile(cdf, .75)


if __name__ == '__main__':
    birth_weight()
