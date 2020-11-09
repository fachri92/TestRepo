


def a():
    print('hello')
def z():
    return [1,[1,2,{'test': a}]]
def x():
    return z
def beta():
    return {'hello' : [1, 2, x]}
beta()['hello'][2]()()[1][2]['test']()

