import Pmf

def PmfRemainingLifeTime(lifetime, age):
    """
    arg:(lifetime) is the pmf obj of lifetime
    arg:(age)
    return pmf of remaining lifetime
    """
    remain = lifetime.Copy()
    for val in remain.Values():
        if age > val:
            remain.Mult(val,0)
    remain.Normalize()
    return remain


def main():
    import myplot
    pmf = Pmf.MakePmfFromList([1,2,3,3,4,4,5,5,5,6,6,7])
    remain = PmfRemainingLifeTime(pmf, age=4)
    myplot.Hist(pmf)
    myplot.Show()

    myplot.Hist(remain)
    myplot.Show()

if __name__ == '__main__':
    main()

