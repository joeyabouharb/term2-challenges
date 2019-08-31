#!/usr/bin/env python3

import pygame
from game_globals import *
from math import cos, sin, pi
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
        pi2 = 2 * pi
        radius = 50
        x, y = (200, 200)
        color = (0, 0, 255)
        item = pygame.draw.polygon(self.screen, color, [
            (x + radius * cos(2 * pi * i / n), y + radius * sin(2 * pi * i / n))
            for i in range(n)
        ])


def main():

    game = Game()


if __name__ == '__main__':
    main()
