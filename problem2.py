#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to Project Euler's Problem 2: Even Fibonacci Numbers

Classes:

Fibo(base1, base2):
    base1: the first base number of the Fibonacci series
    base2: the second base number of the Fibonacci series

    Methods of Fibo:

    createFibolist(index_limit):
        Create a list of Fibonacci numbers with index_limit elements

        index_limit: the maximum number of elements in the list of
        Fibonacci series

    createFibolistbyValue(value_limit):
        Create a list of Fibonacci numbers where the last element is
        less or equal to value_limit

        value_limit: the maximum allowed value for the last element
        in the list of Fibonacci numbers
"""


class Fibo(object):
    """Fibonacci series generator"""
    def __init__(self, base1, base2):
        self.base1 = base1
        self.base2 = base2

    def createFibolist(self, index_limit):
        """Create a list of Fibonacci series up to an index limit"""
        fibolist = [self.base1, self.base2]
        iterator = 0
        while iterator < index_limit - 2:
            nextbase = fibolist[0 + iterator] + fibolist[1 + iterator]
            fibolist.append(nextbase)
            iterator += 1
        return fibolist

    def createFibolistbyValue(self, value_limit):
        """Create a list of Fibonacci numbers: last element <= value_limit"""
        fibolist = [self.base1, self.base2]
        iterator = 0
        nextbase = 0
        while nextbase < value_limit:
            nextbase = fibolist[0 + iterator] + fibolist[1 + iterator]
            fibolist.append(nextbase)
            iterator += 1
        fibolist.pop(-1)
        return fibolist

    def evenFibolist(self, value_limit):
        """Create a list of even Fibonacci numbers up to value_limit"""
        fibolisteven = Fibo.createFibolistbyValue(self, value_limit)
        for oddnumber in fibolisteven[:]:
            if oddnumber % 2 != 0:
                fibolisteven.remove(oddnumber)
        return fibolisteven

    def evenFiboSum(self, value_limit):
        """Create the sum of all even Fibonacci numbers up to value_limit"""
        evensumlist = Fibo.evenFibolist(self, value_limit)
        evensum = sum(evensumlist)
        return evensum


if __name__ == "__main__":
    # fibolistobj = Fibo(1, 2)
    # fl = fibolistobj.createFibolist(10)
    # print fl
    #
    # fibolistobj2 = Fibo(1, 2)
    # fl2 = fibolistobj2.createFibolistbyValue(4000000)
    # print fl2
    #
    # fibolisteven = Fibo(1, 2)
    # fl3 = fibolisteven.evenFibolist(4000000)
    # print fl3

    fibolistsum = Fibo(1, 2)
    fl4 = fibolistsum.evenFiboSum(4000000)
    print fl4
