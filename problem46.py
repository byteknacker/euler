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
                meshtuple.append([x, y])
        sol = [t for t in meshtuple if t[0] + 2 * t[1]**2 == lhs]
    if sol:
        print(lhs)
    if not sol:
        print("Goldbach was wrong! No solution for %d" % lhs)
        break
    lhs += 2
