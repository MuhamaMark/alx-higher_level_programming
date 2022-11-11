#!/usr/bin/python3
"""Module that defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the square.
        Args:
            *args (int): New attribute values.
                -1st argument represents id attribute
                -2nd argument represents size attributes
                -3rd argument represents x attribute
                -4th argumenr represents y attribute
            **kwargs (dict): new key/value pairs of attributes.
        """
        if args is not None and len(args) != 0:
            list_args = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_args[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_args[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
