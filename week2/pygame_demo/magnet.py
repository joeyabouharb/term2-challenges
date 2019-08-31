#!/usr/bin/env python3

import pygame

class Game():
    WIDTH = 1024
    HEIGHT = 768
    FPS = 60 # frames per second limit
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FONT_NAME = 'Noto Sans'
    FONT_PX = 32

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Generate a flag!")
        self.clock = pygame.time.Clock()
        self.my_font = pygame.font.SysFont(self.FONT_NAME, self.FONT_PX)
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
            elif event.type == pygame.MOUSEMOTION:
                self.x, self.y = pygame.mouse.get_pos()
                x_v, y_v = pygame.mouse.get_rel()

                if x_v < 0: # moving left
                    self.x -= x_v * 0.9
                if x_v > 0: # moving right
                    self.x += x_v * 0.9
                if y_v < 0: # moving up
                    self.y -= x_v * 0.9
                if y_v > 0: # moving down
                    self.y += y_v * 0.9

    def _update_display(self):
        self.screen.fill(self.BLACK)
        pygame.draw.circle(self.screen, self.WHITE, (int(self.x), int(self.y)), 25)
        pygame.display.flip()


def main():

    game = Game()



if __name__ == '__main__':
    main()
