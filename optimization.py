import math
import random as random


def randomoptimize(domain, costf):
    best = 999999999
    bestr = None
    for i in range(1000):

        r = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]


        cost = costf(r)


        if cost < best:
            best = cost
            bestr = r

    return bestr


def annealingoptimize(domain, costf, T=10000.0, cool=0.95, step=1):

    vec = [(random.randint(domain[i][0], domain[i][1])) for i in range(len(domain))]

    while T > 0.1:

        i = random.randint(0, len(domain) - 1)


        dir = random.randint(-step, step)


        vecb = vec[:]
        vecb[i] += dir
        if vecb[i] < domain[i][0]:
            vecb[i] = domain[i][0]
        elif vecb[i] > domain[i][1]:
            vecb[i] = domain[i][1]


        ea = costf(vec)
        eb = costf(vecb)
        p = pow(math.e, (-eb - ea) / T)


        if (eb < ea or random.random() < p):
            vec = vecb


        T = T * cool
    return vec
