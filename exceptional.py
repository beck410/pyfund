'''A module for demonstratig exceptions.'''

def convert(s):
    '''Convert to an integer.'''
    try:
        x = int(s)
    except (ValueError, TypeError):
        x = -1
    return x
