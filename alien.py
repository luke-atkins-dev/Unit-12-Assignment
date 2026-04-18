'''
Name: alien.py
Author: Luke Atkins
Purpose: Handles rendering and positiong on alien
Starter Code: No starter code used
Date: 4/7/2026
'''


import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """
    The main bullet type within the game
    """
    def __init__(self, alien_fleet: "AlienFleet", x: float, y: float) -> None:
        """
        Creates and returns instance of bullet

        Args:
            game: (AlienInvasion) instance of the alien invasion game
        
        Returns:
            None
        """
        super().__init__()
        self.fleet = alien_fleet
        self.screen = alien_fleet.screen
        self.settings = alien_fleet.settings
        self.boundaries = alien_fleet.screen.get_rect()

        self.image = pygame.image.load(
            self.settings.alien_file
        )
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h)
        )
        self.image = pygame.transform.rotate(
            self.image,
            -90
        )

        self.rect = self.image.get_rect()
        # self.rect.midright = game.ship.rect.midright
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self) -> None:
        """
        Updates the position of the alien

        Args:
            None

        Returns:
            None
        """
        temp_speed = self.settings.fleet_speed

        # if self.check_edges():
            # self.settings.fleet_direction *= -1
            # self.y += self.settings.fleet_drop_speed


        self.y += temp_speed * self.fleet.fleet_direction

        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        print(f'{self.boundaries.top=}\n{self.boundaries.bottom}')
        return (self.rect.bottom >= self.boundaries.bottom or self.rect.top <= self.boundaries.top)
    
    def draw_alien(self) -> None:
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