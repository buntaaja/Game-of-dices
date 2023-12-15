from first_part import game_setup
from round import round
import UI

def main():
    #----------------------- PART 1 - Setup-------------------------------
    players = game_setup()
    # players = [Player('TEST PLAYER 1'), Player('TEST PLAYER 2')]

    #----------------------- PART 2 - Play--------------------------------
    # While any player's table is still not full, play
    while not players[0].table.is_table_full() and not players[1].table.is_table_full():
        round(players[0])
        round(players[1])

    #-----------------------PART 3 - Count results-------------------------
    announce_winner(players)


############################################################################
def announce_winner(players):
    player1_score = players[0].table.sum_all()
    player2_score = players[1].table.sum_all()

    print(f"{players[0].name} has a score {player1_score} and {players[1].name} has a score {player2_score}.\n")

    if player1_score > player2_score:
        UI.success(f'WINNER IS: {players[0].name}!')
    elif player1_score < player2_score:
        UI.success(f'WINNER IS: {players[1].name}!')
    else:
        print('Unlikely tie')

    print(players[0].name)
    players[0].table.display_table()
    print(players[1].name)
    players[1].table.display_table()


if __name__ == "__main__":
    main()