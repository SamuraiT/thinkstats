#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import relay
import Pmf
import myplot

def BiasPmf(observer_speed, original_pmf):
    """return distribution of speed
    as seen by runner who runs with (speed)"""
    pmf = original_pmf.Copy(name='runner')
    for speed,p  in pmf.Items():
        pmf.Mult(speed, abs(speed - observer_speed))
    pmf.Normalize()
    return pmf

def main():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    pmf = Pmf.MakePmfFromList(speeds, 'speeds')
    pmf = BiasPmf(7,pmf)
    myplot.Hist(pmf)
    #myplot.Show(title='PMF of observed speed',
    #           xlabel='speed (mph)',
    #           ylabel='probability')
    myplot.Save(
                formats=['png'],
                root='runner',
                title='PMF of observed speed',
               xlabel='speed (mph)',
               ylabel='probability')


if __name__ == '__main__':
    main()

