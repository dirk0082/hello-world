##print ("Hello World")
##print (13 + 7)

##Find the area of a circle
##Import math
##Use a math function

import math
import random

"""
pi=3.14159265359
r=5
print ("What is the area of a circle with radius 5?")
print ("pi*r^2")
print(pi * r ** 2)
print (math.factorial(8))
"""

"""
a = (random.uniform(0, random.uniform(0, 100)))
print (a)

b = int(a)
print (b)

print (math.factorial(b))
"""

#This program says hello and asks for my name
"""
print('Hello World!')
print('What is your name?') #asks for their name
myName = input()
if myName == 'Alice':
    print('Hi, Alice.')
else:
        print('Hello, stranger')
#print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in one year')
"""
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        print('Sorry,' + name + ' I do not think this is your computer')
        continue
    else:
        while True:
            print('Hi, Joe. Welcome back. What is your password? (Hint: it is a fish)')
            password = input()
            if password == 'swordfish':
                print('access granted')
                exit()
            elif password != 'swordfish':
                print('Joe, please try again.')
                continue
