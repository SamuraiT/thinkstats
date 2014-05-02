# coding: utf-8
import survey
import __future__
table = survey.Pregnancies()
data_dir = '../chap1/'
table.ReadRecords(data_dir)
print('number of pregnancies: ', len(table.records))

#ex2
def number_of_pregnancies():
    count = 0
    for preg in table.records:
        if preg.outcome == 1:
            count += 1
    return count

#ex3
def categorize_by_birthord():
    first_child = 0
    others = 0
    for preg in table.records:
        if preg.birthord == 1:
            first_child += 1
        elif isinstance(preg.birthord, int):
            others += 1
    return first_child, others

#ex4
def average_pregnancy_length():
    flen, olen = 0,0
    fbabay, obabay = 0,0
    for preg in table.records:
        if preg.birthord == 1:
            flen += preg.prglength
            fbabay += 1
        elif isinstance(preg.birthord, int):
            olen += preg.prglength
            obabay += 1
    return 1.0*flen/fbabay, 1.0*olen/obabay


#2-2

def preg_length_list():
    first = []
    others = []
    for preg in table.records:
        if preg.birthord == 1:
            first.append(preg.prglength)
        elif isinstance(preg.birthord, int):
            others.append(preg.prglength)
    return first,others

def standVar(first,others):
    import thinkstats as stats
    import math
    fmu, fvar = stats.MeanVar(first)
    omu, ovar = stats.MeanVar(others)
    return math.sqrt(fvar),math.sqrt(ovar), fmu, omu

def main():
    fvar, ovar = preg_length_list()
    fsvar, osvar, fmu, omu = standVar(fvar, ovar)
    print("standard var first:{}, others:{}".format(fsvar, osvar) )
    print("mean first:{}, others:{}".format(fmu, omu))
    print("difference of svar {}".format(fsvar - osvar))
    print("difference of mean {}".format((fmu - omu)*7))

if __name__ == '__main__':
    main()
