# GAME OF DICES
#### Video Demo:  <[URL HERE](https://youtu.be/wv0pOOmegw8)>

<span style="color:orange; font-size:24px;">**Welcome to the game of dices!**</span><br><span style="color:pink; font-size:16px;">**(In Slovenia called 'kocke')**</span>

The game is very similar to the game [Yahtzee](https://en.wikipedia.org/wiki/Yahtzee), with one of the biggest differences being the number of dices (6 instead of 5).

It is based on probability and luck but also strategy and experiences.

<!-- ![Dice](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/2-Dice-Icon.svg/1200px-2-Dice-Icon.svg.png) -->
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/2-Dice-Icon.svg/1200px-2-Dice-Icon.svg.png" width="200" height="200">

## Game objective
The objective is to score points, which you gain by rolling six dices and try to make certain combinations to fill the table.

|       | DOWN | UP | RANDOM 1 | RANDOM 2 | CALL | MIDDLE |
|-------|------|----|----------|----------|------|--------|
| **1** |      |    |          |          |      |        |
| **2** |      |    |          |          |      |        |
| **3** |      |    |          |          |      |        |
| **4** |      |    |          |          |      |        |
| **5** |      |    |          |          |      |        |
| **6** |      |    |          |          |      |        |
| **MAX**|      |    |          |          |      |        |
| **MIN**|      |    |          |          |      |        |
| **KENTA** |  |    |          |          |      |        |
| **FULL** |   |    |          |          |      |        |
| **POKER** |  |    |          |          |      |        |
| **YAMB** |   |    |          |          |      |        |
| **ROYAL**|  |    |          |          |      |        |


<span style="color:green; font-size:16px;">**The winner is the player who scores _the most_ points!**</span>

## Rules
<span style="color; font-size:16px;">***As of now, the game is written for 2 players.***</span>

Dices can be rolled up to three times in a turn to try to make various scoring combinations.
After the first roll the player can save any dice they want and re-roll the other dice.
This procedure is repeated after the second roll. The player has complete choice as to which dice to roll. It is possible to re-roll dices that were or were not rolled before.

A game consists of 13 x 6 rounds (one for each cell in a table). After each round, the player chooses which cell he/she will fill in that round. Once a specific cell has been filled in the game, it cannot be changed.

The scoring categories have varying point values, some of which are fixed values (for example the value of 'kenta' or scale is always either 0 or 61), and others for which the score depends on the value of the dice.

### <span style="color: pink; font-size:16px;">**How to calculate scores for each cell**</span>
#### 1. Rows 1 - 6
Sum up all the dices with number that is the same as row number. If there are none, your score in this cell is zero. _Example: [1,1,1,2,3,4] in row 1 would be 3 (because 3 x 1 = 3)._

**If the sum off cells 1-6 in each column is bigger then or equal 60, you add 30 to the score of that column.**

#### 2. Minimum ('MIN') and Maximum ('MAX')
Sum up the values of all the dices. Your objective is to get the lowest score (in 'MIN') and the highest score (in 'MAX').

**In each column you substract Maximum - Minimum and multiply by the number in cell 1.**

#### 3. Kenta
If the values of your 6 dices are 1,2,3,4,5,6 (in any specific order) you get 61. If any value is missing you get 0 points.
#### 4. Full
You need 3 dices with the same number and 2 dices with different same number. If you succeed you sum up this 5 dices and add 30 to the score, else you get 0.
#### 5. Poker
You need 4 dices with the same number. If you succeed you sum up this 4 dices and add 40 to the score, else you get 0.
#### 6. Yamb
You need 5 dices with the same number. If you succeed you sum up this 5 dices and add 50 to the score, else you get 0.
#### 7. Royal
You need 6 dices with the same number. If you succeed you sum up this 6 dices and add 60 to the score, else you get 0.

### <span style="color: pink; font-size:16px;">**Rules based on columns**</span>
Each column has a special rule to follow.

#### 1., 2. DOWN and UP
In the first one ('DOWN') you can only fill the cells from top to bottom (meaning you can't fill the cell if the previous one is empty) and in the second one ('UP') it is the opposite - you can only fill the cell if the next one is already full, so you go from bottom to top.

#### 3., 4. RANDOM 1 and RANDOM 2
In this two column you can fill the cells in which ever order you want.

#### 5. CALL
You can only fill this column if after the first roll you decide to 'call'. _So for example if you roll 3 x 6 in the first roll, you can call the row '6' in column 'CALL' and then even if after the last roll you get 6 x 6 and would like to fill the 'ROYAL' row, you can only fill the one you called ('6' in this case)._

#### 6. MIDDLE
You have to start filling this column from the 'middle', meaning from row 'MAX' going up and from row 'MIN' going down.

### <span style="color: pink; font-size:16px;">**End of the game**</span>
At the end of the game you sum up all the scores in cells 1-6 (optionally add 30 as per the rules) -> **Result 1**, then you substract Maximum - Minimum and multiply by the number in cell 1 -> **Result 2**, and then you sum up all the scores in cells 9-13 -> **Result 3**.

The result of each column is the sum of the Result 1, Result 2 and Result 3.

The final step is to sum up the scores of every column.

## USAGE
The game is written over 5 python files, with 2 '.txt' files with instructions ('instructions.txt' for the instructions at the beginning of the game and 'intermediate_instructions.txt' for help during the game) and 2 '.csv' files with tables for testing the functions.

The file 'dices.py' consists of the main structure of the game (main function):
1. Game setup
2. Play
3. Count results and display winner

It also has the functionality of each round (which in the future I will move into different seperate file) and the function to calculate and display the winner (which is then called in the main).

The file 'first_part.py' contains the 'game setup', meaning functionality welcome the players, get their names, optionally show instructions, set up the tables, choose who will start the game, ...

Files 'table.py' and 'player.py' contain classes defining all functionality of the players and their playing tables. So in the file 'table' you can find all the methods to calculate cell results, update table and so on.

I also have a seperate file called 'test_project.py' which consist of the tests that I have so far written to test the game functionality.

The last file is 'UI.py' which stands for user interface and contains functions to change the text output color based on the text content.
