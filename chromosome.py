# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 20:00:05 2018

@author: 8.1
"""
import numpy as np

np.random.seed(75)

import re


class chromosome():
    def __init__(self, genes, id=None, fitness=-1, flatten=False, lengths=None):
        self.id = id
        self.genes = genes
        self.fitness = fitness
    def flatten(arr):
        tmp = []
        tmp3 = []
        filal = []
        for i in range(len(arr)):
            tmp.append(arr[i])
            tmp.append(-1)
    
        string = str(tmp)
        strList = list(re.split(']|,|\[', string))
    
        while ' ' in strList:
            strList.remove(' ')
        while '' in strList:
            strList.remove('')
        str_tmp2 = str(strList)
    
        tmp2 = list(re.split('\'', str_tmp2))
        for i in range(len(tmp2)):
            if (np.remainder(i, 2) == 1):
                tmp3.append(int(tmp2[i]))
        for i in range(len(tmp3)):
            if (tmp3[i] != -1):
                filal.append(tmp3[i])
    
        return filal

    def describe(self):
        print('ID=#{}, fitenss={}, \ngenes=\n{}'.format(self.id, self.fitness, self.genes))


c = chromosome(genes=np.array([1, 2, 3]), id=1, fitness=125.2)
c.describe()

c2 = chromosome(genes=np.array([[1, 2], [2, 1]]).flatten, id=2,
                fitness=140, flatten=True)
c2.describe()

