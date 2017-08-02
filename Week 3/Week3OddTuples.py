def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    bTup = aTup[::2]

    return bTup

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
