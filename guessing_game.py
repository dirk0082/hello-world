#!/usr/bin/env python3.

#a simple number guessing game that

import random
answer = random.randint(1, 10)
print(answer)
print('I am thinking of a number btwn 1 and 10')
print('Can you guess it?')
guess = int(input())
if answer == guess:
    print('Great guess!')
else:
    print('WRONG!')
