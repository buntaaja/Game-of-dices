from table import Table
from round import roll_dice, count_occurrences, is_valid

# Testing class Table
t = Table()
t.save_table_to_csv('testing_table.csv')
full_table = Table()
full_table.load_table_from_csv('testing_full_table.csv')
full_table.display_table()

def test_calc_value():
    assert t.calc_value("1", [1,1,1,2,3,4]) == 3
    assert t.calc_value("2", [1,1,1,2,3,4]) == 2
    assert t.calc_value("4", [1,1,1,2,3,4]) == 4
    assert t.calc_value("MIN", [1,1,1,2,3,4]) == 12
    assert t.calc_value("MAX", [1,1,1,2,3,4]) == 12
    assert t.calc_value("KENTA", [1,1,1,2,3,4]) == 0
    assert t.calc_value("KENTA", [1,2,3,4,5,6]) == 61
    assert t.calc_value("FULL", [1,1,1,2,3,4]) == 0
    assert t.calc_value("FULL", [1,1,1,2,2,4]) == 37
    assert t.calc_value("FULL", [1,1,1,2,2,2]) == 38
    assert t.calc_value("FULL", [1,1,2,2,2,4]) == 38
    assert t.calc_value("POKER", [1,1,1,2,3,4]) == 0
    assert t.calc_value("POKER", [1,1,1,1,3,4]) == 44
    assert t.calc_value("YAMB", [1,1,1,2,3,4]) == 0
    assert t.calc_value("YAMB", [1,1,1,1,1,4]) == 55
    assert t.calc_value("ROYAL", [1,2,4,4,5,6]) == 0
    assert t.calc_value("ROYAL", [1,1,1,1,1,1]) == 66

def test_kenta():
    assert t.kenta([1,1,1,2,3,4]) == 0
    assert t.kenta([1,2,3,4,5,6]) == 61

def test_full():
    assert t.full([1,1,1,2,2,4]) == 37
    assert t.full([1,1,1,2,2,2]) == 38
    assert t.full([1,1,2,2,2,4]) == 38

def test_poker():
    assert t.poker([1,1,1,2,3,4]) == 0
    assert t.poker([1,1,1,1,3,4]) == 44

def test_yamb():
    assert t.yamb([1,1,1,2,3,4]) == 0
    assert t.yamb([1,1,1,1,1,4]) == 55

def test_royal():
    assert t.royal([1,1,1,2,3,4]) == 0
    assert t.royal([1,1,1,1,1,1]) == 66

def test_is_cell_empty():
    t.update_table("1", "DOWN", 5)
    assert t.is_cell_empty("1", "DOWN") == False
    assert t.is_cell_empty("2", "DOWN") == True

def test_is_table_full():
    assert t.is_table_full() == False
    assert full_table.is_table_full() == True

def test_is_cell_writable():
    t.update_table("1", "DOWN", 5)
    assert t.is_cell_writable("1", "DOWN") == False
    assert t.is_cell_writable("2", "DOWN") == True
    assert t.is_cell_writable("ROYAL", "DOWN") == False
    assert t.is_cell_writable("ROYAL", "UP") == True
    assert t.is_cell_writable("YAMB", "UP") == False
    t.update_table("ROYAL", "UP", 66)
    assert t.is_cell_writable("YAMB", "UP") == True
    assert t.is_cell_writable("MIN", "MIDDLE") == True
    assert t.is_cell_writable("MIN", "UP") == False
    assert t.is_cell_writable("MIN", "RANDOM 1") == True
    assert t.is_cell_writable("MAX", "MIDDLE") == True
    assert t.is_cell_writable("6", "MIDDLE") == False
    assert t.is_cell_writable("KENTA", "MIDDLE") == False
    t.update_table("MAX", "MIDDLE", 31)
    assert t.is_cell_writable("6", "MIDDLE") == True
    assert t.is_cell_writable("KENTA", "MIDDLE") == False
    t.update_table("MIN", "MIDDLE", 9)
    assert t.is_cell_writable("KENTA", "MIDDLE") == True

def test_sum_first_6_rows():
    t.update_table("1", "DOWN", 5)
    assert t.sum_first_6_rows() == 5
    assert full_table.sum_first_6_rows() == 527

def test_sum_max_min():
    assert t.sum_max_min() == 0
    assert full_table.sum_max_min() == 617

def test_sum_all():
    t.update_table("1", "DOWN", 5)
    t.update_table("ROYAL", "UP", 66)
    t.update_table("MAX", "MIDDLE", 31)
    t.update_table("MIN", "MIDDLE", 9)
    assert t.sum_all() == 71
    assert full_table.sum_all() == 2544

###################################################
# Testing round
def test_roll_dice():
    result = roll_dice(6)
    assert len(result) == 6
    assert result[0] <= 6
    outsiders = False
    for n in result:
        if 1 > n > 6:
            outsiders = True
            break
    assert not outsiders

def test_count_occurrences():
    assert count_occurrences([1,1,2,2,2,3]) == {1: 2, 2: 3, 3: 1}
    assert count_occurrences([6,6,6,6,6,6]) == {6: 6}

def test_is_valid():
    assert is_valid("6,6,6,6,6,6", [1,2,3,4,5,6]) == False
    assert is_valid("6,6,6,6,6,6", [6,6,6,6,6,6]) == True
    assert is_valid("h", [6,6,6,6,6,6]) == False