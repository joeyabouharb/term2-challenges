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


    def _draw_elements(self, n = 3):
        a, b = (160, 100), (260, 100)
        top = a[0] + (b[0] - a[0])/2
        c = (top, 50)
        d = (top, c[1] + a[1]/2 + 60 + c[1])
        # pygame.draw.line(self.screen, RED, a, b)
        pygame.draw.polygon(self.screen, RED, (a, b, c))
        pygame.draw.rect(self.screen, RED, (*a, b[0] - a[0], 60))
        pygame.draw.polygon(self.screen, RED, ((a[0], a[1] + 60), (b[0], b[1] + 60), d))
def main():

    game = Game()


if __name__ == '__main__':
    main()
