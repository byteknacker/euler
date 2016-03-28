#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

""" Solution to Project Euler's Problem 7: 10001st Prime
"""


class PrimeNumbers(object):
    def __init__(self):
        pass

    def determinePrime(self, testnumber):
        primestate = True
        list1 = range(3, int(math.sqrt(testnumber)) + 1)
        divisor_list = [element for element in list1 if element % 2 != 0]
        divisor_list.insert(0, 2)
        for divisor in divisor_list:
            modulus = testnumber % divisor
            if modulus == 0:
                primestate = False
                divisor = testnumber
        return primestate

    def primeList(self, index_limit):
        listofprimes = [2]
        test_integer = 3
        index_j = 0
        while index_j < index_limit:
            state = self.determinePrime(test_integer)
            if state is True:
                listofprimes.append(test_integer)
            else:
                pass
            test_integer += 1
            index_j = len(listofprimes)
        return listofprimes

    def lastPrimeinList(self, index_limit):
        listprimes = self.primeList(index_limit)
        lastprime = listprimes.pop(-1)
        return lastprime

    def lastPrime(self, index_limit):
        test_integer = 3
        index_j = 0
        while index_j < index_limit:
            state = self.determinePrime(test_integer)
            if state is True:
                index_j += 1
            else:
                pass
            test_integer += 1
        result_integer = test_integer - 1
        return result_integer

if __name__ == "__main__":
    prime = PrimeNumbers()
    print prime.lastPrime(10000)
