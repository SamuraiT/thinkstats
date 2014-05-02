#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import unittest
import Pmf
import pmfstats
class TestPmfStats(unittest.TestCase):

    def test_PmfMean(self):
        pmf = Pmf.MakePmfFromList([1,2,3,3,4,4,5,5,5])
        self.assertEqual(pmf.Mean(), pmfstats.PmfMean(pmf))

    def test_PmfVar(self):
        pmf = Pmf.MakePmfFromList([1,2,3,3,4,4,5,5,5])
        self.assertEqual(pmf.Var(), pmfstats.PmfVar(pmf))


if __name__ == '__main__':
    unittest.main()

