import random
import UI
from player import Player

ask_for_instructions = "If you play the game for the first time, you can type '?'/'help'/'h' and press 'Enter' anytime to get detailed instructions. If no, just press 'Enter'. "
get_help = ["?", "help", "h"]

def game_setup():
    UI.introduction("\nWelcome to the game of dices (in Slovenia called 'KOCKE')!\n\n")

    if input(ask_for_instructions).lower() in get_help:
        display_instructions('instructions.txt')
        input()

    players = get_players()

    print("\nThis will be your table. Let's fill it!")

    players[0].table.display_table()

    sorted_players = decide_starting_player(players)

    input(f"\nAre you ready to roll? Press 'enter' to begin.\n")

    return sorted_players


def display_instructions(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print("Instructions file not found.")

def get_players():
    # Returns a list with two names
    UI.introduction("\nTell me the name of the player 1 and the name of the player 2.")
    while True:
        team1 = input("Player 1: ").upper().strip()
        team2 = input("Player 2: ").upper().strip()

        if team1 in get_help or team2 in get_help:
            display_instructions('instructions.txt')
        elif team1 == team2:
            UI.sorry("Go find some friends, you can't play alone...")
        else:
            players = [Player(team1), Player(team2)]

            UI.introduction(f"\nHello {players[0].name} and {players[1].name}!\n")

            return players


def decide_starting_player(players):
    sorted_players = False
    # The decision on starting player is random
    while not sorted_players:
        n1 = random.randint(1, 2)
        n2 = random.randint(1, 2)

        if n1 > n2:
            sorted_players = players
        elif n1 < n2:
            sorted_players = players.reverse()

    UI.sorry(f"The ugliest player starts, so {sorted_players[0]} you go first :p")

    return sorted_players