from __future__ import print_function

def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 13
    if(age < AGE_LIMIT):
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print('Minimum age is', AGE_LIMIT)

def report_grade(percent):
    '''Step 6b if-else'''
    if(percent < 80):
        print('A grade of', percent, 'percent does not indiciate mastery.')
        print('Seek extra practice or help.')
    else:
        print('A grade of', percent, 'percent indicates mastery.')
        print('Keep up the good work.')

def vowel(letter):
    vowels = 'aeiou'
    if len(letter) > 1: letter = letter[0]
    return letter.lower() in vowels

def letter_in_word(guess, word):
    return guess.lower() in word.lower()
    
def hint(color, secret):
    return color.lower() in map(str.lower, secret)