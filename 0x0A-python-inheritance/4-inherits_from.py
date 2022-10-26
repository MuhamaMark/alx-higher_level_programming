#!/usr/bin/python3
"""
Module: inherit_from checks for object inheritance
"""


def inherits_from(obj, a_class):
    """
    method that checks for inheritance of object from class
    Args:
        obj: object to be checked
        a_class: class to be checked against
    Returns:
        True: if object is an instance of a class that inherited
        False: if otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
