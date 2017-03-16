
class Line(object):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def set_a(self, a):
        self._a = int(a)

    def get_b(self):
        return self._b

    def set_b(self, b):
        self._b = int(b)

    def x_diff(self):
        return self._b.get_x() - self._a.get_x()

    def y_diff(self):
        return self._b.get_y() - self._a.get_x()

