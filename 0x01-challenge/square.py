#!/usr/bin/python3
"""square module"""


class Square():
    """square class"""
    def __init__(self, width=0, height=0):
        """Initialize the class"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        """perimeter of the square"""
        return 4 * self.width

    def __str__(self):
        """string representation"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
