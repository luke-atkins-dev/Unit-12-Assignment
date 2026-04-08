from pathlib import Path

'''
Name: alien_invasion.py
Author: Luke Atkins
Purpose: Manages game config and source files
Starter Code: No starter code used
Date: 4/7/2026
'''

class Settings:
    """
    Stores settings and paths to image files
    """
    def __init__(self) -> None:
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.resolution: tuple[int, int] = (self.screen_w, self.screen_h)
        self.FPS: int = 60
        self.bg_file: Path = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"
        self.ship_file: Path = Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        self.ship_w = 40
        self.ship_h = 60