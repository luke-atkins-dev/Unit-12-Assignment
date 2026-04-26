
import pygame
from typing import TYPE_CHECKING
from alien import Alien
from math import floor

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet():
    """
    Controls the position of the alien enemies and makes them move down when they've reached the edge
    """
    def __init__(self, game: "AlienInvasion") -> None:
        """
        Initializes instance

        Args:
            game: AlienInvasion, main instance of the game

        Returns:
            AlienFleet
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self) -> None:
        """
        Calculates fleet size and offsets then creates alien enemies

        Args:
            None

        Returns:
            None
        """
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = AlienFleet.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        
        # apply fleet_product
        # represents what percentage of the screen the enemies should cover on the horizontal axis
        fleet_w = floor(fleet_w * self.settings.fleet_product)

        x_offset, y_offset = self.extract_offsets(alien_w, screen_w, fleet_w, fleet_h)
        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset) -> None:
        """
        Creates grid of aliens

        Args:
            alien_w: int, width of the alien enemy
            alien_h: int, height of the alien enemy
            fleet_w: int, width of the fleet
            fleet_h: int, height of the fleet
            x_offset: int, horizontal offset applied to enemy spawn position
            y_offset: int, vertical offset applied to enemy spawn position

        Returns:
            None
        """
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset

                if col % 2 == 0 or row % 2 == 0:
                    continue

                self._create_alien(current_x, current_y)

    def extract_offsets(self, alien_w, screen_w, fleet_w, fleet_h) -> tuple[int, int]:
        """
        Calculates the spawn offset of the enemies

        Args:
            alien_w: int, width of the alien enemy
            screen_w: int, the width of the screen
            fleet_w: int, width of the fleet
            fleet_h: int, height of the fleet

        Returns:
            tuple[int, int] the offsets
        """
        fleet_horizonal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_w

        x_offset = int((screen_w - (fleet_horizonal_space//2)) // 2)
        y_offset = int((self.settings.screen_h - fleet_vertical_space) // 2)
        
        return x_offset, y_offset
    
    def update_fleet(self, delta: float) -> None:
        """
        Updates sprite group and checks if sprites are colliding with top/bottom of screen

        Args:
            delta: the amount of time that has passed since the last frame (seconds)

        Returns:
            None
        """
        alien: "Alien"

        self._check_fleet_edges()

        self.fleet.update(delta)
            

    def _check_collisions(self, other_group: pygame.sprite.Group, kill_bullets: bool, kill_other_group: bool) -> None:
        """
        Checks if alien group collides with other sprite group

        Args:
            other_group: the other group to check
            kill_bullets: whether to remove bullets from the sprite group
            kill_other_group: whether to remove the sprites from the other group

        Returns:
            None
        """
        
        return pygame.sprite.groupcollide(
            self.fleet,
            other_group,
            kill_bullets,
            kill_other_group
        )

    def _check_fleet_edges(self) -> None:
        """
        Checks if any alien within the sprite group has collided with the edge of the screen
        
        Args:
            None

        Returns:
            None
        """
        alien: "Alien"
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def check_destroyed_status(self) -> bool:
        return len(self.fleet) <= 0

    def has_fleet_passed_player(self, player: pygame.sprite.Sprite) -> bool:
        """
        Checks whether the fleet of enemies has passed the player/ship's position horizontally
        
        Args:
            player: Ship the player ship instance

        Returns:
            bool: whether any enemy has passed the player
        """
        alien: "Alien"
        for alien in self.fleet:
            if alien.x <= player.x:
                return True

    def _drop_alien_fleet(self) -> None:
        """
        Moves the aliens down the screen closer to the player

        Args:
            None

        Returns:
            None
        """
        for alien in self.fleet:
            alien.x -= self.fleet_drop_speed

    def calculate_fleet_size(alien_w: float, screen_w: float, alien_h: float, screen_h: float) -> tuple[int, int]:
        """
        Calculates the number of alien enemies based off screen and alien size

        Args:
            None

        Returns:
            tuple[int, int]: alien count horizontally, alien count vertically
        """
        # in the video it makes this an instance method but it does not need to be
        fleet_w = (screen_w//alien_w)
        fleet_h = (screen_h//alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2
        
        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2
        
        return int(fleet_w), int(fleet_h)
    
    def _create_alien(self, current_x: int, current_y: int) -> None:
        """
        Creates alien and adds it to fleet sprite group

        Args:
            current_x: where to spawn the enemy on the x axis
            current_y: where to spawn the enemy on the y axis

        Returns:
            None
        """
        
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)
    
    def draw(self) -> None:
        """
        Draws all aliens to the screen

        Args:
            None

        Returns:
            None
        """
        alien: "Alien"
        for alien in self.fleet:
            alien.draw_alien()