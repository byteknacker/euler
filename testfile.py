L1 = [1, 2, 3, 4]
L2 = ['A', 'B', 'C', 'D']

meshtuple = []

for x in L1:
    for y in L2:
        meshtuple.append([x, y])

print(meshtuple)
