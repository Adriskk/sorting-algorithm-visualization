# -*- coding: utf-8 -*-

"""
Description: Column class file
License:

"""

import pygame
import data
import random

__author__ = "Adriskk"
__copyright__ = "Copyright 2020, Sorting Algorithms Visualization project"
__credits__ = ["Adriskk"]
__license__ = ""
__version__ = "1.0.0"
__email__ = "adrian_iskra@o2.pl"


class Column(object):
    def __init__(self, last_x: int, screen: object, sizes):
        self.x = last_x + data.c_WIDTH
        self.y = data.c_Y
        self.color = data.WHITE

        # => GENERATE Y-SIZES
        self.sizes = sizes

        if len(self.sizes) > 0:
            size = random.choice(self.sizes)

            self.size_Y = size

            # => POP THE VALUE WHEN ALREADY USED
            self.sizes.pop(self.sizes.index(size))

        else:
            self.size_Y = self.sizes[0]

        self.last_x = last_x

        self.screen = screen

    def draw(self):
        # DRAW GIVEN COLUMN
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, data.c_WIDTH, -self.size_Y))

    def return_last(self):
        return self.x

    def return_sizes(self):
        return self.sizes
