#!/usr/bin/python3
"""This module defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize rectangle instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer".format(value))
        if value <= 0:
            raise ValueError("width must be > 0".format(value))
        else:
            self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer".format(value))
        if value <= 0:
            raise ValueError("height must be > 0".format(value))
        else:
            self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer".format(value))
        if value < 0:
            raise ValueError("x must be >= 0".format(value))
        else:
            self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer".format(value))
        if value < 0:
            raise ValueError("y must be >= 0".format(value))
        else:
            self.__y = value

    def area(self):
        """Return the area of a rectangle object"""
        return (self.__width * self.__height)

    def display(self):
        """display a rectangle using '#' character"""
        rect = self.y * "\n"
        for i in range(self.height):
            rect += (" " * self.x)
            rect += ('#' * self.width) + "\n"

        print(rect, end='')

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """update method
        Args:
            *args: New attribute values
            - 1st argument represents id attribute
            - 2nd argument represents width attribute
            - 3rd argument represent height attribute
            - 4th argument represents x attribute
            - 5th argument represents y attribute
            **kwargs: assigns a key/value argument to attributes
        """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returs a dictionary with properties """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
