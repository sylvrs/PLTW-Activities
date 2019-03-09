import random

def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def guess_letter():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return random.choice(list(letters))