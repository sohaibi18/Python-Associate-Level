import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_point(self, point):
        return math.sqrt((self.__x - point.getx()) ** 2 + (self.__y - point.gety()) ** 2)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        # Store the points in a private list
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        # Calculate the lengths of the sides
        side1 = self.__vertices[0].distance_from_point(self.__vertices[1])
        side2 = self.__vertices[1].distance_from_point(self.__vertices[2])
        side3 = self.__vertices[2].distance_from_point(self.__vertices[0])
        # Return the sum of the sides
        return side1 + side2 + side3


# Example usage
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())  # Output: 3.414213562373095
