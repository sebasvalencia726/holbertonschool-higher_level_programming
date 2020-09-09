#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        return tuple_b
    elif tuple_b == ():
        return tuple_a
    elif len(tuple_a) < 2:
        tuple_a = (*tuple_a, 0)
    elif len(tuple_b) < 2:
        tuple_b = (*tuple_b, 0)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
