# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 20:05:10 2018

@author: 8.1
"""
import numpy as np

np.random.seed(75)
import random



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

