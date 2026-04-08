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
    from arsenal import ShipArsenal as Arsenal

class Ship:
    """
    Ship object that handles firing and rendering of the ship
    """
    def __init__(self, game: "AlienInvasion", arsenal: "Arsenal") -> None:
        """
        Initalizes the ship

        Args:
            game: (AlienInvasion) the main instance of the game
            arsenal: (ShipArsenal) the bullet container for the ship
        """
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
        self.image = pygame.transform.rotate(
            self.image,
            -90
        )
        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft

        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)
        self.arsenal = arsenal
    
    def draw(self) -> None:
        """
        Draws the ship's bullets and the ship itself

        Args:
            None

        Returns:
            None
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        """
        Updates the ships movement and arsenal

        Args:
            None

        Returns:
            None
        """
        self._update_ship_movement()
        self.arsenal.update_arsenal()
    
    def _update_ship_movement(self) -> None:
        """
        (Private)

        Updates the ship's movement

        Args:
            None

        Returns:
            None
        """
        speed = self.settings.ship_speed
        if self.moving_up and self.rect.bottom < self.boundaries.bottom:
            self.y += speed
        if self.moving_down and self.rect.top > self.boundaries.top:
            self.y -= speed
        
        self.rect.y = self.y
    
    def fire(self) -> bool:
        """
        Fire's bullet within the current arsenal

        Args:
            None

        Returns:
            bool: whether the bullet was able to fire
        """
        return self.arsenal.fire_bullet()