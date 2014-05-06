#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
from __future__ import print_function
import Pmf

median = lambda x,y: range(x,y+1)[2]
def students_count():
    students = (
            median(5,9),
            median(10,14),
            median(15,19),
            median(20,24),
            median(25,29),
            median(30,34),
            median(35,39),
            median(40,44),
            median(45,49),
            )
    counts = (8,8,14,4,6,12,8,3,2)
    return students,counts

def make_dict(keys, vals):
    size = {}
    for key,val in zip(keys, vals):
        size[key] = size.get(key,0) + val
    return size

def class_size_pmf():
    students, counts = students_count()
    size = make_dict(students, counts)
    return  Pmf.MakePmfFromDict(size, name='class_size_pmf')

def UnbiasPmf(pmf):
    pass

def main():
    class_pmf = class_size_pmf()
    print(class_pmf.Mean())


if __name__ == '__main__':
    main()

