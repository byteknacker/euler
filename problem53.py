#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Combinatorics(object):
    def nCr(self, n, r):
        numerator = int(math.factorial(n))
        denominator1 = int(math.factorial(r))
        denominator2 = int(math.factorial((n - r)))
        denominator = denominator1 * denominator2
        result = numerator / denominator
        return result

    def comboList(self, n_limit):
        combolist = []
        n = 4
        while n <= n_limit:
            for r in range(2, n-1):
                coeff = self.nCr(n, r)
                coeff = int(coeff)
                if coeff > 1000000:
                    combolist.append(coeff)
                else:
                    pass
            n += 1
        return combolist

if __name__ == "__main__":
    combo = Combinatorics()
    cn = list(combo.comboList(100))
    print len(cn)
