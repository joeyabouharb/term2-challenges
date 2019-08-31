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
        self.is_triggered = False
        self.is_beast = False
        self.running = True
        self.pos = []
        self.is_draw = False
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
                if not self.is_triggered:
                    self.pos.append(pygame.mouse.get_pos())
                self.is_triggered = not self.is_triggered
            elif event.type == pygame.MOUSEMOTION:
                if self.is_triggered:
                    self.pos.append(pygame.mouse.get_pos())
                    self.is_draw = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    print('hello')
                    self.is_beast = not self.is_beast
    def _update_display(self):
        self.screen.fill(WHITE)
        if self.is_beast:
            for position in self.pos:
                self.screen.fill(WHITE)
                self._draw_elements(position)
                pygame.display.flip()

        else:
            self._draw_elements()
            pygame.display.flip()


    def _draw_elements(self, position=False):
        if self.is_draw:
            pygame.draw.aalines(self.screen, BLACK, False, self.pos, 5)
        if position:
            pygame.draw.circle(self.screen, OFF_COLOR_0, position, 12)

        text_snippet = self.my_font.render("Hello, Me!", True, BLACK)
        self.screen.blit(text_snippet, (50, 112))


def main():

    game = Game()


if __name__ == '__main__':
    main()
