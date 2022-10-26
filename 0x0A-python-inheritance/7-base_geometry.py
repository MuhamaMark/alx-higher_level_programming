#!/usr/bin/python3
"""
Base class
"""


class BaseGeometry:
    """
    Represents base geometry
    """

    def area(self):
        """
        method not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates the parameter as an integer.
        Args:
            name(str): name of the parameter
            value(int): parameter to validate.
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0.
        """

        def __init__(self, name, value):
            self.name = name
            self.value = value
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
