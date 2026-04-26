'''
Name: alien_invasion.py
Author: Luke Atkins
Purpose: Create and run the main instance of Alien Invasion
Starter Code: No starter code used
Date: 4/7/2026
'''

from Settings import Settings
import sys
import pygame
from ship import Ship
from arsenal import ShipArsenal
from alien_fleet import AlienFleet
from button import Button
from game_stats import GameStats
from time import sleep
from hud import HUD

class AlienInvasion:
    '''
    The main instance of Alien Invasion

    handles pygame window, events, and game loop
    '''
    def __init__(self) -> None:
        """
        Initializes an instance of the Alien Invasion game

        Args:
            None

        Returns:
            None
        """
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.game_stats = GameStats(self)

        if not pygame.get_init():
            # No need to initialize pygame several times although this code will only be run once
            pygame.init()
            pygame.mixer.init()
        
        self.screen = pygame.display.set_mode(
            self.settings.resolution
        )
        pygame.display.set_caption(self.settings.name)
        self.HUD = HUD(self)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg,
            self.settings.resolution
        )
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(self.settings.laser_volume)
        self.clock = pygame.time.Clock()
        self.running = False
        self.game_active = False
        
        self.ship = Ship(self, ShipArsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.play_button = Button(self, "Play")
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(self.settings.impact_volume)
        
    def _update_screen(self) -> None:
        """
        (Private)

        Draws background and ship

        Args:
            None

        Returns:
            None
        """

        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()

        pygame.display.flip()

    def run(self) -> None:
        """
        Creates and runs the main game loop

        Args:
            None

        Returns:
            None
        """
        self.running = True

        while self.running:
            self._check_events()
            
            dt_ms = self.clock.tick(self.settings.FPS)
            # print(dt_ms)
            # this is done because the delta time is returned in milliseconds so we are converting to seconds
            # dt = dt_ms / 1000
            dt = 0.025
            
            self._update_screen()

            if self.game_active:
                self.ship.update(dt)
                self.alien_fleet.update_fleet(dt)
                self._check_collisions()

    def _check_collisions(self) -> None:
        """
        Checks whether the fleet has passed the player or an alien is colliding with the player

        Args:
            None

        Returns:
            None
        """
        fleet_passed_player = self.alien_fleet.has_fleet_passed_player(self.ship)
        ship_hit_fleet = self.ship.check_collisions(self.alien_fleet.fleet)
        if ship_hit_fleet or fleet_passed_player:
            self._reset_level()
        
        # check if fleet is destroyed
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
        
        # check if bullets collided with aliens
        collisions = self.alien_fleet._check_collisions(self.ship.arsenal.arsenal, True, True)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()
    
    def _check_game_status(self):
        if self.game_stats.ships_left > 0:
            self.game_stats.ship_stats -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False
    
    def _reset_level(self) -> None:
        """
        Resets the game state

        Args:
            None

        Returns:
            None
        """
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _check_events(self) -> None:
        """
        (Private)

        Checks key and quit events

        Args:
            None

        Returns:
            None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN and self.game_active:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP and self.game_active:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def restart_game(self):
        self.settings.initialize_dynamic_settings()
        self.game_active = True
        pygame.mouse.set_visible(False)
        self._reset_level()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self.ship._center_ship()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()
    
    def _check_keydown_event(self, event) -> None:
        """
        (Private)

        Handles all keydown events

        Args:
            event: (pygame.event.Event) the event to be processed
        
        Returns:
            None
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_up = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.quit()

    def _check_keyup_event(self, event) -> None:
        """
        (Private)

        Handles all keyup events

        Args:
            event: (pygame.event.Event) the event to be processed
        
        Returns:
            None
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_up = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_down = False

    def quit(self) -> None:
        """
        Stops main game loop and stops Python execution

        Args:
            None

        Returns:
            None
        """
        self.running = False
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    AlienInvasion().run()
