from eulerproject import PrimeNumbers
import math

prime, integer = 2, 1
lhs = 5601
checkprime = PrimeNumbers()

while True:
    if not checkprime.determinePrime(lhs):
        integerlist = range(1, int(math.sqrt((lhs-2)/2) + 1))
        primelist = [x for x in checkprime.primeList(lhs) if x <= lhs - 2]
        meshtuple = []
        solutionnumber = 0
        for x in primelist:
            for y in integerlist:
                prime, integer = x, y
                if lhs == x + 2 * y**2:
                    solutionnumber += 1
    print(lhs)
    if solutionnumber == 0:
        print("Goldbach was wrong! No solution for %d" % lhs)
        break

    # if sol:
    #     print(lhs)
    # if not sol:
    #     print("Goldbach was wrong! No solution for %d" % lhs)
    #     break
    lhs += 2
