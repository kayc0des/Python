import random
import math

randList = []

for i in range(5):
    n = random.randint(1,10)
    randList.append(n)
    #randList.append(random.randrange(1,9))
print(randList)
#for i in randList:
#   print(i)

print("Bubble Sort Algorithm")

i = len(randList) - 1

print(i)

while i > 1:
    j = 0

    while j < i:

        print("\nIs {} > {}".format(randList[j], randList[j+1]))
        
        if randList[j] > randList[j + 1]:

            print("Switch")
            temp = randList[j]
            randList[j] = randList[j + 1]
            randList[j + 1] = temp
        else:
            print("Dont't Switch")
        j += 1

        for k in randList:
            print(k, end=", ")
        print()

    print("END OF ROUND") 
    
    i -= 1
for k in randList:
    print(k, end=", ")
print() 