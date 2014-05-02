import Pmf
from operator import itemgetter

def Mode_(hist):
    hist = reverse(hist.Items())
    return [val for freq, val in hist if freq == hist[0][0] ]

def reverse(t):
    return sorted([ (v,k) for k,v in t], reverse=True)

def AllMode(hist):
    return sorted(hist.Items(), key=itemgetter(1), reverse=True)

def Mode(hist):
    his = AllMode(hist)
    return [val for val, freq in his if freq == his[0][0]]
