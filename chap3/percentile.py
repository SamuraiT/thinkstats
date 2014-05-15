#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""

def PercentileRank(scores, your_score):
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1
    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank

def Percentile(scores, percentile_rank):
    i = (percentile_rank * len(scores)/ 100 ) - 1
    return scores[int(i)]


def main():
    scores = [55, 56, 77, 88, 99]
    rank = PercentileRank(scores,88)
    print(rank)
    print(Percentile(scores, rank))


if __name__ == '__main__':
    main()

