#import the stuff we need
import math
import random
import sys
##print(sys.version)

while True:
    print('Who are you?')
    name = input()
    if name == 'exit':
        sys.exit()
    elif name != 'Joe':
        print('Sorry, ' + name + ' I do not think this is your computer')
        continue
    else:
        while True:
            print('Hi, Joe. Welcome back. What is your password? (Hint: it is a fish)')
            password = input()
            if password == 'swordfish':
                print('Access Granted')
                exit()
            elif password == 'Swordfish':
                print('Access Granted')
                exit()
            elif password == 'exit':
                sys.exit()
            elif password == 'password':
                print('cheeky...but no')
            elif password != 'swordfish':
                print('Joe, please try again.')
                continue


#playing around with math
"""
pi=3.14159265359
r=5
print ("What is the area of a circle with radius 5?")
print ("pi*r^2")
print(pi * r ** 2)
print (math.factorial(8))
"""
"""
total = 0
for num in range(101):
    total = total + num
print(total)
"""
"""
a = (random.uniform(0, random.uniform(0, 100)))
print (a)

b = int(a)
print (b)

print (math.factorial(b))
"""
