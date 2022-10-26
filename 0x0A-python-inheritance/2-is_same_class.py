#!/usr/bin/python3
"""
A module to check whether an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    method to check if object is an exact instance of a class
    Args:
        obj: class attributes
        a_class: class to check against
    """

    if (type(obj) == a_class):
        return True
    else:
        return False
