#!/usr/bin/python3
"""Module containing the Rectangle class"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle

        Args:
            value (int): The width value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle

        Args:
            value (int): The height value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
