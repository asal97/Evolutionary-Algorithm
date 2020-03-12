# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 10:16:07 2018

@author: 8.1
"""
import numpy as np
import random
import math

np.random.seed(75)


class chromosome():
    def __init__(self, genes, id=None, fitness=-1, flatten=False, lengths=None):
        self.id = id
        self.genes = genes
        self.fitness = fitness

        # if you need more parameters for specific problem, extend this class

    #    def flatten_features():

    def describe(self):
        print('ID=#{}, fitenss={}, \ngenes=\n{}'.format(self.id, self.fitness, self.genes))


c = chromosome(genes=np.array([1, 2, 3]), id=1, fitness=125.2)
c.describe()

c2 = chromosome(genes=np.array([[1, 2], [2, 1]]).flatten, id=2,
                fitness=140, flatten=True)
c2.describe()


def Pseudo_Random(n, lengths, binary):
    population = []
    if (binary == False):
        idC = random.sample(range(n), n)
        for i in range(0, n):
            r = random.sample(range(n), lengths[0])
            fit = random.randint(0, 2 * n)
            p = chromosome(genes=np.array(r), id=idC[i], fitness=fit)
            population.append(p)
    else:
        idC = random.sample(range(n), n)
        for i in range(0, n):
            c = []
            for i in range(0, lengths[0]):
                r = random.randint(0, 2)
                c.append(r)
            fit = random.randint(0, 2 * n)
            p = chromosome(genes=np.array(c), id=idC[i], fitness=fit)
            population.append(p)


def truncation(T, population):
    newPop = []
    sorted_fitness = sorted(population, key=lambda x: x.fitness)
    for i in range(0, len(population)):
        r = random.randint((1 - T) * len(population), len(population))
        newPop.append(sorted_fitness[r])
    return sorted_fitness


def tournament(t, population):
    newPop = []
    best = []
    for i in range(0, len(population)):
        for j in range(0, t):
            k = random.randint(0, len(population))
            best.append(population[k])
        sorted_fitness = sorted(best, key=lambda x: x.fitness)
        newPop.append(sorted_fitness[len(best) - 1])
    return newPop


def SUS(R, population):
    newPop = []
    sum = 0
    j = 1
    ptr = random.uniform(0, 1)
    for i in range(0, len(population)):
        sum = sum + R[i]
        while (sum > ptr):
            newPop.append(population[i])
            j = j + 1
            ptr = ptr + 1
    return newPop


def linear_Ranking(rate, population):
    sorted_fitness = sorted(population, key=lambda x: x.fitness)
    s = []
    s.append(0)
    newPop = []
    p = []

    for i in range(0, len(population)):
        p.append((1 / len(population))(rate + (2 - rate - (rate))((i - 1) / (len(population) - 1))))

    for i in range(1, len(population)):
        s.append(s[i - 1] + p[i])

    sSort = s.sort()
    for i in range(0, len(population)):
        r = random.uniform(0, s[-1])
        pUp = 0
        for j in range(0, len(s)):
            if (sSort[j] > r):
                pUp = s[j]
        result = s.index(pUp)
        newPop.append(sorted_fitness[result])

    return newPop


def ERankS(population, c):
    sorted_fitness = sorted(population, key=lambda x: x.fitness)
    s = []
    s.append(0)
    newPop = []
    p = []
    N = len(population)

    for i in range(0, len(population)):
        p.append(((c - 1) / ((c ** N) - 1) * (c ** (N - i))))

    for i in range(1, len(population)):
        s.append(s[i - 1] + p[i])

    sSort = s.sort()
    for i in range(0, len(population)):
        r = random.uniform(0, s[-1])
        pUp = 0
        for j in range(0, len(s)):
            if (sSort[j] > r):
                pUp = s[j]
        result = s.index(pUp)
        newPop.append(sorted_fitness[result])

    return newPop


def Roulette_wheelS(population):
    p = []
    W = 0
    for i in range(0, len(population)):
        W = W + population[i].fitness
    for i in range(0, len(population)):
        p.append((population[i].fitness) / W)
    r = np.random.rand()
    i = 0
    Sum = p[i]
    while (Sum < r):
        i += 1
        Sum += p[i]
    return population[i]


def Roulette_WithStochastic(population):
    newPop = []
    sorted_fitness = sorted(population, key=lambda x: x.fitness)
    wMax = sorted_fitness[-1]
    for i in range(0, len(population)):
        j = random.randint(0, len(population))
        r = np.random.rand()
        pi = (population[j].fitness) / wMax
        if (pi > r):
            newPop.append(population[i])
    return newPop


def single_pointX(p1, p2):
    child = []
    r = random.randint(0, len(p1))
    tmp = p1[r:len(p1)]
    p1[r:len(p1)] = p2[r:len(p1)]
    p2[r:len(p1)] = tmp
    child.append(p1)
    child.append(p2)
    return child


def N_pointX(p1, p2, n):
    child = []
    r = random.sample(range(len(p1)), n)

    c1 = np.zeros(len(p1))
    c2 = np.zeros(len(p1))
    for i in range(0, len(p1) - 2):
        if (np.remainder(i, 2) == 1):
            c1[r[i]:r[i + 1]] = p2[r[i]:r[i + 1]]
            c2[r[i]:r[i + 1]] = p1[r[i]:r[i + 1]]
        else:
            c1[r[i]:r[i + 1]] = p1[r[i]:r[i + 1]]
            c2[r[i]:r[i + 1]] = p2[r[i]:r[i + 1]]

    child.append(c1)
    child.append(c2)
    return child


def Uniform_pointX(p1, p2, pc):
    child = []
    for i in range(0, len(p1)):
        rnd = random.uniform(0, 1)
        if (rnd > pc):
            tmp = p1[i]
            p1[i] = p2[i]
            p2[i] = tmp
    child.append(p1)
    child.append(p2)


def FlatX(p1, p2):
    r1 = []
    r2 = []
    c1, c2 = []
    child = []
    for i in range(0, len(p1)):
        rnd = random.uniform(0, 1)
        r1.append(rnd)
        rnd = random.uniform(0, 1)
        r2.append(rnd)

    for i in range(0, len(p1)):
        c1[i] = (r1[i] * p1[i]) + (1 - r1[i]) * p2[i]
        c2[i] = (r2[i] * p1[i]) + (1 - r2[i]) * p2[i]

    child.append(c1)
    child.append(c2)

    return child


def PMX(l1, l2, ch1, ch2):
    p1 = random.randint(0, len(l1) - 1)
    p2 = random.randint(0, len(l1) - 1)
    while (p2 == p1):
        p2 = random.randint(0, len(l1) - 1)

    first = min(p1, p2)
    second = max(p1, p2)

    ch1[first:second + 1] = l1[first:second + 1]
    ch2[first:second + 1] = l2[first:second + 1]

    pmxC(l1, l2, first, second, ch1)
    pmxC(l2, l1, first, second, ch2)
    child = []
    child.append(ch1)
    child.append(ch2)

    return child


def pmxC(p1, p2, first, second, ch):
    for i in p2[first:second + 1]:
        if (i not in ch):
            posf = p2.index(i)
            pos = p1[posf]
            insert(p1, p2, first, second, ch, i, pos)

    ch = fix(p1, p2, ch)


def insert(p1, p2, first, second, ch, item, pos):
    if (np.count_nonzero(ch) == len(ch)):
        return
    elif (ch[list(p2).index(pos)] != 0):
        insert(p1, p2, first, second, ch, item, p1[list(p2).index(pos)])
    else:
        ch[p2.index(pos)] = item
    return


def fix(p1, p2, ch):
    result = []
    for i in p2:
        if (not (i in ch)):
            result.append(i)
    j = 0
    for i in ch:
        if (i == 0):
            ch[list(ch).index(i)] = result[j]
            j = j + 1
    return ch


def edgeX(p1, p2):
    c1 = np.zeros(len(p1))
    c2 = np.zeros(len(p1))
    ls1 = np.zeros((len(p1), len(p2)))
    for i in range(0, len(p1)):
        if (i < len(p1) - 2):
            ls1[i][0] = p1[i]
            ls1[i][1] = p1[i - 1]
            ls1[i][2] = p1[i + 1]
        else:
            ls1[i][0] = p1[i]
            ls1[i][1] = p1[i - 1]
            ls1[i][2] = p1[0]
    for j in range(0, len(p2)):
        for i in range(0, len(p1)):
            if (ls1[i][0] == p2[j]):
                if (j < len(p2) - 2):
                    if (p2[j - 1] not in ls1[i]):
                        ls1[i][3] = p2[j - 1]
                    if (p2[j + 1] not in ls1[i]):
                        ls1[i][4] = p2[j + 1]
                else:
                    if (p2[j - 1] not in ls1[i]):
                        ls1[i][3] = p2[j - 1]
                    if (p2[0] not in ls1[i]):
                        ls1[i][4] = p2[0]

    c1 = createEdge(p1, ls1, c1)
    c2 = createEdge(p2, ls1, c2)
    child = []
    child.append(c1)
    child.append(c2)
    return child


def createEdge(p, l, c):
    c[0] = p[0]
    for i in range(0, len(l)):
        if (l[i][0] != p[0]):
            if (p[0] in l[i]):
                cip = list(l[i]).index(p[0])
                l[i][cip] = 0

    j = 0
    while (np.count_nonzero(c) < len(c)):
        neighbour = []
        n = 0
        for i in range(0, len(l)):
            if (l[i][0] == c[j]):
                n = i
                for k in range(0, len(l[i])):
                    if (l[i][k] != 0):
                        neighbour.append(l[i][k])
                break
        l = np.delete(l, (n), axis=0)
        count = math.inf
        z = 0
        p = 0
        j += 1
        for i in range(0, len(l)):
            if (l[i][0] == neighbour[z]):
                if (np.count_nonzero(l[i]) <= count):
                    count = np.count_nonzero(l[i])
                    p = i
                    if (z < len(neighbour) - 2):
                        z += 1
                    else:
                        break
        c[j] = l[p][0]
        for i in range(0, len(l)):
            if (l[i][0] != c[j]):
                if (c[j] in l[i]):
                    cip = list(l[i]).index(c[j])
                    l[i][cip] = 0
    return c


# random mutation and inOrder suitable for binary form

def RandomM(c):
    p = random.randint(0, len(c) - 1)
    for i in range(0, p):
        j = random.randint(0, len(c) - 1)
        if (c[j] == 1):
            c[j] = 0
        else:
            c[j] = 1
    return c


def inOrder(pm, c):
    p1 = random.randint(0, len(c) - 1)
    p2 = random.randint(0, len(c) - 1)
    while (p2 == p1):
        p2 = random.randint(0, len(c) - 1)

    f = min(p1, p2)
    s = max(p1, p2)
    for i in range(f, s + 1):
        if (random.uniform(0, 1) < pm):
            if (c[i] == 1):
                c[i] = 0
            else:
                c[i] = 1

    return c


def Twors(c):
    p1 = random.randint(0, len(c))
    p2 = random.randint(0, len(c))
    while (p2 == p1):
        p2 = random.randint(0, len(c) - 1)

    tmp = c[p1]
    c[p1] = c[p2]
    c[p2] = tmp

    return c


def CIM(c):
    p = random.randint(0, len(c))
    c[0:p] = reversed(c[0:p])
    c[p:len(c)] = reversed(c[p:len(c)])

    return c


def RSM(c):
    p1 = random.randint(0, len(c) - 1)
    p2 = random.randint(0, len(c) - 1)
    while (p2 == p1):
        p2 = random.randint(0, len(c) - 1)

    f = min(p1, p2)
    s = max(p1, p2)
    c[f:s] = reversed(c[f:s])
    return c


def reverse(c):
    l = []
    for i in range(0, len(c)):
        l.append(c[i])
    r1 = random.randint(0, len(c) - 1)
    r2 = random.randint(0, len(c) - 1)
    cp1 = l[r1]
    cp2 = l[r2]

    p1 = list(c).index(cp1)
    p2 = list(c).index(cp2)
    c[p1:p2] = reversed(c[p1:p2])


def PSM(population, p):
    i = 1
    while (i < (len(population))):
        r = random.uniform(0, 1)
        if (r < p):
            j = random.randint(0, len(population))
            population[i], population[j] = population[j], population[i]
    return population
