#!/usr/bin/env python3

import pygame

class Game():
    WIDTH = 1024
    HEIGHT = 768
    FPS = 5 # frames per second limit
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                self.screen.fill(self.BLACK)
                x = 96
                y = 128
                for i, point_x in enumerate(range(0, self.HEIGHT + y * 2, y)):
                    is_black = bool(
                        i % 2 != 0
                    )
                    for point_y in range(0, self.WIDTH, x):
                        is_black = not is_black
                        color = (
                            'BLACK'
                            if is_black
                            else 'WHITE'
                        )
                        pygame.draw.rect(self.screen, getattr(self, color), (point_x, point_y, y, x))
                pygame.display.flip()


def main():

    game = Game()



if __name__ == '__main__':
    main()
