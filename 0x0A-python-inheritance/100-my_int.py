#!/usr/bin/python3
"""Defines a class Myint that inherits from int"""


class MyInt(int):
    """ Class that inherits from class int"""

    def __eq__(self, other):
        """ Method that override == with != behaviour """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that overrides != with == behaviour """
        return int.__eq__(self, other)
