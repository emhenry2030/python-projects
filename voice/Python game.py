# This is a Guess ther Number game
import random

gt= 0

print('Hello, what is your name')
mn = input()


number = random.randint(1,20)
print('Well, ' + mn + ', I am thinking of a number between 1 and 20')


for gt in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    
    
    if guess < number:
        print('Your guess is to low.')
        
    if guess > number:
        print('Your guess is too high')
        
    if guess == number:
        break
    
if guess == number:
    gt = str(gt + 1)
    print('Good job, ' + mn + '! You guessed my number in ' + gt + ' guesses!')
    
if guess != number:
    number = str(number)
    print(' Nope. The number I was thinking of was ' + number +'.')    
    