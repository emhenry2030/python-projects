""" Magic Fortune ball, by Emily Henry
Ask a Yes/No question about your future (or about other things). Inspired by the Magic Ball.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, humor"""

import random, time


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
slowSpacePrint('Magic Fortune Ball, By Emily Henry')
time.sleep(0.5)
slowSpacePrint('Ask me a yes/no question.')
input('> ')

# Displays a brief reply
replies = [
    'LET ME THINK ON THIS...',
    'AN INTERESTING QUESTION...',
    'HMM... ARE YOU SURE YOU WANT TO KNOW..?',
    'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
    'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
    'YES...NO...MAYBE..I WILL THINK ON IT...',
    'AND WAHT WILL YOU DO WHEN YOU HAVE THE ANSWER..?',
    'I SHALL CONSULT MY VISIONS...',
    'YOU MAY WNAT TO SIT DOWN FOR THIS...',
]
slowSpacePrint(random.choice(replies))
input('> ')
print('Ok..')

# Dramatic pause:
slowSpacePrint('.' * random.randint(4, 12), 0.7)

# Give the answer:
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
slowSpacePrint(random.choice(answers), 0.5)

print('I hope you have a great day')
print('Bye')           