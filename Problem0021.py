# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:27:16 2017

@author: michael
"""

"""
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math

def divisors(n):
    divs = []
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            yield int(i)
            if i*i != n:
                divs.append(n/i)
    for div in reversed(divs):
        yield int(div)

def sumDivisors(n):
    return int(sum(divisors(n))-n)
    
def amicable(ceiling):
    pairs = []
    sumDivs = [0]
    for x in range(1, ceiling):
        sumDivs.append(int(sumDivisors(x)))
    for i in range(ceiling):
        if i == sumDivisors(sumDivs[i]) and sumDivs[i] != i:
            pairs.append(i)
    return set(pairs)
    
    
    