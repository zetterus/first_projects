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
        J = random.randint(1 - self.f_width[0],
                           board.cols - 1 - self.f_width[1] + self.f_width[2])  # -1 to consider a right border
        print("spawn", self.i, J, self.form, self.f_width[0], self.f_width[1], self.f_width[2])
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
        for jj in range(self.f_width[0], self.f_width[1] - self.f_width[2]):
            for ii in range(self.f_height[0], self.f_height[1] - self.f_height[2]):
                if board.board[self.i + ii][self.j - 1 + jj] + self.form[ii][jj] == 2:
                    print("l_coll", self.i, self.j, self.f_width[0], self.f_height[1], self.f_height[2], ii)
                    return False

        return True

    # right
    def can_move_right(self):
        for jj in range(self.f_width[0], self.f_width[1] - self.f_width[2]):
            for ii in range(self.f_height[0], self.f_height[1] - self.f_height[2]):
                if board.board[self.i + ii][self.j + 1 + jj] + self.form[ii][jj] == 2:
                    print("r_coll", self.i, self.j, self.f_width[1], self.f_width[2], ii, jj)
                    return False

        return True

    # bottom
    def can_move_down(self):
        for ii in range(self.f_height[0], self.f_height[1] - self.f_height[2]):
            for jj in range(self.f_width[0], self.f_width[1] - self.f_width[2]):
                # print("b_coll", self.i, self.j, ii, jj)
                if board.board[self.i + 1 + ii][self.j + jj] + self.form[ii][jj] == 2:
                    print("b_coll", self.i, self.j, ii, jj)
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
        self.score = 0

    def draw_figure(self, fig):
        for i in range(fig.f_height[1]):
            for j in range(fig.f_width[1]):  # Rectangle (startx, starty, width, heigth)
                if fig.form[i][j]:
                    pygame.draw.rect(screen, BLUE, (
                        (fig.j + j) * (self.square_size + self.line_thickness) + self.line_thickness,
                        (fig.i + i - 2) * (self.square_size + self.line_thickness) + self.line_thickness,
                        self.square_size,
                        self.square_size))

    def full_row(self, last_row):  # finish it!
        score_add = 0
        for i in range(last_row, last_row - 5, -1):  # 4 - longest figure
            if all(board.board[i]):
                print("full_row_if", i)
                score_add += last_row - i + 1
            elif score_add:
                print("full_row_elif", i)
                new_upper_rows = [board.board[0] for _ in range(last_row - i)]
                new_middle_rows = board.board[0:i + 1]
                old_bottom_rows = board.board[last_row + 1:]
                board.board = new_upper_rows + new_middle_rows + old_bottom_rows
                self.score += score_add
                break

    def filled(self):
        return 1 in self.board[3][1:11]

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
        self.draw_figure(figure)

        # Draw filled board part
        for i in range(board.rows):
            for j in range(board.cols):
                if board.board[i + 2][j]:
                    pygame.draw.rect(screen, BLUE, (
                        j * (self.square_size + self.line_thickness) + self.line_thickness,
                        i * (self.square_size + self.line_thickness) + self.line_thickness,
                        self.square_size,
                        self.square_size))

        # Draw board borders
        # left border
        pygame.draw.rect(screen, DARK_SLATE_GREY,
                         (0, 0, self.square_size + self.line_thickness,
                          self.height))  # Rectangle (startx, starty, width, heigth)
        # right border
        pygame.draw.rect(screen, DARK_SLATE_GREY,
                         (
                             self.width - self.square_size - self.line_thickness, 0,
                             (self.square_size + self.line_thickness) * self.cols // 2,
                             self.height))
        # upper border
        pygame.draw.rect(screen, DARK_SLATE_GREY, (0, 0, self.width, self.square_size + self.line_thickness))
        # bottom border
        pygame.draw.rect(screen, DARK_SLATE_GREY,
                         (0, self.height - self.square_size - self.line_thickness, self.width,
                          self.square_size + self.line_thickness))

        # Draw score and next figure
        # score text
        font = pygame.font.SysFont("arial.ttf", 48)
        score_text = font.render("SCORE:", True, BLACK, DARK_SLATE_GREY)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 2),
                                  self.line_thickness + (self.square_size + self.line_thickness) * 2)
        screen.blit(score_text, score_text_rect)
        # score int
        font = pygame.font.SysFont("arial.ttf", 48)
        score_int = font.render(f"{self.score}", True, BLACK, DARK_SLATE_GREY)
        score_int_rect = score_int.get_rect()
        score_int_rect.topright = (
            self.line_thickness * 2 + (self.square_size + self.line_thickness) * (self.cols + 3.5),
            self.line_thickness + (self.square_size + self.line_thickness) * 3)
        screen.blit(score_int, score_int_rect)
        # next figure text
        font = pygame.font.SysFont("arial.ttf", 36)
        next_figure_text = font.render("NEXT FIGURE", True, BLACK, DARK_SLATE_GREY)
        next_figure_text_rect = next_figure_text.get_rect()
        next_figure_text_rect.center = (
            self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 2),
            self.line_thickness + (self.square_size + self.line_thickness) * 5)
        screen.blit(next_figure_text, next_figure_text_rect)
        # next figure form
        next_figure.i = 8
        next_figure.j = self.cols
        self.draw_figure(next_figure)

        # Draw info lines
        # Draw vertical lines
        # left
        pygame.draw.line(screen, GRAY18,
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 1),
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 21),
                         self.line_thickness)
        # right
        pygame.draw.line(screen, GRAY18,
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 1),
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 21),
                         self.line_thickness)

        # upper 0
        pygame.draw.line(screen, DARK_GREY,
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 1),
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 1), self.line_thickness)

        # upper 1
        pygame.draw.line(screen, DARK_GREY,
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 4),
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 4), self.line_thickness)

        # upper 2
        pygame.draw.line(screen, DARK_GREY,
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 11),
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 11), self.line_thickness)


        # bottom
        pygame.draw.line(screen, DARK_GREY,
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 21),
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 21), self.line_thickness)

        # Draw the frame
        pygame.display.flip()


# initializing objects
board = Board()
figure = Figure()
next_figure = Figure()
figure.spawn()

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode(((board.width) * 1.5 - (board.square_size + board.line_thickness), board.height))

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
                    board.full_row(figure.i + figure.f_height[1] - figure.f_height[2] - 1)
                    figure = next_figure
                    figure.spawn()
                    next_figure = Figure()
            if event.key == ROTATE and figure.can_rotate():
                figure.rotate()
            if event.key == DROP:
                while figure.can_move_down():
                    figure.move(1, 0)
                else:
                    figure.fix_at_board()
                    board.full_row(figure.i + figure.f_height[1] - figure.f_height[2] - 1)
                    figure = next_figure
                    figure.spawn()
                    next_figure = Figure()
            if event.key == pygame.K_i:
                print(figure.i, figure.j)

    # figures moves
    # Движение фигуры вниз
    current_time = pygame.time.get_ticks()
    delta_time = current_time - last_move_down_time
    if delta_time >= MOVE_DOWN_DELAY and figure.can_move_down():  # if tick passed and figure can move down - move it down
        figure.move(1, 0)
        last_move_down_time = current_time
    if delta_time >= MOVE_DOWN_DELAY * 2 and not figure.can_move_down():  # if two ticks passed and figure can't move down fix it to the board!
        figure.fix_at_board()
        board.full_row(figure.i + figure.f_height[1] - figure.f_height[2] - 1)
        figure = next_figure
        figure.spawn()
        next_figure = Figure()
        last_move_down_time = current_time

    # filling reach top
    if board.filled():
        GAME_OVER = True

    # win conditions
    if board.score >= 10000:
        GAME_OVER = True

    # frame draw
    board.draw(figure)

# Quit pygame
pygame.quit()
print(figure.i, figure.j, figure.form)

for row in board.board:
    print(row)
