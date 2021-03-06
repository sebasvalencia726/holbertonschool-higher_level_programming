#!/usr/bin/python3
"""Class Rectangle
"""


from .base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        x (int): x position of the rectangle.
        y (int): y position of the rectangle.
        id (int): id of the rectangle.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int): x position of the rectangle.
            y (int): y position of the rectangle.
            id (int): id of the rectangle.

        """
        super().__init__(id)
        self.__width = width
        if type(self.__width) != int:
            raise TypeError('width must be an integer')
        if self.__width <= 0:
            raise ValueError('width must be > 0')
        self.__height = height
        if type(self.__height) != int:
            raise TypeError('height must be an integer')
        if self.__height <= 0:
            raise ValueError('height must be > 0')
        self.__x = x
        if type(self.__x) != int:
            raise TypeError('x must be an integer')
        if self.__x < 0:
            raise ValueError('x must be >= 0')
        self.__y = y
        if type(self.__y) != int:
            raise TypeError('y must be an integer')
        if self.__y < 0:
            raise ValueError('y must be >= 0')

    @property
    def width(self):
        """Getter method width of the rectangle.

        Returns:
            width the square.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width method.

        Args:
            value (int): new width of the square.

        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method of height of the rectangle.

        Returns:
            Height the square.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height method.

        Args:
            value (int): new height of the square.

        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """Getter method x argument of the rectangle.

        Returns:
            x position of the rectangle.

        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x position method.

        Args:
            value (int): new x position of the rectangle.

        """
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Getter method of y argument of the rectangle.

        Returns:
            y position of the rectangle.

        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y position method.

        Args:
            value (int): new y position of the rectangle.

        """
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """Method to ger the rectangle area.

        Returns:
            Area of the rectangle.

        """
        return self.__width * self.__height

    def display(self):
        """display method for the rectangle.

        Args:
            None

        """
        stri = ""
        for j in range(self.__height + self.__y):
            if j < self.__y:
                stri += '\n'
            else:
                for i in range(self.__width + self.__x):
                    if i < self.__x:
                        stri += ' '
                    else:
                        stri += "#"
                stri += '\n'
        print(stri.rstrip())
        return(stri)

    def __str__(self):
        """repr method.

        Args:
            None

        """
        representation = "[Rectangle] (%d) %d/%d - %d/%d" % (self.id,
                                                             self.__x,
                                                             self.__y,
                                                             self.__width,
                                                             self.__height)
        return(representation)

    def update(self, *args, **kwargs):
        """public method  that assigns an argument to each attribute:
           **kwargs must be skipped if *args exists and is not empty

            Args:
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            kwargs:
                width (int): width of the rectangle.
                height (int): height of the rectangle.
                x (int): x position of the rectangle.
                y (int): y position of the rectangle.
                id (int): id of the rectangle.

        """
        if len(args) == 0:
            if kwargs.get("id") is not None:
                self.id = kwargs['id']
            if kwargs.get("width") is not None:
                self.__width = kwargs['width']
            if kwargs.get("height") is not None:
                self.__height = kwargs['height']
            if kwargs.get("x") is not None:
                self.__x = kwargs['x']
            if kwargs.get("y") is not None:
                self.__y = kwargs['y']
        else:
            self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]

    def to_dictionary(self):
        """Public method that returns the dictionary
        representation of a Rectangle

        """
        emptyDict = {}
        dictionary = self.__dict__
        emptyDict['id'] = dictionary['id']
        emptyDict['width'] = dictionary['_Rectangle__width']
        emptyDict['height'] = dictionary['_Rectangle__height']
        emptyDict['x'] = dictionary['_Rectangle__x']
        emptyDict['y'] = dictionary['_Rectangle__y']
        return emptyDict
