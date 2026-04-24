
from typing import TYPE_CHECKING
from pathlib import Path
import json

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats:
    def __init__(self, game: "AlienInvasion"):
        self.game = game
        self.settings = game.settings
        self.score = 0
        self.level = 1
        self.init_saved_scores()
        self.reset_stats()
    
    def init_saved_scores(self):
        self.path = self.settings.score_file

        if self.path.exists() and self.path.stat().st_size > 0:
            content = self.path.read_text()
            scores = json.loads(content)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
        
    def save_scores(self):
        scores = {
            'hi_score': self.hi_score
        }
        
        content = json.dumps(scores, indent=0)
        self.path.mkdir(parents=True, exist_ok=True) # have the wrong path and so I added this as a fail safe
        self.path.touch(exist_ok=True) # if file no exist

        try:
            

            self.path.write_text(content)
        except FileNotFoundError as e:
            print(f"File not found: {e}")


    def reset_stats(self):
        self.level = 1
        self.score = 0
        self.ships_left = self.settings.starting_ship_count

    def update(self, collisions) -> None:
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
    
    def _update_score(self, collisions: list):
        for alien in collisions.values():
            self.score += self.settings.alien_points
        
    def update_level(self):
        self.level += 1