import pygame
import random
from consts import *


def init_grid_cells():
    grid_list = []
    for i in range(1, 4):
        for j in range(1, 4):
            cell = Cell((25 + (i * 75), (25 + (j * 75))), 50, 50, 255)
            grid_list.append(cell)
    return grid_list


class Cell:
    def __init__(self, coords, sizex, sizey, color):
        self.delta = 0
        self.coords = coords
        self.sizex = sizex
        self.sizey = sizey
        self.color = color
        self.cell = pygame.Rect(self.coords[0] - self.delta, self.coords[1] - self.delta, self.sizex + 2 * self.delta, self.sizey + 2 * self.delta)

    def update(self):
        self.cell = pygame.Rect(self.coords[0] - self.delta, self.coords[1] - self.delta, self.sizex + 2 * self.delta, self.sizey + 2 * self.delta)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.cell)


class Grid:
    def __init__(self, cells):
        self.cells = cells

    def check_mouse_pos(self):
        for i in self.cells:
            if i.cell.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                return i

    def draw(self, surface):
        for i in self.cells:
            i.draw(surface)