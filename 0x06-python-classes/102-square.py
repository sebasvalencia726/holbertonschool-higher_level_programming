#!/usr/bin/python3
"""Class Square
"""


class Square:
    """empty class Square that defines a square.

    Attributes:
        Not Attributes for now.

    """
    def __init__(self, size=0):
        """Example of docstring on the __init__ method.

        Args:
            size (int): size of square.

        """
        self.__size = size
        if isinstance(self.__size, (int, float)) is False:
            raise TypeError('size must be a number')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Class methods are similar to regular functions.

        Returns:
            Area of the square.

        """
        return self.__size * self.__size

    @property
    def size(self):
        """Class methods are similar to regular functions.

        Returns:
            Size the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter size method.

        Args:
            value (int): new size of the square.

        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        else:
            self.__size = value

    def __lt__(self, other):
        """Setter size method.

        Args:
            other (int): new size of the square.

        """
        return self.__size < other.__size

    def __gt__(self, other):
        """Setter size method.

        Args:
            other (int): new size of the square.

        """
        return self.__size > other.__size

    def __le__(self, other):
        """Setter size method.

        Args:
            other (int): new size of the square.

        """
        return self.__size <= other.__size

    def __eq__(self, other):
        """Setter size method.

        Args:
            other (int): new size of the square.

        """
        return self.__size == other.__size

    def __ne__(self, other):
        """Setter size method.

        Args:
            other (int): new size of the square.

        """
        return self.__size != other.__size

    def __ge__(self, other):
        """Setter size method.

        Args:
            other (int): new size of the square.

        """
        return self.__size >= other.__size
