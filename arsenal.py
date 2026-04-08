'''
Name: arsenal.py
Author: Luke Atkins
Purpose: Contains class for limiting the bullet count to the config and deleting bullets off screen
Starter Code: No starter code used
Date: 4/7/2026
'''

import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class ShipArsenal:
    """
    Acts like a container for all bullets on screen.
    Manages bullet count and deletes bullets that are off screen
    """
    def __init__(self, game: "AlienInvasion") -> None:
        """
        Intializes Arsenal instance

        Args:
            game: (AlienInvasion) the main instace of alien invasion

        Returns:
            None
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()
        self.boundaries = game.screen.get_rect()
    
    def update_arsenal(self) -> None:
        """
        Updates the arsenal for each frame.

        Args:
            None

        Returns:
            None
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()
    
    def _remove_bullets_offscreen(self) -> None:
        """
        (Private)

        Removes bullets that are off the main display

        Args:
            None

        Returns:
            None
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.left > self.boundaries.right:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """
        Draws all bullets onto the screen

        Args:
            None

        Returns:
            None
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()
    
    def fire_bullet(self) -> bool:
        """
        Fires a bullet within the container

        Args:
            None

        Returns:
            bool: whether the bullet was able to fire
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)

            return True
        return False