# -*- coding: utf-8 -*-

"""
Description: Window class file
License:

"""

# => BUILT-IN MODULES
import pygame
from data import *
import time

# => COLUMN INSTANCE FILE
import column as c

# => ALGORITHMS
from algorithms import bubble_sort  # WORKS
from algorithms import selection_sort  # WORKS
from algorithms import insertion_sort  # WORKS
from algorithms import quick_sort  # WORKS
from algorithms import heap_sort  # WORKS

__author__ = "Adriskk"
__copyright__ = "Copyright 2020, Sorting Algorithms Visualization project"
__credits__ = ["Adriskk"]
__license__ = ""
__version__ = "1.0.0"
__email__ = "adrian_iskra@o2.pl"


class Window(object):
    def __init__(self, algorithm: str):
        self.run = True
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(algorithm)

        self.algorithm = algorithm
        self.result = False
        self.update_loop = False
        self.start = None
        self.time = 'Time: 0 sec'

        # => SORTING METHODS SET IN A DICT
        self.sorting_methods = {
            "selection-sort": selection_sort.selection_sort,
            "bubble-sort": bubble_sort.bubble_sort,
            "insertion-sort": insertion_sort.insertion_sort,
            "quick-sort": quick_sort.quick_sort,
            "heap-sort": heap_sort.heap_sort,
        }

        self.clock = pygame.time.Clock()

        # => FONT
        pygame.font.init()

        self.font = pygame.font.SysFont(FONT, FONT_SIZE)

        CURRENT = self.algorithm.upper()

        # => PROGRAM LABELS
        self.labels = [  # KEY TEXT             # POSITION
            [self.font.render(KEY_G, True, WHITE), (50, 25)],
            [self.font.render(KEY_S, True, WHITE), (50, 75)],
            [self.font.render(KEY_E, True, WHITE), (50, 125)],
            [self.font.render(CURRENT, True, WHITE), (550, 25)],
            [self.font.render(self.time, True, WHITE), (1050, 25)]
        ]

        # => GENERATE COLUMNS
        LAST = 150
        self.columns = []
        self.sizes = [x for x in range(10, 410) if x % 2 == 0]
        self.LENGTH = len(self.sizes)

        # CREATE 200 INSTANCES OF COLUMN
        for i in range(c_AMOUNT + 1):
            try:
                column_inst = c.Column(LAST, self.window, self.sizes)
                self.columns.append(column_inst)

            except IndexError:
                break

            # GET NEW X
            LAST = column_inst.return_last()
            self.sizes = column_inst.return_sizes()

    def loop(self):
        # => PROGRAM MAIN LOOP
        while self.run:
            pygame.event.get()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            keys = pygame.key.get_pressed()

            # => IF G PRESSED -> GENERATE NEW
            if keys[pygame.K_g]:
                self.generate()

            # => IF E PRESSED -> EXIT
            if keys[pygame.K_e]:
                self.run = False

            # => IF S PRESSED -> START THE SORTING VISUALIZATION
            if keys[pygame.K_s]:
                self.update_loop = True

            if self.update_loop: self.update()
            else: self.draw()

            self.clock.tick(FPS)

        # QUIT THE LOOP
        pygame.display.quit()

    # RE-DRAW ALL INSTANCES
    def draw(self):
        # => SET THE BACKGROUND COLOR
        self.window.fill(LIGHT_DARK)

        # => DRAW EVERY COLUMN
        for column in self.columns:
            if self.result: column.color = GREEN
            column.draw()

        if self.start is not None:
            self.time = 'Time: {:.2f} sec'.format((time.time() - self.start))
            self.labels[4][0] = self.font.render(self.time, True, WHITE)



        for label in self.labels:
            self.window.blit(label[0], label[1])

        # UPDATE A WINDOW WITH A NEW INSTANCES
        pygame.display.update()

    def update(self):
        # => CALL CORRECT SORTING FUNCTION
        if self.result is False:

            # => GET THE TIMESTAMP
            if self.start is None: self.start = time.time()

            MAX = (len(self.columns) - 1)

            # => FOR DIFFERENT TYPE OF SORT GIVE DIFFER ENT FUNCTION AND PARAMS

            # => FUNCTIONS THAT NEED START AND MAX PARAMS ADDITIONAL
            if self.sorting_methods[self.algorithm] == quick_sort.quick_sort:
                self.result = self.sorting_methods[self.algorithm](self.columns, 0, MAX, self.swap)

            else:
                self.result = self.sorting_methods[self.algorithm](self.columns, self.swap)

        else:
            # => STOP THE TIMER
            self.start = None
            self.draw()

    def swap(self, element: object, other: object):
        # => CHANGE CURRENT TO RED
        element.color = RED

        # => CHANGE POSITION
        element.x, other.x = other.x, element.x
        element.y, other.y = other.y, element.y

        self.draw()

        # => RE-CHANGE
        element.color = WHITE

    def generate(self):
        # => CALL A __init__ FUNCTION AGAIN TO CREATE A NEW DATA
        Window.__init__(self, self.algorithm)

