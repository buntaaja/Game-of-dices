from table import Table

class Player:
    def __init__(self, name):
        self.name = name
        self.table = Table()  # Create a new table for each new player

    def __str__(self):
        return self.name