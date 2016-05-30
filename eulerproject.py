import math

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
