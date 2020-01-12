hand = ['one', 'two', 'three', 'four', 'five']
print('Hi! Let us play a game of go fish')
print('If you need to give up, just say: I give up')
while len(hand) > 0:
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
