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

class AlienInvasion:
    '''
    The main instance of Alien Invasion

    handles pygame window, events, and game loop
    '''
    def __init__(self) -> None:
        self.settings = Settings()

        if not pygame.get_init():
            # No need to initialize pygame several times although this code will only be run once
            pygame.init()
        
        self.screen = pygame.display.set_mode(
            self.settings.resolution
        )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg,
            self.settings.resolution
        )
        self.clock = pygame.time.Clock()
        self.running = False
        
        self.ship = Ship(self, ShipArsenal(self))
    def _update_screen(self, dt: float):
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        pygame.display.flip()

    def run(self) -> None:
        self.running = True
        while self.running:
            self._check_events()
            
            dt = self.clock.tick(self.settings.FPS)
            self.ship.update()
            self._update_screen(dt)


    def _check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
    
    def _check_keydown_event(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.quit()

    def _check_keyup_event(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def quit(self) -> None:
        """
        Stops main game loop and stops Python execution
        """
        self.running = False
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    AlienInvasion().run()
