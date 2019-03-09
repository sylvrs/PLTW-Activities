import random
 
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''
    This function is a small text game.
    In this game, you provide a list of names(all as strings) as the parameter.
    The user must guess who 'won' the lottery among the names given. 
    
    Returns the guesses count before they found the right answer.
    '''
    winner = random.choice(players) 

    ####
    # Prints 'Guess which of these people won the lottery: '
    # Scans all of the list except the last index, and prints out all of the names with a comma after each one
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: #This index is used to prevent the last player from being printed out 
        print(p+', ', end='')
    print(players[len(players)-1]) # This player was printed separately, so that they wouldn't display a comma after(since they are the last person)

    ####
    # This section creates an infinite loop until the user correctly answers the right name
    # If the name is wrong, it'll print out 'Guess again!' and then add to the guesses by 1
    # If they guess the name right, the loop ends and will tell the user how many guesses it took for them to answer
    # The code ends with the function returning the guess count.
    ####
    guesses = 1 
    while input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses

def goguess(low=1, high=20):
    guess_count = 1
    secret = random.randint(low, high)
    print('I have a number between', low, 'and', high, 'inclusive.')
    guess = int(input('Guess: '))
    while guess != secret:
        if(guess < secret):
            reason = 'low'
        else:
            reason = 'high'
        print(guess, 'is too', reason, end='.')
        guess_count += 1
        guess = int(input('Guess: '))
    print('Right! My number is ', secret, '!', ' You guessed in ', guess_count, ' guess(es)!', sep='')