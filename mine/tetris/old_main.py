# modules
import pygame
import random

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
GAME_OVER = False

# keybinds
ROTATE = pygame.K_UP
DOWN = pygame.K_DOWN
RIGHT = pygame.K_RIGHT
LEFT = pygame.K_LEFT
DROP = pygame.K_SPACE

# Define colors
WHITE = (255, 255, 255)
BLACK = (16, 16, 16)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
GRAY18 = (46, 46, 46)
DARK_GREY = (32, 32, 32)
DARK_SLATE_GREY = (47, 79, 79)

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Tetris")
icon = pygame.image.load("tetris.png")
pygame.display.set_icon(icon)

# starting screen including "start", "options", "records", "exit"

# figures setup
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
                "T": [[0, 1, 0],
                      [1, 1, 1],
                      [0, 0, 0]],
                "Z": [[0, 0, 0],
                      [1, 1, 0],
                      [0, 1, 1]]}


# functions section
def draw_board(board):
    # Fill the background
    screen.fill(GRAY18)
    # Draw vertical lines
    for i in range(0, WIDTH, SQUARE_SIZE + LINE_THICKNESS):
        pygame.draw.line(screen, DARK_GREY, (i, 0), (i, HEIGHT), LINE_THICKNESS)
    # Draw horizontal lines
    for j in range(0, HEIGHT, SQUARE_SIZE + LINE_THICKNESS):
        pygame.draw.line(screen, DARK_GREY, (0, j), (WIDTH, j), LINE_THICKNESS)

    # Draw filled
    for i in range(len(current_figure)):
        for j in range(len(current_figure[0])):
            if current_figure[i][j]:
                pygame.draw.rect(screen, BLUE, (
                    (CUR_COL + 1) * (SQUARE_SIZE + LINE_THICKNESS) + LINE_THICKNESS,
                    (CUR_ROW - 2) * (SQUARE_SIZE + LINE_THICKNESS) + LINE_THICKNESS, SQUARE_SIZE, SQUARE_SIZE))

    # Draw borders
    pygame.draw.rect(screen, DARK_SLATE_GREY,
                     (0, 0, SQUARE_SIZE + LINE_THICKNESS, HEIGHT))  # Rectangle (startx, starty, width, heigth)
    pygame.draw.rect(screen, DARK_SLATE_GREY,
                     (WIDTH - SQUARE_SIZE - LINE_THICKNESS, 0, SQUARE_SIZE + LINE_THICKNESS, HEIGHT))
    pygame.draw.rect(screen, DARK_SLATE_GREY, (0, 0, WIDTH, SQUARE_SIZE + LINE_THICKNESS))
    pygame.draw.rect(screen, DARK_SLATE_GREY,
                     (0, HEIGHT - SQUARE_SIZE - LINE_THICKNESS, WIDTH, SQUARE_SIZE + LINE_THICKNESS))

    # Draw info and scoreboard

    # Draw the frame
    pygame.display.flip()


def pick_random_figure():
    return FIGURES_LIST[random.choice(("I", "J", "L", "O", "S", "T", "Z"))]


def figure_spawn(figure):
    global CUR_COL
    global CUR_ROW
    CUR_COL = random.randint(1, COL_COUNT - 2 - len(current_figure[0]))
    CUR_ROW = 4 - len(figure)
    # for i in range(len(figure)):
    #     if any(d != 0 for d in figure[len(figure) - 1 - i]):
    #         CUR_ROW = 3 - len(figure)  # 3 - filled height
    #         break
    figure_move(figure, CUR_ROW, CUR_COL)
    return CUR_ROW, CUR_COL


def figure_move(figure, row, col, dirx=0, diry=0):
    for i in range(len(figure)):
        for j in range(len(figure[0])):
            board[row + i][col + j] = 0
    global CUR_COL
    global CUR_ROW
    CUR_COL = col + dirx
    CUR_ROW = row + diry
    # figures collision with walls
    if CUR_COL < 0:
        CUR_COL = 0
    if CUR_COL > COL_COUNT - len(current_figure[0]):
        CUR_COL = COL_COUNT - len(current_figure[0])
    print(CUR_ROW, CUR_COL)
    temp = [[0] * len(figure) for _ in range(len(figure))]
    for i in range(len(figure)):
        for j in range(len(figure[0])):
            temp[i][j] = board[row + i + diry][col + j + dirx] = figure[i][j]
    for row in temp:
        print(row)


def figure_rotate(figure):
    side_size = len(figure)
    temp = [[0] * side_size for _ in range(side_size)]
    for i in range(side_size):
        for j in range(side_size):
            temp[j][(side_size - 1) - i] = figure[i][j]
    global current_figure
    current_figure = temp  # is it legal?
    # return temp


# some technical stuff
current_figure = pick_random_figure()
for _ in range(random.randint(0, 4)):
    figure_rotate(current_figure)
figure_spawn(current_figure)

# main loop
while not GAME_OVER:

    # here would be main game logic
    # keypress

    # detecting keypress
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True

        # keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == LEFT:
                figure_move(current_figure, CUR_ROW, CUR_COL, -1, 0)
            if event.key == RIGHT:
                figure_move(current_figure, CUR_ROW, CUR_COL, 1, 0)
            if event.key == DOWN:
                figure_move(current_figure, CUR_ROW, CUR_COL, 0, 1)
            if event.key == ROTATE:
                figure_rotate(current_figure)
            if event.key == DROP:
                figure_rotate(current_figure)

            # figures moves
            # CUR_ROW, CUR_COL = figure_spawn(current_figure)
            # Таймер для движения фигуры вниз
            MOVE_DOWN_DELAY = 1000  # Задержка в миллисекундах
            last_move_down_time = pygame.time.get_ticks()

            # Движение фигуры вниз
            current_time = pygame.time.get_ticks()
            if current_time - last_move_down_time >= MOVE_DOWN_DELAY:
                figure_move(current_figure, CUR_ROW, CUR_COL, 0, 1)
                last_move_down_time = current_time

    # figures appears

    # figures reach bottom

    draw_board(board)

# Quit pygame
pygame.quit()
