#!/usr/bin/env python3

###########################
#                         #
#     PyGame Template     #
#                         #
###########################


import pygame
import sys


#### Set everything up ####

# application config
WIDTH = 1024
HEIGHT = 768
FPS = 25 # frames per second limit

# basic useful constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BEIGE = (255, 240, 180)
RED = (255, 0, 20)
PLUM = (10, 0, 0)

LIMEGREEN = (200, 250, 100)
DARKGREEN = (20, 40, 20)


# initialise pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Baby’s first PyGame")
clock = pygame.time.Clock()


font_name = 'serif' # or None for the default font
font_name = 'sans' # or None for the default font
font_name = 'Helvetica' # or None for the default font
font_px = 32
my_font = pygame.font.SysFont(font_name, font_px)


# Stuff specific to our program
class Mushroom:
    def __init__(self):

        self.x = 300
        self.y = 600
        self.vy = 0

        self.squash = False

    def draw(self): # method
        """draw me"""

        # draw border (background)
        pygame.draw.rect(screen, BEIGE, (self.x - 40, self.y - 75, 80, 75))
        if self.squash:
            pygame.draw.polygon(screen, RED, [
                (self.x - 90, self.y - 65),
                (self.x + 90, self.y - 65),
                (self.x + 10, self.y - 140),
                (self.x - 10, self.y - 140),
            ])
        else:
            pygame.draw.polygon(screen, RED, [
                (self.x - 90, self.y - 75),
                (self.x + 90, self.y - 75),
                (self.x + 10, self.y - 150),
                (self.x - 10, self.y - 150),
            ])

    def move(self):

        self.y = self.y + self.vy / FPS
        self.vy += 4000 / FPS

        if self.y > 600:
            self.y = 600
            self.vy = 0


    def key(self, event):
        """takes mouse click event and determines whether the click
           is within the button and sets button state appropriately"""
        if event.type == pygame.KEYDOWN:
            self.squash = True
        elif event.type == pygame.KEYUP:
            self.squash = False
            if self.vy == 0:
                self.vy = -1500 # pixels/sec






player = Mushroom()


#### Game loop ####

running = True
while running:

    clock.tick(FPS)

    #### Game loop part 1: Event handling #####

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            print(event)
            player.key(event)


        # add any other events here (keys, mouse, etc.)

        #elif event.type == ????:
        #   handle this type of event


    #### Game loop part 2: Updates #####

    # Run animations, etc.

    player.move()



    #### Game loop part 3: Draw #####
    screen.fill(WHITE)

    player.draw()







    # e.g. draw some text
    text_snippet = my_font.render("Hello PyGame", True, WHITE)
    screen.blit(text_snippet, (460, 330))

    
    # after drawing, make the drawing visible
    pygame.display.flip()



#### Clean up and close program ####

# close the window
pygame.quit()
