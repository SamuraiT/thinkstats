#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import first as First
def conditional_prob(x, is_first_baby=True, is_all=False):
    first,others, all = First.preg_pmf()
    if is_first_baby:
        pmf = first
    elif is_all:
        pmf = all
    else:
        pmf = others

    for week in pmf.Values():
        if week < x:
            pmf.Mult(week, 0)
    pmf.Normalize()
    return pmf.Prob(x)

def plot():
    import matplotlib.pyplot as plt
    first = []
    others = []
    weeks = range(47)
    for week in weeks:
        first.append(conditional_prob(week))
        others.append(conditional_prob(week, False))
    plt.plot(weeks, first, 'g-', label='first baby')
    plt.plot(weeks, others, 'y-', label='second baby')
    plt.xlabel('week (x)')
    plt.ylabel('conditional probability (p)')
    plt.legend(loc='upper left')
    plt.show()
def main():
    print conditional_prob(39)
    plot()

if __name__ == '__main__':
    main()

