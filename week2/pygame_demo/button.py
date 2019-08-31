#!/usr/bin/env python3

import pygame
from globals import *

class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Generate a flag!")
        self.clock = pygame.time.Clock()
        self.my_font = pygame.font.SysFont(FONT_NAME, FONT_PX)
        self.is_on = False
        self.running = True
        self.buttons = BUTTONS
        self.elements = BORDERS
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for index, items in enumerate(self.buttons):
                    _, off_rect = items
                    if off_rect[-1] + off_rect[0] >= x >= off_rect[0] and\
                    off_rect[-2] + off_rect[1] >= y >=off_rect[1]:
                        self.change_elements(ELEMENTS.get(f'NEW_ELEMENT_{index}'))

    def change_elements(self, element):
        if self.elements.count(element):
            self.elements.remove(
                (element)
            )
        else:
            self.elements.append(element)


    def _update_display(self):
        self.screen.fill(WHITE)
        self._draw_elements()
        pygame.display.flip()


    def _draw_elements(self):

        for color, pos in self.buttons:
            pygame.draw.rect(self.screen, color, pos)
        for color, pos, border in self.elements:
            pygame.draw.rect(self.screen, color, pos, border)
        text_snippet = self.my_font.render("Click Me!", True, WHITE)
        self.screen.blit(text_snippet, (50, 112))


def main():

    game = Game()


if __name__ == '__main__':
    main()
