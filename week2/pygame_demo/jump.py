#!/usr/bin/env python3
"""
A game that makes a jumping mushroom
"""
import pygame
from game_globals import *  # defined list of game variables

BORDER = 20
class Player():
    """
    defines the player object
    """

    def __init__(self, body_pos, body_size):

        self.x_body, self.y_body = body_pos
        self.w_body, self.h_body = body_size
        self.jump_state, self.max_jump = 0, 230
        self.arc_width = 20
        self.speed = 50
        self.color = RED
        self.status = "jumped"
        self.face = 'right'
    def draw(self, screen, level):
        """
        draw the player on the screen
        """
        self.legs = pygame.draw.rect(
            screen, RED,
            (self.x_body, self.y_body, self.w_body, self.h_body)
        )
        if not level.colliderect(self.legs):
            exit('you loose!')

    def jump(self, floors):
        """
        initiate a jumping movement by updating vertical position
        """
        if any(\
                 self.legs.top == floor.rect.top + floor.rect.height\
            and self.legs.left >= floor.rect.left\
            for floor in floors\
        ):
            print('shh')
            self.status = 'jumped'
        else:
            print('bla')
            player_dy = self.speed / FPS
            self.y_body -= player_dy


    def back_to_floor(self, floors):
        if any(self.legs.colliderect(floor.rect) for floor in floors):
            self.status = 'stationary'
        else:
            player_dy = self.speed / FPS
            self.y_body += player_dy



    def move(self, boundaries, floors):
        """
        initiate player movement by updating current possition
        """
        player_dx = self.speed / FPS
        if not any(\
            self.legs.colliderect(floor.rect)\
            for floor in floors\
        ) and not 'jump' in self.status:
            self.status = 'stationary'
        elif self.status == 'move' or 'jump' in self.status:
            if self.face == 'right':
                if boundaries[0].rect.colliderect(self.legs):
                    print('collision')
                else:
                    self.x_body += player_dx

            elif self.face == 'left':
                if any(self.legs.colliderect(boundary) for boundary in boundaries):
                    print('collision')
                else:
                    self.x_body -= player_dx




class Platform:
    def __init__(self, pos, size, color=BLACK):
        self.pos_x, self.pos_y = pos
        self.size_width, self.size_height = size
        self.color = color
        self.status = 'stationary'
        self.face = 'none'


    def draw(self, screen):
        self.rect = pygame.draw.rect(
            screen, self.color,
            (self.pos_x, self.pos_y, self.size_width, self.size_height)
        )


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Generate a flag!")
        self.clock = pygame.time.Clock()
        self.my_font = pygame.font.SysFont(FONT_NAME, FONT_PX)
        self.running = True
        self.player = Player(
            (148, 548), (10, 50))
        self.platforms = [
            Platform(
                (0, 608), (900, 100)
            ),
            Platform(
                (700, 458), (400, 70)
            )
        ]
        self.boundaries = [
            Platform(
                (700, 450), (15, 60), RED
            ),
            Platform(
                (0, 0), (20, HEIGHT)
            )
            ]
        self.boundary = BORDER
        self._event_loop()

    def _event_loop(self):
        """
        pygame event loop
        """
        while self.running:
            self._handle_events()
            self._update_display()

    def _handle_events(self):
        """
        definition of all events in the event loop
        """
        for event in pygame.event.get():
            print(self.player.status)
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.status == 'stationary' or self.player.status == 'move':
                        self.player.status = 'jumping'
                        print(self.player.y_body)
                        self.player.jump_state = 0
                        print(self.player.jump_state)
                if event.key == pygame.K_RIGHT or \
                event.key == pygame.K_LEFT:
                    if self.player.status == 'stationary':
                        self.player.status = 'move'
                    self.player.face = (
                        'right'
                        if event.key == pygame.K_RIGHT
                        else 'left'
                    )
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or\
                        event.key == pygame.K_LEFT:
                    if not 'jump' in self.player.status:
                        self.player.status = 'stationary'

    def _update_display(self):
        """
        handles screen display updates
        """
        self.screen.fill(WHITE)
        self._draw_elements()
        pygame.display.flip()

    def _draw_elements(self):
        """
        draw all elements to the screen
        """
        level = pygame.draw.rect(self.screen, WHITE, (0, 0, WIDTH, HEIGHT), 1)
        self.player.draw(self.screen, level)
        for platform in self.platforms:
            platform.draw(self.screen)
        for boundary in self.boundaries:
            boundary.draw(self.screen)
        if self.player.status == 'jumping':
            if self.player.jump_state <= self.player.max_jump:
                self.player.jump(self.platforms)
                self.player.jump_state += 1
            else:
                self.player.status = 'jumped'
            self.player.move(self.boundaries, self.platforms)
        elif self.player.status == 'jumped':
            self.player.jump_state -= 1
            self.player.back_to_floor(self.platforms)
            self.player.move(self.boundaries, self.platforms)
        elif self.player.status == 'move':
            self.player.move(self.boundaries, self.platforms)
        self.player.draw(self.screen, level)


def main():
    """
    entrypoint
    """
    Game()


if __name__ == '__main__':
    main()
