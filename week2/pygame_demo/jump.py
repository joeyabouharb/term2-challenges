#!/usr/bin/env python3
"""
A game that makes a jumping mushroom
"""
import pygame
from math import pi
from game_globals import * # defined list of game variables


class Player():
    """
    defines the player object
    """
    def __init__(self, head_pos, head_size, body_pos, body_size):
        self.x_head, self.y_head = head_pos
        self.w_head, self.h_head = head_size
        self.x_body, self.y_body = body_pos
        self.w_body, self.h_body = body_size
        self.jump_state, self.max_jump = 0, 180
        self.arc_width = 42
        self.speed = 70
        self.color = RED
        self.status = "stationary"

    def draw(self, screen):
        """
        draw the player on the screen
        """
        pygame.draw.arc(screen, RED, (
            self.x_head, self.y_head, self.w_head, self.h_head),
            0, pi, self.arc_width
        )
        pygame.draw.rect(
            screen, RED,
            (self.x_body, self.y_body, self.w_body, self.h_body)
        )


    def jump(self):
        """
        initiate a jumping movement by updating vertical position
        """
        player_dy = self.speed / FPS
        self.y_body = self.y_body - player_dy
        self.y_head = self.y_head - player_dy


    def back_to_floor(self):
        player_dy = self.speed / FPS
        self.y_body = self.y_body + player_dy
        self.y_head = self.y_head + player_dy


    def move(self):
        """
        initiate player movement by updating current possition
        """
        player_dx = self.speed / FPS
        if self.status == 'move right':
            self.x_body = self.x_body + player_dx
            self.x_head = self.x_head + player_dx
        else:
            self.x_body = self.x_body - player_dx
            self.x_head = self.x_head - player_dx




class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Generate a flag!")
        self.clock = pygame.time.Clock()
        self.my_font = pygame.font.SysFont(FONT_NAME, FONT_PX)
        self.running = True
        self.player = Player(
            (128, 528), (125, 155), (170, 558), (40, 100))
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
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.status == 'stationary':
                        self.player.status = 'jumping'
                elif event.key == pygame.K_RIGHT or \
                    event.key == pygame.K_LEFT:
                    if self.player.status == 'stationary':
                        self.player.status = (
                            'move right'
                            if event.key == pygame.K_RIGHT
                            else 'move left'
                        )
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or\
                    event.key == pygame.K_LEFT:
                    self.player.status = 'stationary'


    def _update_display(self):
        """
        handles screen display updates
        """
        self.screen.fill(WHITE)
        self._draw_elements(self.player)
        pygame.display.flip()


    def _draw_elements(self, *elements):
        """
        draw all elements to the screen
        """
        for element in elements:
            if element.status == 'jumping':
                if element.jump_state <= element.max_jump:
                    element.jump()
                    element.jump_state += 1
                else:
                    element.status = 'jumped'
            elif element.status == 'jumped':
                if element.jump_state:
                    element.back_to_floor()
                    element.jump_state -= 1
                else:
                    element.status = 'stationary'
            elif element.status == 'move right' or\
                element.status == 'move left':
                element.move()
            element.draw(self.screen)

def main():
    """
    entrypoint
    """
    game = Game()


if __name__ == '__main__':
    main()
