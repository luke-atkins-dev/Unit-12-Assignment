'''
Name: alien_invasion.py
Author: Luke Atkins
Purpose: Create and run the main instance of Alien Invasion
Starter Code: No starter code used
Date: 4/7/2026
'''

import sys
import pygame

class AlienInvasion:
    '''
    The main instance of Alien Invasion

    handles pygame window, events, and game loop
    '''
    def __init__(self):
        self.display_info = pygame.display.Info()
        

        if not pygame.get_init():
            # No need to initialize pygame several times although this code will only be run once
            pygame.init()
        
        self.screen = pygame.display.set_mode(
            self._get_desired_window_resolution()
        )
    def _get_desired_window_resolution(self) -> tuple[int, int]:
        display_info = self.display_info

        return (display_info.current_h, display_info.current_w)
    def run() -> None:
        pass

if __name__ == '__main__':
    pass
