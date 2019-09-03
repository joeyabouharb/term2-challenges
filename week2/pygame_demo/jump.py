#!/usr/bin/env python3
"""
A game that makes a jumping mushroom
"""
import pygame
from pygame.locals import (
    KEYDOWN, KEYUP,
    K_SPACE, QUIT,
    K_LEFT, K_RIGHT
)
from game_globals import (
    RED, BLACK, WHITE, WIDTH, HEIGHT,
    FONT_NAME, FONT_PX, FPS
)  # defined list of game variables

def check_collision(floors, player):
    results = []
    for floor in floors:
        results.append(
            bool((
                floor.rect.left <= player.left <= floor.rect.right
                and floor.rect.bottom >= player.top >= floor.rect.top
                ))
        )
    return results


class Player():
    """
    defines the player object
    """

    def __init__(self, body_pos, body_size):
        self.pos = body_pos
        self.size = body_size
        self.jump_state, self.max_jump = 0, 230
        self.status = "jumped"
        self.face = 'none'
        self.legs = None
        self.trigger = False


    def draw(self, screen, level):
        """
        draw the player on the screen
        """
        self.legs = pygame.draw.rect(
            screen, RED,
            (self.pos, self.size)
        )
        if not level.colliderect(self.legs):
            exit('you loose!')


    def jump(self, floors, speed=40):
        """
        initiate a jumping movement by updating vertical position
        """
        collisions = check_collision(floors, self.legs)
        if any(collisions):
            self.status = 'jumped'
        else:
            player_dy = speed / FPS
            self.pos[1] -= player_dy


    def back_to_floor(self, floors, speed=40):
        """
        player falling to floor
        """
        if any(self.legs.colliderect(floor.rect) for floor in floors):
            self.status = 'move'
            if not self.trigger:
                self.face = 'none'
        else:
            player_dy = speed / FPS
            self.pos[1] += player_dy



    def move(self, floors, boundaries, speed=50):
        """
        initiate player movement by updating current possition
        """
        player_dx = speed / FPS
        if all(
            not self.legs.colliderect(floor.rect)
            for floor in floors
        ) and self.status == 'move':
            self.status = 'jumped'
        elif self.status == 'move' or 'jump' in self.status:
            if self.face == 'right':
                if any(
                    boundary.rect.colliderect(self.legs)
                    for boundary in boundaries['right']
                ):
                    self.status = 'jumped'
                    self.pos[0] -= player_dx
                else:
                    self.pos[0] += player_dx
            elif self.face == 'left':
                if any(
                    boundary.rect.colliderect(self.legs)
                    for boundary in boundaries['left']
                ):
                    self.status = 'jumped'
                    self.pos[0] += player_dx
                else:
                    self.pos[0] -= player_dx




class Platform:
    """
    game platforms and collision points
    """
    def __init__(self, pos, size, face='none', color=BLACK):
        self.pos = pos
        self.size = size
        self.color = color
        self.status = 'stationary'
        self.face = face
        self.rect = None

    def draw(self, screen):
        """
        draw platform object
        """
        self.rect = pygame.draw.rect(
            screen, self.color,
            (self.pos, self.size)
        )
    def move(self):
        """
        moving platform
        """
        pass



class Game():
    """
    initiate game instance
    """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Generate a flag!")
        self.clock = pygame.time.Clock()
        self.my_font = pygame.font.SysFont(FONT_NAME, FONT_PX)
        self.running = True


    def handle_events(self, player):
        """
        definition of all events in the event loop
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                pygame.quit()
            elif event.type == KEYDOWN:
                player.trigger = True
                if event.key == K_SPACE:
                    if player.status == 'stationary' or player.status == 'move':
                        player.status = 'jumping'
                        player.jump_state = 0
                if event.key == K_RIGHT or \
                event.key == K_LEFT:
                    if player.status == 'stationary':
                        player.status = 'move'
                    player.face = (
                        'right'
                        if event.key == K_RIGHT
                        else 'left'
                    )
            elif event.type == KEYUP:
                if event.key == K_RIGHT or\
                        event.key == K_LEFT:
                    player.trigger = False
                    if not 'jump' in player.status:
                        player.status = 'stationary'
                        player.face = 'none'

    def update_display(self, platforms, boundaries, player):
        """
        handles screen display updates
        """
        self.screen.fill(WHITE)
        level = pygame.draw.rect(self.screen, WHITE, (0, 0, WIDTH, HEIGHT), 1)
        player.draw(self.screen, level)
        for platform in platforms:
            platform.draw(self.screen)
        for item in list(boundaries.values()):
            for boundary in item:
                boundary.draw(self.screen)
        if player.status == 'jumping':
            if player.jump_state <= player.max_jump:
                player.jump(platforms)
                player.jump_state += 1
            else:
                player.status = 'jumped'
            player.move(platforms, boundaries)
        elif player.status == 'jumped':
            player.jump_state -= 1
            player.back_to_floor(platforms)
            player.move(platforms, boundaries)
        elif player.status == 'move':
            player.move(platforms, boundaries)
        player.draw(self.screen, level)
        pygame.display.flip()


def main():
    """
    entrypoint
    """

    game = Game()
    platforms = [
        Platform(
            [0, 608], [900, 100], 'left'
        ),
        Platform(
            [700, 470], [400, 76], 'right'
        ),
        Platform(
            [380, 380], [200, 70], 'none'
        )
        ]
    boundaries = {
        'left': [
            Platform(
                [0, 0], [20, HEIGHT]
            ),
            Platform(
                [580, 380], [10, 70]
            )
        ],
        'right': [
            Platform(
                [699, 470], [10, 76]
            ),
            Platform(
                [370, 380], [10, 70]
            )
        ]
    }
    player = Player(
        [148, 548], [10, 50]
    )

    while game.running:
        game.handle_events(player)
        game.update_display(platforms, boundaries, player)


if __name__ == '__main__':
    main()
