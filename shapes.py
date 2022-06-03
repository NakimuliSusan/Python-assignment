from cmath import pi
import math
class Circle:
    pi = math.pi
    def __init__(self, radius):
        self.radius = radius

    def area (self):
      Area = pi * (self.radius**2)
      return Area

    def circumference (self):
        c = 2 * pi * (self.radius)
        return c


class Square:
    def __init__ (self,side_a):
        self.side_a = side_a

    def area (self):
        A = (self.side_a **2)
        return A

    def perimeter (self):
        P = (4*self.side_a)
        return P


class Rectangle:
    def __init__ (self,length,width):
        self.length = length
        self.width = width
    
    def area (self):
        A = (self.length*self.width)
        return A


    def perimeter (self):
        P = 2*(self.length + self.width)
        return P


class Sphere:
    def __init__ (self, radius):
        self.radius = radius

    def area (self):
        A = (4*pi*(self.radius**2))
        return A

    def volume (self):
        V = (4/3*(pi*(self.radius**3)))
        return V
