# coding: utf-8
import survey
table = survey.Pregnancies()
table.ReadRecords()
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



