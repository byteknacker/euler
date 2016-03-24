#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to Project Euler's Problem 2: Even Fibonacci Numbers

Classes:

Fibo(base1, base2, index_limit):
    base1: the first base number of the Fibonacci series
    base2: the second base number of the Fibonacci series
    index_limit: the maximum number of elements in the list of
    Fibonacci series

    Methods of Fibo:

    createFibolist()
        Create a list of Fibonacci numbers with "2 + index_limit"
        elements, where index_limit is an argument of Fibo.
"""


class Fibo(object):
    """Fibonacci series generator"""
    def __init__(self, base1, base2, index_limit):
        self.base1 = base1
        self.base2 = base2
        self.index_limit = index_limit

    def createFibolist(self):
        """Create a list of Fibonacci series up to a limit"""
        fibolist = [self.base1, self.base2]
        iterator = 0
        while iterator < self.index_limit:
            nextbase = fibolist[0 + iterator] + fibolist[1 + iterator]
            fibolist.append(nextbase)
            iterator += 1
        return fibolist

if __name__ == "__main__":
    fibolistobj = Fibo(1, 2, 10)
    fl = fibolistobj.createFibolist()
    print fl
