#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import first as First
import Pmf
import __future__

def generate_pmf():
    first, others, all = First.all_of_preg_length_list()
    fpmf = Pmf.MakePmfFromList(first, name='first')
    opmf = Pmf.MakePmfFromList(others, name='second')
    allpmf =  Pmf.MakePmfFromList(all, name='all')
    return fpmf, opmf, allpmf


def fraction_of_birth(pmf, week_bin):
    pmf = pmf.Copy()
    start, end = week_bin
    total = len(pmf.Values())
    count = 0
    total_prob = 0
    for week, prob in pmf.Items():
        if  start <= week <= end:
            total_prob += prob
            pmf.Remove(week)
    pmf.Set(start, total_prob)
    pmf.Normalize()
    return pmf.Prob(start)


def ProbEarly(pmf):
    """return probability of being born early"""
    return fraction_of_birth(pmf, [0,37])


def ProbOnTime(pmf):
    return fraction_of_birth(pmf, [38,39])

def ProbLate(pmf):
    return fraction_of_birth(pmf, [41,60])

def main():
    for birth in generate_pmf():
        print '\nprob'
        print(birth.name, 'prob early', ProbEarly(birth))
        print(birth.name, 'prob on time', ProbOnTime(birth))
        print(birth.name, 'prob late', ProbLate(birth))
        print

        print 'relative risk'
        for other in generate_pmf():
            if birth.name is other.name:continue
            print(birth.name, other.name,
                    relative_risk(
                    ProbEarly(birth),
                    ProbEarly(other)
                ))
            print(birth.name, other.name,
                    relative_risk(
                    ProbOnTime(birth),
                    ProbOnTime(other)
                ))
            print(birth.name, other.name,
                    relative_risk(
                    ProbLate(birth),
                    ProbLate(other)
                ))




def relative_risk(p, p2):
    return p/p2



if __name__ == '__main__':
    main()

