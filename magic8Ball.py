import random
import sys
def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Very doubtful'

while True:
    r = random.randint(1, 9)
    fortune = get_answer(r)
    print('Hello there. I am the magic 8 ball. Ask me a question')
    important_question = input()
    if important_question == 'STOP':
        break
    if len(important_question) < 2:
        print('Do you not have a question? - Try again')
    elif len(important_question) >= 2:
        print(fortune)
    continue
sys.exit()
