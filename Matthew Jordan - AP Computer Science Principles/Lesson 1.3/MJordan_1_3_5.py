def how_eligible(essay):
    points = 0
    chars = ['?', '"', ',', '!']
    for char in chars:
        if(char in essay):
            points += 1
    return points