# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 20:02:43 2018

@author: 8.1
"""
import numpy as np

np.random.seed(75)
import random


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
