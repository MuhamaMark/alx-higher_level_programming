#!/usr/bin/python3
"A module defining a class MyList"


class MyList(list):
    """class that inherits attributes from list
    Args:
        list: class list
    """

    def print_sorted(self):
        """method that prints a sorted list"""
        print(sorted(self))
