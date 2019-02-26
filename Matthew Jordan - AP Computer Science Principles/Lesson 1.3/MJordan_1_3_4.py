#Testing
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = False
        print('orange bug in food id()')
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = False
        print('banana bug in food_id()') 
    # Add tests so that all lines of code are visited during test
 
    if works:
        print('food_id passed all tests')
        return works

def f(x):
    #isinstance is better than int(x) == x, because an error is thrown when converting x to an int.
    if(isinstance(x, int)):
        if(x % 2 == 0):
            if(x % 3 == 0):
                print('Number', x, 'is a multiple of 6.')
            else:
                print('Number', x, 'is even.')
        else:
            print('Number', x, 'is odd.')
    else:
        print('The input given is not an integer.')
            