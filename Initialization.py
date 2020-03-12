# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 20:01:20 2018

@author: 8.1
"""
import numpy as np

np.random.seed(75)
import random


def Pseudo_Random(n, same, lengths, binary):
    population = []
    # age mosavi bashe ya nabashe farghi nadare chon age mosavi bashe ke oke neveshtim
    # vali age mosavi anbashe 2halat pish miad ya randome ke dg zhen mohem nist chon flatten
    # beshe hamoon chromosomo dorost mikone va vasash zhen mohem nist
    # age ham karbar bede ke bazam flatten mishe
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