'''
Name: bullet.py
Author: Luke Atkins
Purpose: Handles bullet drawing and movement code
Starter Code: No starter code used
Date: 4/7/2026
'''


import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """
    The main bullet type within the game
    """
    def __init__(self, game: "AlienInvasion") -> None:
        """
        Creates and returns instance of bullet

        Args:
            game: (AlienInvasion) instance of the alien invasion game
        
        Returns:
            None
        """
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            self.settings.bullet_file
        )
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )
        self.image = pygame.transform.rotate(
            self.image,
            -90
        )

        self.rect = self.image.get_rect()
        self.rect.midright = game.ship.rect.midright
        self.x = float(self.rect.x)
    
    def update(self, delta: float) -> None:
        """
        Updates the position of the bullet

        Args:
            delta: the amount of time that has passed since the last frame (seconds)

        Returns:
            None
        """
        self.x += self.settings.bullet_speed * delta
        self.rect.x = self.x
    
    def draw_bullet(self) -> None:
        """
        Draws the bullet onto the screen

        Args:
            None

        Returns:
            None
        """
        self.screen.blit(
            self.image, self.rect
        )