# modules
import time
from time import sleep
import keyboard  # if keyboard.read_key() == "a":

# settings, resolution, colors, mb keybinds
ROW_COUNT = 20
COL_COUNT = 10

# keybinds
UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"
space = "space"

# system settings
board = [["[.]"] * COL_COUNT for _ in range(ROW_COUNT)]
GAME_OVER = False

# starting screen including "start", "options", "records", "exit"

# figures list
FIGURES_LIST = {"I": [["[.]", "[X]", "[.]", "[.]"],
                      ["[.]", "[X]", "[.]", "[.]"],
                      ["[.]", "[X]", "[.]", "[.]"],
                      ["[.]", "[X]", "[.]", "[.]"]],
                "J": [["[X]", "[.]", "[.]"],
                      ["[X]", "[.]", "[.]"],
                      ["[X]", "[X]", "[.]"]],
                "L": [["[.]", "[.]", "[X]"],
                      ["[.]", "[.]", "[X]"],
                      ["[.]", "[X]", "[X]"]],
                "O": [["[.]", "[.]", "[.]", "[.]"],
                      ["[.]", "[X]", "[X]", "[.]"],
                      ["[.]", "[X]", "[X]", "[.]"],
                      ["[.]", "[.]", "[.]", "[.]"]],
                "S": [["[.]", "[.]", "[.]"],
                      ["[.]", "[X]", "[X]"],
                      ["[X]", "[X]", "[.]"]],
                "T": [["[.]", "[.]", "[.]"],
                      ["[.]", "[X]", "[.]"],
                      ["[X]", "[X]", "[X]"]],
                "Z": [["[.]", "[.]", "[.]"],
                      ["[X]", "[X]", "[.]"],
                      ["[.]", "[X]", "[X]"]]}


# functions section
def print_board():
    print()
    print()
    print()
    print("[-]" * (COL_COUNT + 2))
    for row in board:
        print("[I]", *row, "[I]", sep="")
    print("[-]" * (COL_COUNT + 2))



def figure_rotate(figure):
    side_size = len(figure)
    temp = [["[.]"] * side_size for _ in range(side_size)]
    for i in range(side_size):
        for j in range(side_size):
            temp[j][(side_size - 1) - i] = figure[i][j]
    # figure = temp  # is it legal?
    return temp


# figures moove in main loop
# figures collision
while not GAME_OVER:
    print_board()
    time.sleep(1)
    if keyboard.read_key() == "q":
        break
