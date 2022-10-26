#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Derived class Rectangle from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle
        Args:
            width(int): width of the new rectangle
            height(int): height of the new rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method that returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Special method that returns the printable string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
