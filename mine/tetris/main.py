import pygame
import random

# game over condition
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


# figure class
class Figure:
    # figures forma list
    FORMAS_LIST = {"I": [[0, 1, 0, 0],
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

    def __init__(self):
        self.i = None
        self.j = None
        self.form = self.__class__.FORMAS_LIST[random.choice(("I", "J", "L", "O", "S", "T", "Z"))]
        self.f_width = len(self.form[0])
        self.f_height = len(self.form)
        for _ in range(4):
            self.rotate()

    def spawn(self):  # dunno why separate, not in init, but o want so
        self.i = 3-self.f_height
        for row in reversed(self.form):
            if sum(row):
                break
            else:
                self.i += 1

        self.j = random.randint(1, board.cols - self.f_width)

    def rotate(self):
        side_size = len(self.form)
        temp = [[0] * side_size for _ in range(side_size)]
        for i in range(side_size):
            for j in range(side_size):
                temp[j][(side_size - 1) - i] = self.form[i][j]
        self.form = temp
        # return temp ???

    def move(self, diri=0, dirj=0):
        self.i += diri
        self.j += dirj
        if self.j < 0:
            self.j = 0
        if self.j > board.cols - self.f_width:
            self.j = board.cols - self.f_width


# board class
class Board:
    def __init__(self, rows=20, cols=10, square_size=40, line_thickness=2):
        self.board = [[0] * cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols
        self.square_size = square_size
        self.line_thickness = line_thickness
        self.width = cols * (square_size + line_thickness) + square_size * 2 + line_thickness * 3
        self.height = rows * (square_size + line_thickness) + square_size * 2 + line_thickness * 3

    def draw(self, fig):
        # Fill the background
        screen.fill(GRAY18)
        # Draw vertical lines
        for i in range(0, self.width, self.square_size + self.line_thickness):
            pygame.draw.line(screen, DARK_GREY, (i, 0), (i, self.height), self.line_thickness)
        # Draw horizontal lines
        for j in range(0, self.height, self.square_size + self.line_thickness):
            pygame.draw.line(screen, DARK_GREY, (0, j), (self.width, j), self.line_thickness)

        # Draw figures
        for i in range(fig.f_height):
            for j in range(fig.f_width):  # Rectangle (startx, starty, width, heigth)
                if fig.form[i][j]:
                    pygame.draw.rect(screen, BLUE, (
                        (fig.j + j + 1) * (self.square_size + self.line_thickness) + self.line_thickness,
                        (fig.i + i - 1) * (self.square_size + self.line_thickness) + self.line_thickness,
                        self.square_size,
                        self.square_size))

        # Draw borders
        pygame.draw.rect(screen, DARK_SLATE_GREY,
                         (0, 0, self.square_size + self.line_thickness,
                          self.height))  # Rectangle (startx, starty, width, heigth)
        pygame.draw.rect(screen, DARK_SLATE_GREY,
                         (
                             self.width - self.square_size - self.line_thickness, 0,
                             self.square_size + self.line_thickness,
                             self.height))
        pygame.draw.rect(screen, DARK_SLATE_GREY, (0, 0, self.width, self.square_size + self.line_thickness))
        pygame.draw.rect(screen, DARK_SLATE_GREY,
                         (0, self.height - self.square_size - self.line_thickness, self.width,
                          self.square_size + self.line_thickness))

        # Draw info and scoreboard

        # Draw the frame
        pygame.display.flip()


# initializing objects
board = Board()
figure = Figure()
figure.spawn()

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((board.width, board.height))

# Title and Icon
pygame.display.set_caption("Tetris")
icon = pygame.image.load("tetris.png")
pygame.display.set_icon(icon)

# starting screen including "start", "options", "records", "exit"


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
                figure.move(0, -1)
            if event.key == RIGHT:
                figure.move(0, 1)
            if event.key == DOWN:
                figure.move(1, 0)
            if event.key == ROTATE:
                figure.rotate()
            # if event.key == DROP:
            #     figure_rotate(current_figure)

            # # figures moves
            # # CUR_ROW, CUR_COL = figure_spawn(current_figure)
            # # Таймер для движения фигуры вниз
            # MOVE_DOWN_DELAY = 1000  # Задержка в миллисекундах
            # last_move_down_time = pygame.time.get_ticks()
            #
            # # Движение фигуры вниз
            # current_time = pygame.time.get_ticks()
            # if current_time - last_move_down_time >= MOVE_DOWN_DELAY:
            #     figure_move(current_figure, CUR_ROW, CUR_COL, 0, 1)
            #     last_move_down_time = current_time

    # figures appears

    # figures reach bottom

    # frame draw
    # figure.i = 5
    # figure.j = 4
    board.draw(figure)
    print(figure.i, figure.j, figure.form)
    # for row in board.board:
    #     print(row)

# Quit pygame
pygame.quit()
