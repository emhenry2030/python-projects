""" Magic Fortune ball, by Emily Henry
Ask a Yes/No question about your future (or about other things). Inspired by the Magic Ball.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, humor"""

import random, time, platform
# Make sure you put mysr.py in the same folder as this script
from mysr import voice_to_text


if platform.system() == "Windows":
    import pyttsx3
    engine = pyttsx3.init()
else:
    import os

def talk(text):
    os.system(f'gtts-cli --nocheck "{text}" | mpg123 -q -')
    
def slowSpacePrint(text, interval=0.1):
    """Slowly display text with spaces in between each letter and
    lowercase letter i's."""
    for character in text:
        if character == 'I':
            # I's are displayed in lowercase for style
            print('i ', end='', flush=True)
        else:
            # All other characters are displayed normally:
            print(character + ' ', end='', flush=True)
        time.sleep(interval)
    print() # Print twonewlines at the end.
    print()
    
    
# Prompt for a question:
intro = 'Chatty Magic Fortune Ball, By Emily Henry'
talk(intro)
slowSpacePrint(intro)

time.sleep(0.5)
promptForQuestion = 'Ask me a yes or no question.'

talk(promptForQuestion)
slowSpacePrint(promptForQuestion)
print('listening...')
inp = voice_to_text()
print(f'{inp}')
# Displays a brief reply
replies = [
    'LET ME THINK ON THIS...',
    'AN INTERESTING QUESTION...',
    'HMM... ARE YOU SURE YOU WANT TO KNOW..?',
    'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
    'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
    'YES...NO...MAYBE..I WILL THINK ON IT...',
    'AND WHAT WILL YOU DO WHEN YOU HAVE THE ANSWER..?',
    'I SHALL CONSULT MY VISIONS...',
    'YOU MAY WANT TO SIT DOWN FOR THIS...',
]
choosenReply = random.choice(replies)
talk(choosenReply)
slowSpacePrint(choosenReply)



print('listening...')
inp2 = voice_to_text()
print(f'You just said {inp2}')
talk('Ok')

# Dramatic pause:
slowSpacePrint('.' * random.randint(4, 12), 0.7)

# Give the answer:
talk('I have an answer...')
slowSpacePrint('I have an answer...', 0.2)
time.sleep(1)
answers = [
    'YES, FOR SURE',
    'MY ANSWER IS NO',
    'ASK ME LATER',
    'I AM PROGRAMMED TO SAY YES',
    'THE STARS SAY YES BUT I SAY NO',
    'I DUNNO MAUBE',
    'FOCUS AND ASK ME ONCE MORE',
    'DOUBTFUL, VERY DOUBTFUL',
    'AFFIRMATIVE',
    'YES, THOUGH YOU MAY NOT LIKE IT',
    'NO, BUT YOU MAY WISH IT WAS SO',
]
choosenAnswer = random.choice(answers)
talk(choosenAnswer)
slowSpacePrint(choosenAnswer, 0.5)

talk('I hope you have a great day')
talk('Bye')
print('Bye')


