#!/usr/bin/env python3

import pygame
from game_globals import *
from math import cos, sin, pi

class Arrow():
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.speed = 50
        self.length = 40
        self.fatness = 60
        self.color = RED


    def move(self):
        arrow_dy = self.speed / FPS
        self.y = self.y + arrow_dy


    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            (self.x - self.w/2, self.y - self.h, self.w, self.h)
        )
        pygame.draw.polygon(screen, self.color, [
            (self.x, self.y + self.length),
            (self.x - self.fatness / 2, self.y),
            (self.x + self.fatness /2, self.y)
        ])


    def check_boundary(self, event):
        if CIRCLE_POS_Y + CIRCLE_RADIUS > self.y\
        >= CIRCLE_POS_Y - CIRCLE_RADIUS:
            self.color = GREEN
            print('correct?')


class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Generate a flag!")
        self.clock = pygame.time.Clock()
        self.my_font = pygame.font.SysFont(FONT_NAME, FONT_PX)
        self.running = True
        self.arrows = [
            Arrow(128, 28, 25, 55)
        ]
        self._event_loop()

    def _event_loop(self):
        """
        """
        pygame.time.set_timer(pygame.USEREVENT, 700)
        while self.running:
            self._handle_events()
            self._update_display()


    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.USEREVENT:
                self.arrows.append(
                    Arrow(128, 28, 25, 55)
                )
            elif event.type == pygame.KEYDOWN:
                for arrow in self.arrows:
                    arrow.check_boundary(event)

    def _update_display(self):
        self.screen.fill(WHITE)
        self._draw_elements(self.arrows)
        pygame.display.flip()

    def _draw_elements(self, arrows):
        for arrow in arrows:
            arrow.move()
            arrow.draw(self.screen)
        pygame.draw.circle(
            self.screen, BLACK,
            (CIRCLE_POS_X, CIRCLE_POS_Y),
            CIRCLE_RADIUS, CIRCLE_WIDTH
        )

def main():

    game = Game()


if __name__ == '__main__':
    main()
