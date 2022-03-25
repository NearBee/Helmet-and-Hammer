import random


OPTIONS = ["c", "l", "f"]  # Possible choices to be used in weighted_preference()


class Enemy:
    """Creates a new enemy"""

    # Dicitonary of possible races with their respective stat ranges
    races = {
        "Goblin": {
            "name": ["Lunk", "Wakz", "Bezz", "Bath", "Darx"],
            "health": (3, 5),
            "strength": (3, 4),
            "defense": (4, 5),
            "preference": (30, 45, 25),
        },
        "Undead": {
            "name": ["Past", "Levin", "Eddy", "Nicalaus", "Fern"],
            "health": (2, 6),
            "strength": (2, 6),
            "defense": (2, 6),
            "preference": (40, 25, 35),
        },
        "Orc": {
            "name": ["Gulm", "Hateahh", "Snat", "Slapdud", "Dabub"],
            "health": (4, 7),
            "strength": (5, 8),
            "defense": (5, 7),
            "preference": (20, 25, 55),
        },
    }

    def __init__(self) -> None:
        """Initializes a randomized enemy with randomized stats"""
        race = random.choice(list(self.races.keys()))
        curr_race = self.races[race]

        self.name = random.choice(curr_race["name"])
        self.race = race
        self.health = random.randint(curr_race["health"][0], curr_race["health"][1])
        self.defense = random.randint(curr_race["defense"][0], curr_race["defense"][1])
        self.strength = random.randint(
            curr_race["strength"][0], curr_race["strength"][1]
        )
        self.preference = curr_race["preference"]

    def weighted_preference(self) -> str:
        """Method used to take the preference tuple parameter and output a weighted choice"""
        return random.choices(OPTIONS, weights=self.preference)[0]

    def __str__(self):
        return self.name


if __name__ == "__main__":
    print(Enemy().__dict__)
