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
from pygame.sprite import Group, spritecollideany

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
        self._center_ship()

        self.moving_up = False
        self.moving_down = False
        self.arsenal = arsenal

    def _center_ship(self) -> None:
        """
        Recenters the ship to the starting point

        Args:
            None
        
        Returns:
            None
        """
        self.rect.midleft = self.boundaries.midleft
        self.y = float(self.rect.y)
    
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

    def update(self, delta: float) -> None:
        """
        Updates the ships movement and arsenal

        Args:
            None

        Returns:
            None
        """
        self._update_ship_movement(delta)
        self.arsenal.update_arsenal(delta)
        
    def _update_ship_movement(self, delta: float) -> None:
        """
        (Private)

        Updates the ship's movement

        Args:
            delta: the amount of time that has passed since the last frame (seconds)

        Returns:
            None
        """
        speed = self.settings.ship_speed
        if self.moving_up and self.rect.bottom < self.boundaries.bottom:
            self.y += speed * delta
        if self.moving_down and self.rect.top > self.boundaries.top:
            self.y -= speed * delta
        
        self.rect.y = self.y
        self.x = self.rect.x
    
    def fire(self) -> bool:
        """
        Fire's bullet within the current arsenal

        Args:
            None

        Returns:
            bool: whether the bullet was able to fire
        """
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group: Group):
        """
        Checks if ship collides with other sprite group

        Args:
            other_group: the sprite group to see if collides with ship

        Returns:
            bool: whether the two groups did collide
        """
        did_collide = spritecollideany(self, other_group)
            
        if did_collide:
            # life lost
            self._center_ship()
        
        return did_collide