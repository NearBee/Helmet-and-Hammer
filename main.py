from player import Player
from enemy import Enemy
from time import sleep
from os import system, name
from rps import battle


def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def combat() -> None:
    wins = 0
    losses = 0
    battles = 0
    combat = True

    while True:
        player_input = input("What is your name adventurer? ").strip().capitalize()
        if player_input != "":
            break
    player = Player(player_input, "Human", 10, 5, 5)

    clear_screen()
    print(f"\n Welcome to the arena, {player.name}\n")

    while combat:

        enemy = Enemy()

        print(
            f"\nYou're greeted by {enemy} the {enemy.race} champion! Prepare for combat!\n"
        )
        sleep(1)
        fight = input("\nWill you stand to the challenge y/n? ").lower()
        if fight == "y":
            clear_screen()
            battles += 1
            result = battle(player, enemy)
            if result:
                wins += 1
            else:
                losses += 1
                if losses >= 3:
                    combat = False
                    print(f"\nSorry ran out of lives :(....try again\n")
                    sleep(2)
        else:
            combat = False
    clear_screen()
    sleep(1)
    print(f"Wins: {wins}, Losses: {losses}, Total Battles: {battles}\n")
    print(f"Thank you for playing {player.name}!\n")


if __name__ == "__main__":
    combat()
