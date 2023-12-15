import csv
from tabulate import tabulate
import UI
from collections import Counter

class Table:

    def __init__(self):
        # Define column and row names
        self.col_names = ["DOWN", "UP", "RANDOM 1", "RANDOM 2", "CALL", "MIDDLE"]
        self.row_names = ["1", "2", "3", "4", "5", "6", "MAX", "MIN", "KENTA", "FULL", "POKER", "YAMB", "ROYAL"]

        # Create an empty table with the predefined dimensions
        self.rows = len(self.row_names)
        self.cols = len(self.col_names)
        self.table = [['' for _ in range(self.cols)] for _ in range(self.rows)]

    def calc_value(self, row_name, numbers):
        # Calculation for cells in rows 1-6
        if row_name in ['1','2','3','4','5','6']:
            n = int(row_name)
            return numbers.count(n) * n

        # In cells MIN and MAX you put in the sum of all 6 numbers
        elif row_name in ['MIN','MAX']:
            return sum(numbers)

        else:
            match row_name:
                case 'KENTA':
                    return self.kenta(numbers)
                case 'FULL':
                    return self.full(numbers)
                case 'POKER':
                    return self.poker(numbers)
                case 'YAMB':
                    return self.yamb(numbers)
                case 'ROYAL':
                    return self.royal(numbers)

    # If the player doesn't throw kenta, the result is 0, else 61
    def kenta(self, numbers):
        if numbers == [1, 2, 3, 4, 5, 6]:
            return 61
        else:
            return 0


    def full(self, numbers):
        # Count the occurrences of each number
        counts = []

        # Iterate over the unique values and count their occurrences
        counts = list(Counter(numbers).values())

        # Create a set of unique values in the numbers list
        unique_values = set(numbers)
        numbers_with_count_3 = []
        numbers_with_count_2 = []

        # Iterate over the unique values and count their occurrences
        for value in unique_values:
            count = numbers.count(value)
            if count == 3:
                numbers_with_count_3.append(value)
            elif count == 2:
                numbers_with_count_2.append(value)

        # Check if there are 2 distinc numbers in the given numbers set
        if len(counts) == 2:
             if counts[0] == 3:
                  return sum(numbers[-3:]) + sum(numbers[:2]) + 30
             elif counts[0] == 2:
                  return sum(numbers[-3:]) + sum(numbers[:2]) + 30
             elif counts[0] == 4:
                  return sum(numbers[-2:]) + sum(numbers[:3]) + 30
        # Check if there are three distinc numbers
        elif len(counts) == 3:
             return numbers_with_count_3[0] * 3 + numbers_with_count_2[0] * 2 + 30

        # If the conditions are not met
        return 0

    def poker(self, numbers):
        for x in numbers:
            if numbers.count(x) >= 4:
                return x * 4 + 40
        return 0

    def yamb(self, numbers):
        for x in numbers:
            if numbers.count(x) >= 5:
                return x * 5 + 50
        return 0

    def royal(self, numbers):
        for x in numbers:
            if numbers.count(x) >= 6:
                return x * 6 + 60
        return 0

    def is_cell_empty(self, row_name, col_name):
        row = self.row_names.index(row_name)
        col = self.col_names.index(col_name)
        if self.table[row][col] == '':
            return True
        else:
            return False

    def is_table_full(self):
        empty_cells = 0
        for col in range(self.cols):
            for row in range(self.rows):
                if self.table[row][col] == '':
                    empty_cells += 1
        if empty_cells > 0:
            return False
        else:
            return True

    def is_cell_writable(self, row_name, col_name):
        current_row_index = self.row_names.index(row_name)

        # Fisrt check if the cell is actually empty
        if not self.is_cell_empty(row_name, col_name):
            UI.error("This cell is filled already.\n")
            return False

        # Check if the column is "Down" and there is a previous row
        if col_name == "DOWN" and current_row_index > 0:
            previous_row_name = self.row_names[current_row_index - 1]
            if self.is_cell_empty(previous_row_name, col_name):
                UI.error("In column 'Down' you can only fill the cell, if the previous one in order is already filled.\n")
                return False

        # Check if the column is "Up" and there is a following row
        elif col_name == "UP" and current_row_index < len(self.row_names) - 1:
            following_row_name = self.row_names[current_row_index + 1]
            if self.is_cell_empty(following_row_name, col_name):
                UI.error("In column 'Up' you can only fill the cell, if the next one in order is already filled.\n")
                return False

        # Check if the column in 'MIDDLE' and it follows the rules for this column
        elif col_name == "MIDDLE":
            message = "In this column, you have to move from 'Max' up and from 'Min' down.\n"
            if current_row_index in range(6):
                # Rows in range(0 to 5)
                if self.is_cell_empty(self.row_names[current_row_index + 1], col_name):
                    UI.error(message)
                    return False
            elif current_row_index in range(8, 13):
                # Rows in range(8 to 12)
                if self.is_cell_empty(self.row_names[current_row_index - 1], col_name):
                    UI.error(message)
                    return False

        return True


    def update_table(self, row_name, col_name, value):
        row = self.row_names.index(row_name)
        col = self.col_names.index(col_name)
        self.table[row][col] = value

    def sum_first_6_rows(self):
        result = 0
        # Calculate result for each of the 6 columns
        for col in range(self.cols):
            column_sum = 0
            for row in range(6):
                cell_value = self.table[row][col]
                if cell_value == "":
                    cell_value = 0
                else:
                    cell_value = int(cell_value)

                column_sum += cell_value

            # Add 30 for each column where the sum of the first 6 rows is >= 60
            if column_sum >= 60:
                result += column_sum + 30
            else:
                result += column_sum

        return result

    def sum_max_min(self):
        result = 0
        for col in range(self.cols):
            value_max = self.table[6][col]
            value_min = self.table[7][col]
            value_1 = self.table[0][col]
            if value_max == '' or value_min == '' or value_1 == '':
                result = 0
            else:
                value_max = int(value_max)
                value_min = int(value_min)
                value_1 = int(value_1)
                result += ((value_max - value_min) * value_1)
        return result

    def sum_all(self):
        down_result = 0
        up_result = self.sum_first_6_rows()
        middle_result = self.sum_max_min()
        for col in range(self.cols):
            for row in range(8,13):
                cell_value = self.table[row][col]
                if cell_value == "":
                    cell_value = 0
                else:
                    cell_value = int(cell_value)
                down_result += cell_value
        result = down_result + up_result + middle_result
        return result


    def display_table(self):
        table_data = [[row_name] + row for row_name, row in zip(self.row_names, self.table)]
        headers = [''] + self.col_names
        table = tabulate(table_data, headers, tablefmt='pretty')
        print(table)

    def save_table_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.table)

    def load_table_from_csv(self, filename):
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            self.table = [row for row in reader]