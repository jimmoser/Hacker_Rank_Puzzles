import math
import matplotlib.pyplot as plt


class Circle:
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color
        self.area = math.pi * radius ** 2
        self.circum = 2 * math.pi * radius

    def add_radius(self):
        self.radius += int(input("How much would you like to add to the radius? "))
        return print("The radius of {} is now {}".format(self, self.radius))

    def draw_circle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()


jim_circle = Circle(10, 'blue')
jim_circle.radius = 2
Circle.draw_circle(jim_circle)