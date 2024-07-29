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
        self.f_width = (self.hitbox()["left"], len(self.form[0]),
                        self.hitbox()["right"])  # -left zero cols, filled cols, right zero cols
        self.f_height = (
            self.hitbox()["up"], len(self.form),
            self.hitbox()["bottom"])  # upper zero rows, filled rows, bottom zero rows
        for _ in range(4):
            self.rotate()

    def hitbox(self):
        left_zero_cols = 0
        for j in range(len(self.form[0])):
            if any(self.form[i][j] for i in range(len(self.form))):
                break
            else:
                left_zero_cols += 1
        right_zero_cols = 0
        for j in range(len(self.form[0]) - 1, 0, -1):
            if any(self.form[i][j] for i in range(len(self.form))):
                break
            else:
                right_zero_cols += 1
        corr_i_up = 0
        for row in self.form:
            if sum(row):
                break
            else:
                corr_i_up += 1
        corr_i_bot = 0
        for row in reversed(self.form):
            if sum(row):
                break
            else:
                corr_i_bot += 1
        return {"left": left_zero_cols, "right": right_zero_cols, "up": corr_i_up, "bottom": corr_i_bot}

    def spawn(self):  # dunno why separate, not in init, but I want so
        self.i = 4 - self.f_height[1] + self.f_height[2]
        J = random.randint(1 - self.f_width[0], board.cols - self.f_width[1] + self.f_width[2])
        print(self.f_width[0], board.cols, self.f_width[1], self.f_width[2])
        self.j = J

    def rotate(self):
        side_size = len(self.form)
        temp = [[0] * side_size for _ in range(side_size)]
        for i in range(side_size):
            for j in range(side_size):
                temp[j][(side_size - 1) - i] = self.form[i][j]
        self.form = temp
        self.f_width = (self.hitbox()["left"], len(self.form[0]),
                        self.hitbox()["right"])  # -left zero cols, filled cols, right zero cols
        self.f_height = (
            self.hitbox()["up"], len(self.form),
            self.hitbox()["bottom"])  # upper zero rows, filled rows, bottom zero rows
        # return temp ???

    def move(self, diri=0, dirj=0):
        self.i += diri
        self.j += dirj

    # Figures collision
    # left
    def can_move_left(self):
        for ii in range(self.f_height[0], self.f_height[1] - self.f_height[2]):
            if board.board[self.i + ii][self.j - 1 + self.f_width[0]] + self.form[ii][0 + self.f_width[0]] == 2:
                print("l_coll", self.i, self.j, self.f_width[0], self.f_height[1], self.f_height[2], ii)
                return False
                break

        return True

    # right
    def can_move_right(self):
        for ii in range(self.f_height[0], self.f_height[1] - self.f_height[2]):
            if (board.board[self.i + ii][self.j + self.f_width[1] - self.f_width[2]] +
                    self.form[ii][-1 - self.f_width[2]] == 2):
                print("r_coll", self.j, self.f_width[1], self.f_width[2], ii)
                return False

        return True

    # bottom
    def can_move_down(self):
        for jj in range(self.f_width[0], self.f_width[1] - self.f_width[2]):
            # print("b_coll", self.i, self.j, self.f_height[1], self.f_height[2], jj, "|", self.f_width[0], self.f_width[1], self.f_width[2])
            if board.board[self.i + self.f_height[1] - self.f_height[2]][self.j + jj] + self.form[-1][jj] == 2:
                print("b_coll", self.i, self.j, self.f_height[1], self.f_height[2], jj, "|", self.f_width[0],
                      self.f_width[1], self.f_width[2])
                return False

        return True

    def can_rotate(self):
        temp = figure.form
        figure.rotate()
        for ii in range(self.f_height[0], self.f_height[1] - self.f_height[2]):
            for jj in range(self.f_width[0], self.f_width[1] - self.f_width[2]):
                if board.board[self.i + ii][self.j + jj] + figure.form[ii][jj] == 2:
                    figure.form = temp
                    return False

        figure.form = temp
        return True

    def fix_at_board(self):
        for ii in range(self.f_height[0], self.f_height[1] - self.f_height[2]):
            for jj in range(self.f_width[0], self.f_width[1] - self.f_width[2]):
                if self.form[ii][jj]:
                    board.board[self.i + ii][self.j + jj] = self.form[ii][jj]


# board class
class Board:
    def __init__(self, rows=20, cols=10, square_size=40, line_thickness=2):
        self.board = [[1] + [0] * cols + [1] if i != rows + 3 else [1] * (cols + 2) for i in range(rows + 4)]
        self.rows = len(self.board) - 2
        self.cols = len(self.board[0])
        self.square_size = square_size
        self.line_thickness = line_thickness
        self.width = self.cols * (self.square_size + self.line_thickness) + self.line_thickness
        self.height = self.rows * (self.square_size + self.line_thickness) + self.line_thickness

    def draw(self, fig):
        # Fill the background
        screen.fill(GRAY18)
        # Draw vertical lines
        for j in range(0, self.width, self.square_size + self.line_thickness):
            pygame.draw.line(screen, DARK_GREY, (j, 0), (j, self.height), self.line_thickness)
        # Draw horizontal lines
        for i in range(0, self.height, self.square_size + self.line_thickness):
            pygame.draw.line(screen, DARK_GREY, (0, i), (self.width, i), self.line_thickness)

        # Draw figure
        for i in range(fig.f_height[1]):
            for j in range(fig.f_width[1]):  # Rectangle (startx, starty, width, heigth)
                if fig.form[i][j]:
                    pygame.draw.rect(screen, BLUE, (
                        (fig.j + j) * (self.square_size + self.line_thickness) + self.line_thickness,
                        (fig.i + i) * (self.square_size + self.line_thickness) + self.line_thickness,
                        self.square_size,
                        self.square_size))

        # Draw filled board part
        for i in range(board.rows):
            for j in range(board.cols):
                if board.board[i+2][j]:
                    pygame.draw.rect(screen, BLUE, (
                        j * (self.square_size + self.line_thickness) + self.line_thickness,
                        i * (self.square_size + self.line_thickness) + self.line_thickness,
                        self.square_size,
                        self.square_size))

        # # Draw borders
        # pygame.draw.rect(screen, DARK_SLATE_GREY,
        #                  (0, 0, self.square_size + self.line_thickness,
        #                   self.height))  # Rectangle (startx, starty, width, heigth)
        # pygame.draw.rect(screen, DARK_SLATE_GREY,
        #                  (
        #                      self.width - self.square_size - self.line_thickness, 0,
        #                      self.square_size + self.line_thickness,
        #                      self.height))
        # pygame.draw.rect(screen, DARK_SLATE_GREY, (0, 0, self.width, self.square_size + self.line_thickness))
        # pygame.draw.rect(screen, DARK_SLATE_GREY,
        #                  (0, self.height - self.square_size - self.line_thickness, self.width,
        #                   self.square_size + self.line_thickness))

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

# some settings and constants
# Время последнего перемещения фигуры вниз
last_move_down_time = pygame.time.get_ticks()

# Задержка между перемещениями фигуры вниз (в миллисекундах)
MOVE_DOWN_DELAY = 1000

while not GAME_OVER:

    # here would be main game logic
    # keypress

    # detecting keypress
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True

            # keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == LEFT and figure.can_move_left():
                figure.move(0, -1)
            if event.key == RIGHT and figure.can_move_right():
                figure.move(0, 1)
            if event.key == DOWN:
                if figure.can_move_down():
                    figure.move(1, 0)
                else:
                    figure.fix_at_board()
                    figure.spawn()
            if event.key == ROTATE and figure.can_rotate():
                figure.rotate()
            # if event.key == DROP:
            #     figure_rotate(current_figure)
            if event.key == pygame.K_i:
                print(figure.i, figure.j)

    # figures moves
    # Движение фигуры вниз
    current_time = pygame.time.get_ticks()
    if current_time - last_move_down_time >= MOVE_DOWN_DELAY:
        if figure.can_move_down():
            figure.move(1, 0)
        else:
            figure.fix_at_board()
            figure.spawn()
        last_move_down_time = current_time
        # print(figure.i)

    # # figures reach bottom
    result = figure.can_move_down()
    if not result:
        print("can move down", result)
        figure.fix_at_board()
        figure = Figure()
        figure.spawn()  # figures appears

    # # figures walls collision
    # else:
    #     figure.can_move_side()

    # frame draw
    board.draw(figure)

# Quit pygame
pygame.quit()
print(figure.i, figure.j, figure.form)

for row in board.board:
    print(row)
