#!/usr/bin/env python3

import pygame
from game_globals import *
from math import cos, sin, pi
RADIUS = 50
class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Generate a flag!")
        self.clock = pygame.time.Clock()
        self.my_font = pygame.font.SysFont(FONT_NAME, FONT_PX)
        self.running = True
        self._event_loop()


    def _event_loop(self):
        """
        """
        while self.running:
            self._handle_events()
            self._update_display()


    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

    def _update_display(self):
        self.screen.fill(WHITE)
        self._draw_elements()
        pygame.display.flip()


    def _draw_elements(self, n = 6):
        pygame.draw.polygon(
            self.screen, 
            OFF_COLOR_1,
            [
                (
                    cos(i / n * 2 * pi + pi / 2) * RADIUS + 120,
                    sin(i / n * 2 * pi + pi / 2) * RADIUS + 100
                )
                for i in range(0,n)
            ]
        )
def main():

    game = Game()


if __name__ == '__main__':
    main()
