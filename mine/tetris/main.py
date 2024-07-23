# modules
import pygame as PG
import random as R
import time

# settings
# resolution, colors, mb keybinds
ROW_COUNT = 20
COL_COUNT = 10
SQUARE_SIZE = 40
LINE_THICKNESS = 2
WIDTH = COL_COUNT * (SQUARE_SIZE + LINE_THICKNESS) + SQUARE_SIZE * 2 + LINE_THICKNESS * 3
HEIGHT = ROW_COUNT * (SQUARE_SIZE + LINE_THICKNESS) + SQUARE_SIZE * 2 + LINE_THICKNESS * 3

# system settings
board = [[0] * COL_COUNT for _ in range(ROW_COUNT + 3)]
tick = 1  # sec
GAME_OVER = False

# keybinds
UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"
space = "space"

# Define colors
WHITE = (255, 255, 255)
BLACK = (16, 16, 16)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY18 = (46, 46, 46)
DARK_GREY = (32, 32, 32)
DARK_SLATE_GREY = (47, 79, 79)

# Initialize the PG
PG.init()

# Create the screen
screen = PG.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
PG.display.set_caption("Tetris")
icon = PG.image.load("tetris.png")
PG.display.set_icon(icon)

# starting screen including "start", "options", "records", "exit"

# figures list
FIGURES_LIST = {"I": [[0, 1, 0, 0],
                      [0, 1, 0, 0],
                      [0, 1, 0, 0],
                      [0, 1, 0, 0]],
                "J": [[1, 0, 0],
                      [1, 0, 0],
                      [1, 1, 0]],
                "L": [[0, 0, 1],
                      [0, 0, 1],
                      [0, 1, 1]],
                "O": [[1, 1],
                      [1, 1]],
                "S": [[0, 0, 0],
                      [0, 1, 1],
                      [1, 1, 0]],
                "T": [[0, 0, 0],
                      [0, 1, 0],
                      [1, 1, 1]],
                "Z": [[0, 0, 0],
                      [1, 1, 0],
                      [0, 1, 1]]}


# functions section
def draw_board(board):
    # Fill the background
    screen.fill(GRAY18)
    # Draw vertical lines
    for i in range(0, WIDTH, SQUARE_SIZE + LINE_THICKNESS):
        PG.draw.line(screen, DARK_GREY, (i, 0), (i, HEIGHT), LINE_THICKNESS)
    # Draw horizontal lines
    for j in range(0, HEIGHT, SQUARE_SIZE + LINE_THICKNESS):
        PG.draw.line(screen, DARK_GREY, (0, j), (WIDTH, j), LINE_THICKNESS)
    # Draw borders
    PG.draw.rect(screen, DARK_SLATE_GREY, (0, 0, SQUARE_SIZE, HEIGHT))  # Rectangle (startx, starty, width, heigth)
    PG.draw.rect(screen, DARK_SLATE_GREY, (WIDTH - SQUARE_SIZE, 0, SQUARE_SIZE, HEIGHT))
    PG.draw.rect(screen, DARK_SLATE_GREY, (0, 0, WIDTH, SQUARE_SIZE))
    PG.draw.rect(screen, DARK_SLATE_GREY, (0, HEIGHT - SQUARE_SIZE, WIDTH, SQUARE_SIZE))

    # Draw info and scoreboard

    # Draw filled
    for i in range(ROW_COUNT):
        for j in range(COL_COUNT):
            if board[i][j]:
                PG.draw.rect(screen, BLUE, (
                    j * (SQUARE_SIZE + LINE_THICKNESS) + LINE_THICKNESS,
                    i * (SQUARE_SIZE + LINE_THICKNESS) + LINE_THICKNESS, SQUARE_SIZE, SQUARE_SIZE))

    # Draw the frame
    PG.display.flip()


def figure_fall(figure, row, col):
    for i in range(len(figure)):
        for j in range(figure[0]):
            board[row + i][col + j] = 0
    for i in range(len(figure)):
        for j in range(figure[0]):
            board[row + i + 1][col + j] = figure[i][j]


def figure_rotate(figure):
    side_size = len(figure)
    temp = [[0] * side_size for _ in range(side_size)]
    for i in range(side_size):
        for j in range(side_size):
            temp[j][(side_size - 1) - i] = figure[i][j]
    # figure = temp  # is it legal?
    return temp


# figures moove in main loop
# figures collision
while not GAME_OVER:
    for event in PG.event.get():
        if event.type == PG.QUIT:
            GAME_OVER = True

    # this would be main game logic


    draw_board(board)

# Quit PG
PG.quit()
