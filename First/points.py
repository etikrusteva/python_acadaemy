
class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = int(x)

    def get_y(self):
        return self.y
    def set_y(self, y):
        self.y = int(y)

    def get_color(self):
        return self.color
    def set_color(selfself, color):
        self.color = color

from random import randint

values_y = []
for item in values_y:
    item.set_y(randint(-100, 100))
    vy = item.get_y()
    print(vy)

values_x =[]
for item in values_x:
    item.set_x(randint(-100, 100))
    vx = item.get_y()
    print(vx)

list_color = ["red", "green", "blue"]
rand_color = randint(0, len(list_color)-1)



