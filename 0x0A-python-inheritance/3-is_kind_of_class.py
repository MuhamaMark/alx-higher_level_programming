#!/usr/bin/python3
"""
Module: is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Method to check whether an object is an instance of a class
    Args:
        obj: instance of a class
        a_class: class to check against
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
