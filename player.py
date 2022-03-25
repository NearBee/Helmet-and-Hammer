from dataclasses import dataclass


@dataclass
class Player:
    """This is the Player's class"""

    name: str
    race: str = "Human"
    health: int = 10
    defense: int = 5
    strength: int = 5

    def __str__(self):
        return self.name


### TODO create a way to save player's data to be loaded at a later time ###
def save_player(self):
    """Used to save player data to be loaded at a later time"""
