import math
import time

# Self - instance
# __init__ - initializer
# self.date,metal,raduis etc - instance variables


class Ring(object):

    # def __init__(self, date, metal, radius, price, quantity):
    #     self.date = date
    #     self.metal = metal
    #     self.radius = radius
    #     self.price = price
    #     self.quantity = quantity

    # def cost(self):
    #     return self.price * self.quantity

    # def area(self):
    #     return math.pi * self.radius

    # Class variable
    date = time.strftime("%Y-%m-%d", time.gmtime())
    centre = 0.0

    def __init__(self, date=date, metal="Copper", radius=5.0, price=5.0, quantity=5):
        self.date = date
        self.metal = metal
        self.radius = radius
        self.price = price
        self.quantity = quantity

# Below code refers to the Class Methods
    def cost(self):
        return self.price * self.quantity

    def area(self):
        return math.pi * self.radius**2


def main():
    print("Center of the Ring is at: ", Ring.centre)
    r = Ring(price=8)
    print("Radius:{0}, Cost:{1}".format(r.radius, r.cost()))


if __name__ == '__main__':
    main()
