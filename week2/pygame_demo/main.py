#!/usr/bin/env python3

###########################
#                         #
#     PyGame Template     #
#                         #
###########################


import pygame


#### Set everything up ####

# application config
WIDTH = 1024
HEIGHT = 768
FPS = 5 # frames per second limit

# basic useful constants
BLACK = (0, 0, 0)
WHITE = (125, 255, 33)


# initialise pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Baby’s first PyGame")
clock = pygame.time.Clock()


font_name = 'serif' # or None for the default font
font_px = 32
my_font = pygame.font.SysFont(font_name, font_px)


#### Game loop ####

running = True
while running:

    clock.tick(FPS)

    #### Game loop part 1: Event handling #####

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            break

        # add any other events here (keys, mouse, etc.)

        #elif event.type == ????:
        #   handle this type of event




    #### Game loop part 2: Updates #####

    # Run animations, etc.



    #### Game loop part 3: Draw #####
    screen.fill(WHITE)

    # e.g. draw a rectangle
    pygame.draw.rect(screen, (0, 0, 100), (0, 100, 300, 100))

    pygame.draw.rect(screen, (100, 100, 100), (410, 0, 300, 800))

    start_point = 100
    end_point = 600
    step = 150
    for point in range(start_point, end_point, step):
        pygame.draw.rect(screen, (0, 0, 0), (530, point, 50, 100))

    # draw car
    pygame.draw.circle(screen, (20, 20, 20), (610, 300), 30, 15)
    pygame.draw.circle(screen, (20, 20, 20), (690, 300), 30, 15)
    pygame.draw.circle(screen, (20, 20, 20), (690, 440), 30, 15)
    pygame.draw.circle(screen, (20, 20, 20), (610, 440), 30, 15)
    pygame.draw.ellipse(screen, (100, 65, 200), (600, 280, 110, 200),  40)

    # draw person
    pygame.draw.circle(screen, (255, 255, 255), (810, 440), 30)
    pygame.draw.rect(screen, (255, 255, 255), (800, 465, 20, 100))
    pygame.draw.polygon(screen, (255, 255, 255), [(750, 470), (810, 490), (805, 520)])
    pygame.draw.polygon(screen, (255, 255, 255), [(870, 470), (815, 490), (815, 520)])
    pygame.draw.polygon(screen, (255, 255, 255), [(750, 580), (810, 540), (805, 565)])
    pygame.draw.polygon(screen, (255, 255, 255), [(870, 580), (815, 540), (815, 565)])
    # e.g. draw some text
    text_snippet = my_font.render("Drive Safe!", True, WHITE)
    screen.blit(text_snippet, (50, 130))

    # after drawing, make the drawing visible
    pygame.display.flip()



#### Clean up and close program ####

# close the window
pygame.quit()

