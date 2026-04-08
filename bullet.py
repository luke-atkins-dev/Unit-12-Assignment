
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: "AlienInvasion") -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        