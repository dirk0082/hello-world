
#a game of go fish with the terminal

#could elaborate by having terminal randomly asking for cards
#in the player's hand

import random

one = random.randint(1,10)
two = random.randint(1,10)
three = random.randint(1,10)
four = random.randint(1,10)
five = random.randint(1,10)

hand = [str(one), str(two), str(three), str(four), str(five)]
print('Hi! Let us play a game of go fish')
print('If you need to give up, just say: I give up')
while len(hand) > 0:
    print(hand)
    print('Which card are you a looking for?')
    card = input()
    if card == 'I give up':
        break
    if card in hand:
        print('Good guess! You can have my ' + card)
        hand.remove(card)
    else:
        print('Go Fish!')
if len(hand) == 0:
    print('Good game, I am all out of cards!')
