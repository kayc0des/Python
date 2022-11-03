import random
import math

randList = []

for i in range(5):
    n = random.randint(1,10)
    randList.append(n)
    #randList.append(random.randrange(1,9))
print(randList)
for i in randList:
    print(i)

