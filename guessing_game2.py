
#guessing game that changes randomly by -1, 0, or 1
# if you guess incorrectly

import random
import sys
answer = random.randint(1, 10)

def attempt():
    global answer
    #prints answer to verify program is working
    print('answer: ' + str(answer))
    print('I am ready for guess')
    guess = int(input())
    if answer == guess:
        print('Great guess!')
        sys.exit()
    else:
        print('WRONG!...try again')
        adjust_factor = random.randint(-1,1)
        answer = answer + adjust_factor
        print('adjust factor: ' + str(adjust_factor))
        if answer < 1:
            answer = 1
        if answer > 10:
            answer = 10

print(answer)
print('I am thinking of a number btwn 1 and 10')
while True:
    attempt()
    print(answer)
