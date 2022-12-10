"""Hacking Minigame, by Emily Henry
The hacking minigame from "Fallout 3". Find out which seven letter
word is the password by using clues each guess gives you."""



# NOTE: this program requires the sevenletterwords.txt file. You can
# downlaod it from https://inventwithpython/sevenletterwords.txt

import random, sys

# set up the constants:
# The garbage filler characters for the "computer memory" display.
GARBAGE_CHARS = '~@#$%^&*()_+-={}[];:,.<>?/'

