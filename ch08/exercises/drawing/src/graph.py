import pygame
from src import point


class Graph:

    def __init__(self, width=200, height=200):
        self.width = width
        self.height = height
        self.points = []

        self.x_axis = pygame.Surface((width, 1))
        self.x_axis_rect = self.x_axis.get_rect()
        self.x_axis_rect.y = height/2
        self.x_axis.fill((0,0,0))

        self.y_axis = pygame.Surface((1, height))
        self.y_axis_rect = self.x_axis.get_rect()
        self.y_axis_rect.x = width/2
        self.y_axis.fill((0,0,0))

    def clear(self):
        self.points = []

    def complement(self):
        for p in self.points:
            p.set_to_comp_color()

    def add_point(self, x=0, y=0, color=None):
        p = point.Point(x, y, color)
        self.points.append(p)
        return p