def days():
    ''' Explain the function here
    '''
    for day in 'MTWRFSS':
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')

import matplotlib.pyplot as plt # standard short name
import random

plt.ion() # sets "interactive on": figures redrawn when updated

def picks():
    a = [] # make an empty list

    # Why all the brackets below?
    # a += [  brackets here to add an iterable onto a list      ]
    #    random.choice(   [brackets here to choose from a list] )
    a += [random.choice([1, 3, 10])]

    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.show()

def roll_hundred_pair():
    results = []
    for number in range(101):
        results.append(random.randint(1, 6) + random.randint(1, 6))
    
    plt.hist(range(101), 100, weights=results)
    plt.show()

def dice(amount):
    sum = 0
    for die in range(amount):
        sum += random.randint(1, 6)
    print('Roll was', sum)
    return sum

def hangman_display(guessed, secret):
    return_string = '' 
    for char in secret:
        add = char
        if(not char.lower() in guessed.lower()):
            add = '-'
        return_string += add
    return return_string

def matches(ticket, winner):
    count = 0
    used = []
    for num in ticket:
        for value in winner:
            if(num == value and (not value in used)):
                count += 1
                used += [value]
    return count

def report(guess, secret):
    right_place = []
    wrong_place = []
    matches = []
    for i in range(len(guess)):
        value = guess[i]
        for j in range(len(secret)):
            val = secret[j]
            if(val.lower() == value.lower()):
                if(i == j):
                    right_place.append(val.lower())
                    matches.append(i)
                else:
                    if(not i in matches and not j in matches):    
                        wrong_place.append(val.lower())
    
    wrong_place = list(set(wrong_place))
    return [len(right_place), len(wrong_place)]
    