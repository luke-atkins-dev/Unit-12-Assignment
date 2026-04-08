'''
Name: ship.py
Author: Luke Atkins
Purpose: Holds the class for the ship object used within the game
Starter Code: No starter code used
Date: 4/7/2026
'''

import pygame
from Settings import Settings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Ship:
    def __init__(self, game: "AlienInvasion") -> None:
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.image = pygame.image.load(
            self.settings.ship_file
        )
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_w, self.settings.ship_h)
        )
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom

        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
    
    def draw(self) -> None:
        self.screen.blit(self.image, self.rect)
    
    def update(self) -> None:
        speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= speed
        
        self.rect.x = self.x