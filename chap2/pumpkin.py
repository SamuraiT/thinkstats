import thinkstats as stats
import math

def Pumpkin(t):
    mu, var = stats.MeanVar(t)
    return mu, var, math.sqrt(var)

if __name__ == '__main__':
    t = [0.5, 0.5, 1.5, 1.5, 96]
    print(Pumpkin(t))
