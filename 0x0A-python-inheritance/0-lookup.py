#!/usr/bin/python3
"""
Module for the lookup method
"""


def lookup(obj):
    """lookup returns a list of available attributes
    Args:
        obj: instance of a class
    Returns:
        List of attributes
    """

    return (dir(obj))
