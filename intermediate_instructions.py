def help_filling():
    print("""You need to specify the column and row of the cell you would like to fill.
If you would like to fill a cell that requires a certain amount of the same or different numbers and you don't have them,
you get a score 0 in this cell.

For example, if you want to fill the cell Poker, but you threw 3 x 3 and 3 x 4, you will get a zero.""")

def help_calling():
     print("If you want to fill the column 'CALL' you need to decide which cell to fill after the first throw")

def help_deciding():
     print("""Are you happy with your throw, or would you like to throw again?
If you're happy type 'all'/'a' to keep all and not throw again.
If you are throwing again, specify which dices you would like to keep
(by typing the numbers on the dices, separated by a comma),
if not even one just press 'enter'. """)