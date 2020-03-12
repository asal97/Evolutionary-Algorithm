# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 20:03:46 2018

@author: 8.1
"""
import numpy as np

np.random.seed(75)
import random
import math

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


def OX(parent1, parent2):
    r = random.sample(range(len(parent1)), 2)  # Choose 2point for breaking
    r.sort()
    child1 = np.ones(len(parent1)) * -1  # tolide bache aval
    child2 = np.ones(len(parent1)) * -1  # tolide bache dovom

    for i in range(0, r[1] - r[0]):  # enteghale tikehaii ke bayad bedoone taghir montaghel she
        child1[r[0] + i] = parent1[r[0] + i]
        child2[r[0] + i] = parent2[r[0] + i]

    rem1 = parent1[0:r[0]] + parent1[r[1]:len(parent1)]  # adadi ke baraye bache aval mojaz be entekhabim
    secIndex = index = r[1]  # index for child and secIndex for parent
    for i in range(0, len(parent1)):
        if (parent2[secIndex] in rem1):  # Create first child
            child1[index] = parent2[secIndex]
            index = np.remainder((index + 1), len(parent1))
            secIndex = np.remainder((secIndex + 1), len(parent1))
        else:
            secIndex = np.remainder((secIndex + 1), len(parent1))

    rem2 = parent2[0:r[0]] + parent2[r[1]:len(parent2)]  # adadi ke baraye bache dovom mojaz be entekhabim
    secIndex = index = r[1]
    for i in range(0, len(parent1)):
        if (parent1[secIndex] in rem2):  # Create second child
            child2[index] = parent1[secIndex]
            index = np.remainder((index + 1), len(parent1))
            secIndex = np.remainder((secIndex + 1), len(parent1))
        else:
            secIndex = np.remainder((secIndex + 1), len(parent1))

    print(child1)
    print(child2)


def edgeX(p1,p2):
    c1=np.zeros(len(p1))
    c2=np.zeros(len(p1))
    ls1=np.zeros((len(p1),len(p2)))
    for i in range(0,len(p1)):
        if(i<len(p1)-2):
            ls1[i][0]=p1[i]
            ls1[i][1]=p1[i-1]
            ls1[i][2]=p1[i+1]
        else:
            ls1[i][0]=p1[i]
            ls1[i][1]=p1[i-1]
            ls1[i][2]=p1[0]
    for j in range(0,len(p2)):
        for i in range(0,len(p1)):
            if(ls1[i][0]==p2[j]):
                if(j<len(p2)-2):
                    if(p2[j-1] not in ls1[i]):
                        ls1[i][3]=p2[j-1]
                    if(p2[j+1] not in ls1[i]):
                        ls1[i][4]=p2[j+1]
                else:
                     if(p2[j-1] not in ls1[i]):
                        ls1[i][3]=p2[j-1]
                     if(p2[0] not in ls1[i]):
                        ls1[i][4]=p2[0]
                            
    c1=createEdge(p1,ls1,c1)
    c2=createEdge(p2,ls1,c2)
    child=[]
    child.append(c1)
    child.append(c2)
    return child
  
def createEdge(p,l,c):
    c[0]=p[0]
    for i in range(0,len(l)):
        if(l[i][0]!=p[0]):
            if(p[0] in l[i]):
                cip=list(l[i]).index(p[0])
                l[i][cip]=0

    j=0
    while(np.count_nonzero(c)<len(c)):
       neighbour=[]
       n=0
       for i in range(0,len(l)):
           if(l[i][0]==c[j]):
               n=i
               for k in range(0,len(l[i])):
                   if(l[i][k]!=0):
                       neighbour.append(l[i][k])       
               break
       l=np.delete(l,(n),axis=0)   
       count=math.inf
       z=0
       p=0
       j+=1
       for i in range(0,len(l)):
          if(l[i][0]==neighbour[z]):
              if(np.count_nonzero(l[i])<=count):
                  count=np.count_nonzero(l[i])
                  p=i
                  if(z<len(neighbour)-2):
                      z+=1
                  else:
                      break
       c[j]=l[p][0] 
       for i in range(0,len(l)):
           if(l[i][0]!=c[j]):
              if(c[j] in l[i]):
                cip=list(l[i]).index(c[j])
                l[i][cip]=0 
    return c
     

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
