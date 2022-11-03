#The print statement prints to stdout
#Comments in Python use the hash symbol

#name = input("What is your name? ") #accept input from user
#print("Nice to meet you", name)

#print("Welcome to ChatBot")


sal = 10000.23 
print(type(sal))

#AlU print integer
number = 98
print(f"{number} Battery Street")

number = 3.14159
print(f"Float: {number:.2f}")

str = "Holberton School"
print(str*3)
print(str[:9])

squares = [1, 4, 9, 16, 25] #Data Structure: List
print(squares)

squares.insert(2, 'a') #use insert to insert new item at a given position
print(squares)
print(len(squares))
squares.insert(len(squares), "N") #Same as appending to the end of the list using squares.appemd('N')
print(squares)

iterable = squares[len(squares):]
squares.extend(iterable) #READ MORE HERE
print(squares)

squares.remove('a')
print(squares)

#from collections import deque


