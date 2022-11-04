import math


class Color:
    def col(color):
        return color

class Rectangle:
    def __init__(self, width, height, color):
        self.width=width
        self.height=height
        self.color=Color.col(color)

    def square(self):
        return self.width*self.height

    def __repr__(self):
        return f'Длина - {self.width}, ширина - {self.height}, цвет - {self.color}, площадь - {Rectangle.square(self)}'

class Circle:
    def __init__(self,radius,color):
        self.radius=radius
        self.color=Color.col(color)

    def square(self):
        return math.pi*self.radius**2
    def __repr__(self):
        return f'Радиус - {self.radius}, цвет - {self.color}, площадь - {Circle.square(self)}'

class Square(Rectangle):
    def __init__(self,side,color):
        self.width=side
        self.height=side
        self.color=Color.col(color)
    def square():
        return side**2

    

