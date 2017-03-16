from abc import abstractmethod

class basePoint(object):

#abstract method
    def get_x(self):
        pass
    def set_x(self, x):
        pass

class Point(basePoint):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = int(x)

    def set_y(self, y):
        self._y = int(y)

    def __str__(self):
        return"point with x={}, y={}".format(self._x, self._y)

class ColorPoint(Point):
    def __init__(self, x, y, color):
        self.color = color
        super(ColorPoint, self).__init__(x, y)
# obra6tenie kum parent class

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
