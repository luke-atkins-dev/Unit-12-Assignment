from pathlib import Path

'''
Name: alien_invasion.py
Author: Luke Atkins
Purpose: Manages game config and source files
Starter Code: No starter code used
Date: 4/7/2026
'''

project = Path(__file__).parent

class Settings:
    """
    Stores settings and paths to image files
    """
    def __init__(self) -> None:
        """
        Initializes all constants and path objects
        """
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.resolution: tuple[int, int] = (self.screen_w, self.screen_h)
        self.FPS: int = 60
        self.bg_file: Path = project / "Assets" / "images" / "Starbasesnow.png"
        self.ship_file: Path = project / "Assets" / "images" / "ship2(no bg).png"
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        self.bullet_file = project / "Assets" / "images" / "laserBlast.png"
        self.laser_sound = project / "Assets" / "sound" / "laser.mp3"
        self.laser_volume = 0.5
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.alien_file = project / "Assets" / "images" / "enemy_4.png"
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 8
        self.fleet_direction = 1
        self.fleet_drop_speed = 40