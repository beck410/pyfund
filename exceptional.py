'''A module for demonstratig exceptions.'''

def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError):
        return -1
