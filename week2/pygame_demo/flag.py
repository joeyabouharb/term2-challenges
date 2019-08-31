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
                # Polish
                pygame.draw.rect(self.screen, self.WHITE, (0, 0, 300, 100))
                pygame.draw.rect(self.screen, (255, 0, 0), (0, 100, 300, 100))
                # Japanese
                pygame.draw.rect(self.screen, self.WHITE, (0, 300, 300, 200))
                pygame.draw.circle(self.screen, (255, 0, 0), (150, 400), 40)
                # Australian Aborigine
                pygame.draw.rect(self.screen, self.BLACK, (500, 0, 300, 100))
                pygame.draw.rect(self.screen, (255, 0, 0), (500, 100, 300, 100))
                pygame.draw.circle(self.screen, (255, 255, 0), (650, 100), 40)

                # SWISS
                pygame.draw.rect(self.screen, (255, 0, 0), (500, 300, 300, 200))
                pygame.draw.rect(self.screen, self.WHITE, (630, 350, 35, 100))
                pygame.draw.rect(self.screen, self.WHITE, (600, 380, 100, 35))
                pygame.display.flip()


def main():

    game = Game()



if __name__ == '__main__':
    main()
    