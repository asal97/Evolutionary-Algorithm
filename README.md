
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

# Evolutionary-Algorithm
Computational Intelligence (second project)

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Initialization](#Initialization)
    * [Chromosome](#Chromosome)
    * [Population](#Population)
  * [Crossover](#Crossover)
  * [Mutation](#Mutation)
* [Contributers](#contributers)

<!-- ABOUT THE PROJECT -->
## About The Project
In this assignment,we implemented main parts of genetic algorithms. <br>
we've implemented few of the famous genetic algorithms based on submitted research papers concluded below. 
<br><br>
This assignment includes these parts:
1. [Initialization](#Initialization) (Population and Chromosome)
2. Selection Methods
3. Crossover Methods
4. Mutation Methods
 
## Initialization
In this step we talk about initializing chromosomes and population.
So here are the contents:
1. [Chromosome](#Chromosome)
2. [Population](#Population)

### Chromosome
Here we assume that every problem can be encoded to chromosomes with 1 dimensional vector genes.<br>
But the structure of this genes depends on the problem. We've described most famous ones here so we have 3 types of gene vectors:
1. A binary vector in which 1 represents the existence of the genes and 0 represents non-existence.<br>
Numeric example: <br>
```python
genes = [0, 1, 0, 0, 0, 1, ... , 0]
print(chromosome.genes)
output: [0, 1, 0, 0, 0, 1, ... , 0]
```

2. An integer vector of vectors which each element's represents a vector of the batch of the genes with the same size. something like a flatten 2 dimensional matrix. <br>
```python
genes = [
    [1,2,3],
    [2,1,3],
    [3,2,1],
    [3,1,2]
        ]
chromosome.genes = genes.flatten()
print(chromosome.genes)
output: [1,2,3,2,1,3,3,2,1,3,1,2]
```

3.An integer vector of vectors like state 2, but each element has different size.
```python
genes = [
    [1,2,3,4,5],
    [3,2,1],
    [2,3,1,4],
    [1]
        ]
chromosome.genes = genes.flatten()
print(chromosome.genes)
output: [1,2,3,4,5,3,2,1,2,3,1,4,1]
```
`lengths` is important. So we added another attribute to the `chromosome` class. <br>
```python
chromosome.lengths = [5,3,4,1]
```
So every time you want to apply any operation on these features, you have to do it with respect to `lengths`.<br>

**Note: These numbers are just for demonstration purposes and in real world example, they are data points (features).**

### Population
In the population,chromosomes are like friends and enemies. So all operators in mutation and crossover will be applied on these chromosomes based on nature selection ideas and survival of the fittest.<br><br>
Initialization can help  you to find global optima faster but can even get you stuck in the local optima on the other hand. Hence, it is an important part.<br>
There are some methods to initialize population and they are hyperparameters.<br>
**Hyperparameters** are:
1. **Population Size**
2. **Chromosome Genes**

The most famous one is random initialization.<br>

**Population** initialization:
1. **Pseudo Random**
2. **Quasi Random Sequence**
3. **Centroid Voronoi Tessellation**

* we've only implemented the first method

## Selection
The main purpose of selection phase is to select the fittest individuals and let them pass their genes to the next generation.

These are the selection that we have implemented based on the reference papers:

1. **Truncation Selection**
2. **Tournament Selection**
3. **stochastic Universal Sampling**
4. **Roulette Wheel Selection**
5. **Roulette Wheel Selection with stochastic Acceptance**
6. **Linear Ranking Selection**
7. **Exponential Ranking Selection**

#### 1. Truncation Selection
Use <a href='https://1drv.ms/b/s!ApJ0ieVzUhjimzd5SFGoAOyO7N1x'>This</a> as reference.<br>
More reading:
<a href='http://www.muehlenbein.org/breeder93.pdf'>Muhlenbein's Breeder Genetic Algorithm</a>.

#### 2. Tournament Selection
Use <a href='https://1drv.ms/b/s!ApJ0ieVzUhjimzgexRonyUszQgZQ'>this</a> as reference.

#### 3. Stockasting Universal Sampling
Use <a href='https://1drv.ms/b/s!ApJ0ieVzUhjimz4N8jF3YOuiZRB3'>this</a> as reference.

#### 4. Roulette-wheel Selection
Use <a href='https://1drv.ms/b/s!ApJ0ieVzUhjimz-rnk7Msm7BKOMK'>this</a> as reference.

#### 5. Roulette-wheel Selection with Stocastic Acceptance
Use <a href='https://1drv.ms/b/s!ApJ0ieVzUhjimz-rnk7Msm7BKOMK'>this</a> as reference.

#### 6. Linear Ranking Selection
Use <a href='https://1drv.ms/b/s!ApJ0ieVzUhjimzbRG8A17Ycg2udK'>this</a> and <a href='https://1drv.ms/b/s!ApJ0ieVzUhjimzmCZk6isS3EFksH'>this</a> as reference.

#### 7. Exponential Ranking Selection
Use <a href='https://1drv.ms/b/s!ApJ0ieVzUhjimzpfBTPATw3e9ccF'>this</a> and <a href='https://1drv.ms/b/s!ApJ0ieVzUhjimzu8TjpgpnGhJ5mc'>this</a> as reference.

## Crossover
The idea is to have better individuals at the next generations. So we have to do something. Here we try to use top individuals offspring for next generations as parents. This help us to exploit.

Here is the crossover operators that we've implemented :
1. **Single-point Crossover**
2. **Multi-point Crossover (N-point)**
3. **Uniform Crossover**
4. **Flat Crossover**
5. **Order Crossover (OX)**
6. **Partially Mapped Crossover(PMX)**
7. **Edge Recombination Crossover (ERX)**


Reference:
1. For 1 to 4 operators, use <a href='https://1drv.ms/b/s!ApJ0ieVzUhjim0zBWnOATxVrK5oC'>this</a> link.
2. For 5 to 7 operators use <a href='https://1drv.ms/b/s!ApJ0ieVzUhjim0tAfWp7OZVebBaO'>this</a> link.

## Mutation
The main goal of mutation phase is to change the values of genes in a chromosome randomly and introduce new genetic material into the population,to increase genetic diversity.

implemented methods:

1. **Uniform/Random Mutation**
2. **Inorder Mutation**
3. **Twors Mutation**
4. **Centre inverse mutation (CIM)**
5. **Reverse Sequence Mutation (RSM)**
6. **Partial Shuffle Mutation (PSM)**

* <a href='https://1drv.ms/b/s!ArsLn8kTdaA1ig9o9boJtvw6HgAY'>reference</a>


<!-- CONTACT -->
## Contributers
* [@asal97](https://github.com/asal97) Asal Asgari
* [@Emadpourjafar](https://github.com/Emadpourjafar) Emad Pourjafar 


Project Link: [https://github.com/asal97/Evolutionary-Algorithm](https://github.com/asal97/Evolutionary-Algorithm)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[forks-shield]: https://img.shields.io/github/forks/asal97/Evolutionary-Algorithm
[forks-url]: https://img.shields.io/github/forks/asal97/Evolutionary-Algorithm
[stars-shield]: https://img.shields.io/github/stars/asal97/Evolutionary-Algorithm
[stars-url]: https://img.shields.io/github/stars/asal97/Evolutionary-Algorithm




