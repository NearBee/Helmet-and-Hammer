import math
from typing import Union
from player import Player
from enemy import Enemy


OPTIONS = ["c", "l", "f"]

c = OPTIONS[0]
l = OPTIONS[1]
f = OPTIONS[2]


def battle(player: Player, enemy: Enemy) -> bool:
    player_health = player.health
    enemy_health = enemy.health
    while player_health > 0 and enemy_health > 0:

        while True:
            player_choice = input(
                f"\nCurrent Health: Player - {player_health}, {enemy} - {enemy_health}\nWill you use (c)ounter, (l)unge or (f)erocious strike? "
            ).lower()
            if player_choice != OPTIONS:
                break
        enemy_choice = enemy.weighted_preference()

        if player_choice == enemy_choice:
            print(f"\nBoth players chose [{player_choice}], resulting in no damage!\n")
            continue

        elif player_choice == c:
            if enemy_choice == f:
                print(f"{player.name} has countered {enemy.name}'s ferocious strike!")
                enemy_health -= damage(player, enemy, 0.6)
            else:
                print(f"{enemy.name} pierced {player.name}'s defenses!")
                player_health -= damage(enemy, player, 0.8)

        elif player_choice == l:
            if enemy_choice == c:
                print(
                    f"{player.name} has gone and pierced through {enemy.name}'s defenses!"
                )
                enemy_health -= damage(player, enemy, 0.8)
            else:
                print(f"{enemy.name}'s ferocity has bested {player.name}'s lunge!")
                player_health -= damage(enemy, player, 1.2)

        elif player_choice == f:
            if enemy_choice == l:
                print(
                    f"{player.name} has foregone defenses to ferociously strike {enemy.name}!"
                )
                enemy_health -= damage(player, enemy, 1.2)
            else:
                print(
                    f"{enemy.name}'s defensive stance quelled {player.name}'s ferocious strike!"
                )
                player_health -= damage(enemy, player, 0.6)

    if player_health <= 0:
        print(f"\n{enemy.name} has defeated {player.name}!\n")
        return False
    else:
        print(f"\nYou've defeated {enemy.name}!")
        return True


def damage(
    attacker: Union[Player, Enemy], defender: Union[Player, Enemy], modifier: float
) -> int:
    """Calculate damage dealt by attacker to defender"""
    """Doing the calculation here lets us use the same function for both player and enemy and test various scenarios"""

    dmg = max(
        1, math.floor((attacker.strength * (1 - (defender.defense / 10))) * modifier)
    )

    print(
        f"Attacker strength: {attacker.strength}, Defender defense: {defender.defense}, Damage: {dmg}"
    )
    return dmg


if __name__ == "__main__":
    battle(player=Player("", "Human", 10, 5, 5), enemy=Enemy())
