import random
import UI
from intermediate_instructions import help_filling, help_calling, help_deciding
get_help = ["?", "help", "h"]

def round(player):
    UI.introduction(f"\n{player.name}'s turn.")
    keep_first_throw, cell = decision1(player)
    keep_second_throw = decision2(keep_first_throw)
    final_keep = decision3(keep_second_throw)
    fill_the_cell(player, final_keep, cell)

def roll_dice(n):
    # Roll N dices
    return [random.randint(1, 6) for _ in range(n)]

# Decision after the first throw
def decision1(player):
    input("Press 'enter' to throw.")
    result = sorted(roll_dice(6))
    UI.show(f"\nThrow #1: {result}")
    player.table.display_table()
    dices_kept = decision_which_to_keep(result)
    is_call = UI.text_input("Call? (y)  ")
    cell = []
    if is_call in get_help:
        help_calling()
    elif is_call == "Y":
        while True:
            print("Which cell in the column 'CALL' would you like to fill?")
            row_name = UI.text_input("Enter the row name: ")
            col_name = "CALL"

            if row_name not in player.table.row_names:
                UI.error("Invalid row name. Try again.\n")
                continue

            if player.table.is_cell_empty(row_name, col_name):
                cell = [row_name, col_name]
                break

    return dices_kept, cell

# Decision after the second throw
def decision2(dices_kept):
    if len(dices_kept) == 6:
        return dices_kept

    rerolled_dices = roll_dice(6 - len(dices_kept))

    result = sorted(rerolled_dices + dices_kept)
    UI.show(f"\nThrow #2: {rerolled_dices}. Previously kept: {dices_kept}")
    kept_dices = decision_which_to_keep(result)
    return kept_dices

# Decision where to put in the table after the third throw
def decision3(kept_dices):
    if len(kept_dices) == 6:
        return kept_dices

    dices_to_throw = 6 - len(kept_dices)
    result = roll_dice(dices_to_throw)
    UI.show(f"\nThrow #3: {result}. Previously kept: {kept_dices}")
    result = sorted(result + kept_dices)
    UI.warning(f"\nYour final numbers are: {result}\n")
    return result

def count_occurrences(list):
    counts = {}
    for item in list:
        counts[item] = counts.get(item, 0) + 1
    return counts

# Check if the player actually threw the numbers that he wants to keep
def is_valid(kept_dices, result):
    try:
        kept_dices = list(map(int, kept_dices.split(",")))
        result_counts = count_occurrences(result)
        user_input_counts = count_occurrences(kept_dices)
        valid_selection = True

        for dice, count in user_input_counts.items():
            if dice not in result_counts or count > result_counts[dice]:
                if count == 1:
                    print(f"You didn't roll {dice}. Try again: ")
                else:
                    print(f"You didn't roll {count}x {dice}. Try again: ")
                valid_selection = False
                break

        if valid_selection:
            return valid_selection

    except ValueError:
        get_help = ["help", "h", "?"]
        if kept_dices.lower() in get_help:
            help_deciding()
        else:
            UI.error("We are playing with numbers here...")
        valid_selection = False

    return valid_selection

# Check if and how many numbers after a throw would a player like to keep
def decision_which_to_keep(result):
    while True:
        keep_all = ["all", "a"]
        dices_to_keep = UI.text_input("Keeping: ").replace(" ", "")


        if dices_to_keep == "":
            return []  # User wants to keep none
        if dices_to_keep.lower() in keep_all:
            return result
        elif is_valid(dices_to_keep, result):
            dices_to_keep = list(map(int, dices_to_keep.split(",")))
            return dices_to_keep

# Check if the desired location in the table exists, if it's empty and he can fill it freely (without extra rules)
def choose_the_cell(player, called_cell):
    while True:
        print("Which cell would you like to fill?")
        row_name = UI.text_input("Enter the row name: ")
        col_name = UI.text_input("Enter the column name: ")
        cell = [row_name, col_name]
        if row_name in get_help or col_name in get_help:
            help_filling()
            continue

        if row_name not in player.table.row_names:
            UI.error("Invalid row name. Try again.\n")
            continue

        if col_name not in player.table.col_names:
            UI.error("Invalid column name. Try again.\n")
            continue

        if col_name == "CALL":
            if len(called_cell) != 2:
                UI.error("You can't choose the 'CALL' column, if you didn't chose it after the first throw\n")
                continue

        if player.table.is_cell_writable(row_name, col_name):
            return cell

# After establishing the desired cell in the table to fill,
# check if the result would be 0 so that player doesn't make mistakes
def fill_the_cell(player, numbers, called_cell):
    if len(called_cell) == 2:
        row_name, col_name = called_cell
        result = player.table.calc_value(row_name, numbers)
        player.table.update_table(row_name, col_name, result)
        UI.show(f"\nUpdated {player}'s table:")
        player.table.display_table()
        return

    while True:
        row_name, col_name = choose_the_cell(player, called_cell)
        result = player.table.calc_value(row_name, numbers)

        if result == 0:
            confirmation = UI.warning_input("\nThe result will be 0. Are you sure? (y/n): ")

            if confirmation != "Y":
                UI.error("Update canceled.\n")
                continue


        player.table.update_table(row_name, col_name, result)
        UI.show(f"\nUpdated {player}'s table:")
        player.table.display_table()
        return