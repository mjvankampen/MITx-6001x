def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    dout = {}
    for key in d:
        if d[key] not in dout:
            dout[d[key]] = [key]
        else:
            dout[d[key]].append(key)
            dout[d[key]].sort()
    return dout

d = {1:10, 2:20, 3:30}
print(dict_invert(d))

d = {1:10, 2:20, 3:30, 4:30}
print(dict_invert(d))

d = {4:True, 2:True, 0:True}
print(dict_invert(d))