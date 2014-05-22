#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import Cdf
import random
import survey
import myplot
def Sample(cdf, n):
    value = []
    for i in range(n):
        ran = random.random()
        value.append(cdf.Value(ran))
    return value

def weight_cdf(preg):
    weight = []
    for record in preg.records:
        wgt = record.totalwgt_oz
        if wgt == 'NA':continue
        weight.append(wgt)
    cdf = Cdf.MakeCdfFromList(weight)
    return cdf

def main():
    data_dir = '../chap1/'
    preg = survey.Pregnancies()
    preg.ReadRecords(data_dir)
    cdf = weight_cdf(preg)
    myplot.Cdf(cdf)
    myplot.show()

    sample = Sample(cdf, 1000)
    cdf_sample = Cdf.MakeCdfFromList(sample)
    myplot.Cdf(cdf_sample)
    myplot.Show()

if __name__ == '__main__':
    main()

