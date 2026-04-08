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
    
    def run(self) -> None:
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event == pygame.quit:
                    self.quit()
            
            dt = self.clock.tick(self.settings.FPS)

            pygame.display.flip()
    def quit(self) -> None:
        """
        Stops main game loop and stops Python execution
        """
        self.running = False
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    AlienInvasion()
