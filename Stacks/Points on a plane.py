import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        # Private properties for coordinates
        self.__x = x
        self.__y = y

    def getx(self):
        # Return the x coordinate
        return self.__x

    def gety(self):
        # Return the y coordinate
        return self.__y

    def distance_from_xy(self, x, y):
        # Calculate the distance between the current point and the given (x, y) point
        return math.sqrt((self.__x - x) ** 2 + (self.__y - y) ** 2)

    def distance_from_point(self, point):
        # Calculate the distance between the current point and another Point object
        return math.sqrt((self.__x - point.getx()) ** 2 + (self.__y - point.gety()) ** 2)


# Testing the implementation
point1 = Point(0, 0)
point2 = Point(1, 1)

# Distance between point1 and point2
print(point1.distance_from_point(point2))  # Output: ~1.414

# Distance between point2 and coordinates (2, 0)
print(point2.distance_from_xy(2, 0))  # Output: ~1.414
