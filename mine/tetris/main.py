import pygame
import random
import pickle


# starting screen including "start", "options", "records", "exit"
class Menu():
    def __init__(self):
        # game over condition
        self.GAME_OVER = False
        # keybindings
        self.ROTATE = pygame.K_UP
        self.DOWN = pygame.K_DOWN
        self.RIGHT = pygame.K_RIGHT
        self.LEFT = pygame.K_LEFT
        self.DROP = pygame.K_SPACE
        self.EXIT = pygame.K_ESCAPE

        # Define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (16, 16, 16)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 100, 255)
        self.GRAY18 = (46, 46, 46)
        self.DARK_GREY = (32, 32, 32)
        self.DARK_SLATE_GREY = (47, 79, 79)

        # delay between move down time
        self.MOVE_DOWN_DELAY = 1000
        # last move down time
        self.last_move_down_time = pygame.time.get_ticks()

        # highscores
        # implement it with pickle to disable editing as text?
        try:
            with open("highscores.pkl", "rb") as file:
                self.highscores = pickle.load(file)
        except:
            self.highscores = {}

    def draw_menu(self):
        # Fill the background
        screen.fill(menu.DARK_SLATE_GREY)

        # menu text
        # start text
        start_font = pygame.font.SysFont("arial.ttf", 64)
        start_text = start_font.render("START", True, menu.BLACK, menu.DARK_SLATE_GREY)
        start_text_rect = start_text.get_rect()
        start_text_rect.center = (
            board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 / 4),
            board.line_thickness + (board.square_size + board.line_thickness) * 8)
        screen.blit(start_text, start_text_rect)

        # options text
        options_font = pygame.font.SysFont("arial.ttf", 64)
        options_text = options_font.render("OPTIONS", True, menu.BLACK, menu.DARK_SLATE_GREY)
        options_text_rect = options_text.get_rect()
        options_text_rect.center = (
            board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 / 4),
            board.line_thickness + (board.square_size + board.line_thickness) * 10)
        screen.blit(options_text, options_text_rect)

        # exit text
        exit_font = pygame.font.SysFont("arial.ttf", 64)
        exit_text = exit_font.render("EXIT", True, menu.BLACK, menu.DARK_SLATE_GREY)
        exit_text_rect = exit_text.get_rect()
        exit_text_rect.center = (
            board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 / 4),
            board.line_thickness + (board.square_size + board.line_thickness) * 12)
        screen.blit(exit_text, exit_text_rect)

        # draw highscores text
        highscores_font = pygame.font.SysFont("arial.ttf", 48)
        highscores_text = highscores_font.render("HIGHSCORES:", True, menu.BLACK, menu.DARK_SLATE_GREY)
        highscores_text_rect = highscores_text.get_rect()
        highscores_text_rect.topleft = (
            board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 * 0.55),
            board.line_thickness + (board.square_size + board.line_thickness) * 2)
        screen.blit(highscores_text, highscores_text_rect)

        # draw champs list
        if self.highscores:
            for place, champ in enumerate(self.highscores.items()):
                champ_font = pygame.font.SysFont("arial.ttf", 32)
                champs_text = champ_font.render(F"{place}. {champ[0]}: {champ[1]}", True, menu.BLACK, menu.DARK_SLATE_GREY)
                champs_text_rect = champs_text.get_rect()
                champs_text_rect.topleft = (
                    board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 * 0.55),
                    board.line_thickness + (board.square_size + board.line_thickness) * (3 + place))
                screen.blit(champs_text, champs_text_rect)
        else:
            no_champ_font = pygame.font.SysFont("arial.ttf", 48)
            champs_text = no_champ_font.render(F"NO RECORDS", True, menu.BLACK, menu.DARK_SLATE_GREY)
            champs_text_rect = champs_text.get_rect()
            champs_text_rect.topleft = (
                board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 * 0.55),
                board.line_thickness + (board.square_size + board.line_thickness) * 4)
            screen.blit(champs_text, champs_text_rect)

        # Draw info lines
        # Draw vertical lines
        # left
        pygame.draw.line(screen, menu.GRAY18,
                         (board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 / 2) - (
                                 board.square_size + board.line_thickness) / 2,
                          board.line_thickness + (board.square_size + board.line_thickness) * 1),
                         (board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 / 2) - (
                                 board.square_size + board.line_thickness) / 2,
                          board.line_thickness + (board.square_size + board.line_thickness) * 21),
                         board.line_thickness)
        # right
        pygame.draw.line(screen, menu.GRAY18,
                         (board.line_thickness + (board.square_size + board.line_thickness) * (board.cols + 5) - (
                                 board.square_size + board.line_thickness) / 2,
                          board.line_thickness + (board.square_size + board.line_thickness) * 1),
                         (board.line_thickness + (board.square_size + board.line_thickness) * (board.cols + 5) - (
                                 board.square_size + board.line_thickness) / 2,
                          board.line_thickness + (board.square_size + board.line_thickness) * 21),
                         board.line_thickness)

        # upper 0
        pygame.draw.line(screen, menu.DARK_GREY,
                         (board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 / 2) - (
                                 board.square_size + board.line_thickness) / 2,
                          board.line_thickness + (board.square_size + board.line_thickness) * 1),
                         (board.line_thickness + (board.square_size + board.line_thickness) * (board.cols + 5) - (
                                 board.square_size + board.line_thickness) / 2,
                          board.line_thickness + (board.square_size + board.line_thickness) * 1), board.line_thickness)

        # bottom
        pygame.draw.line(screen, menu.DARK_GREY,
                         (board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 / 2) - (
                                 board.square_size + board.line_thickness) / 2,
                          board.line_thickness + (board.square_size + board.line_thickness) * 21),
                         (board.line_thickness + (board.square_size + board.line_thickness) * (board.cols + 5) - (
                                 board.square_size + board.line_thickness) / 2,
                          board.line_thickness + (board.square_size + board.line_thickness) * 21), board.line_thickness)

        # Draw the frame
        pygame.display.flip()

    def options_init(self):
        pass


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

    def spawn(self):  # to be able spawn figures one by one
        self.i = 4 - self.f_height[1] + self.f_height[2]
        self.j = random.randint(1 - self.f_width[0],
                                board.cols - 1 - self.f_width[1] + self.f_width[2])  # -1 to consider a right border

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
                    return False

        return True

    # right
    def can_move_right(self):
        for jj in range(self.f_width[0], self.f_width[1] - self.f_width[2]):
            for ii in range(self.f_height[0], self.f_height[1] - self.f_height[2]):
                if board.board[self.i + ii][self.j + 1 + jj] + self.form[ii][jj] == 2:
                    return False

        return True

    # bottom
    def can_move_down(self):
        for ii in range(self.f_height[0], self.f_height[1] - self.f_height[2]):
            for jj in range(self.f_width[0], self.f_width[1] - self.f_width[2]):
                if board.board[self.i + 1 + ii][self.j + jj] + self.form[ii][jj] == 2:
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
        self.score = 9999
        self.difficulty = {0: 1000, 1: 925, 2: 850, 3: 775, 4: 700, 5: 625, 6: 550, 7: 475, 8: 400, 9: 325, 10: 250,
                           11: 175, 12: 100}
        self.paused = False

    def draw_figure(self, fig):
        for i in range(fig.f_height[1]):
            for j in range(fig.f_width[1]):  # Rectangle (startx, starty, width, heigth)
                if fig.form[i][j]:
                    pygame.draw.rect(screen, menu.BLUE, (
                        (fig.j + j) * (self.square_size + self.line_thickness) + self.line_thickness,
                        (fig.i + i - 2) * (self.square_size + self.line_thickness) + self.line_thickness,
                        self.square_size,
                        self.square_size))

    def full_row(self, last_row):  # finish it!
        score_add = 0
        bonus = 0
        for i in range(last_row, last_row - 4, -1):  # 4 - longest figure
            if all(board.board[i]):
                board.board.remove(board.board[i])
                bonus += 1
                score_add += bonus
        board.board = [[1] + [0] * (self.cols - 2) + [1] for _ in range(bonus)] + board.board
        board.score += score_add

    def filled(self):
        return 1 in self.board[3][1:11]

    def draw_board(self, fig):
        # Fill the background
        screen.fill(menu.GRAY18)
        # Draw vertical lines
        for j in range(0, self.width, self.square_size + self.line_thickness):
            pygame.draw.line(screen, menu.DARK_GREY, (j, 0), (j, self.height), self.line_thickness)
        # Draw horizontal lines
        for i in range(0, self.height, self.square_size + self.line_thickness):
            pygame.draw.line(screen, menu.DARK_GREY, (0, i), (self.width, i), self.line_thickness)

        # Draw figure
        self.draw_figure(figure)

        # Draw filled board part
        for i in range(board.rows):
            for j in range(board.cols):
                if board.board[i + 2][j]:
                    pygame.draw.rect(screen, menu.BLUE, (
                        j * (self.square_size + self.line_thickness) + self.line_thickness,
                        i * (self.square_size + self.line_thickness) + self.line_thickness,
                        self.square_size,
                        self.square_size))

        # Draw board borders
        # left border
        pygame.draw.rect(screen, menu.DARK_SLATE_GREY,
                         (0, 0, self.square_size + self.line_thickness,
                          self.height))  # Rectangle (startx, starty, width, heigth)
        # right border
        pygame.draw.rect(screen, menu.DARK_SLATE_GREY,
                         (
                             self.width - self.square_size - self.line_thickness, 0,
                             (self.square_size + self.line_thickness) * self.cols // 2,
                             self.height))
        # upper border
        pygame.draw.rect(screen, menu.DARK_SLATE_GREY, (0, 0, self.width, self.square_size + self.line_thickness))
        # bottom border
        pygame.draw.rect(screen, menu.DARK_SLATE_GREY,
                         (0, self.height - self.square_size - self.line_thickness, self.width,
                          self.square_size + self.line_thickness))

        # Draw info
        # score text
        score_font = pygame.font.SysFont("arial.ttf", 48)
        score_text = score_font.render("SCORE:", True, menu.BLACK, menu.DARK_SLATE_GREY)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 2),
                                  self.line_thickness + (self.square_size + self.line_thickness) * 2)
        screen.blit(score_text, score_text_rect)

        # score int
        score_font = pygame.font.SysFont("arial.ttf", 48)
        score_int = score_font.render(f"{self.score}", True, menu.BLACK, menu.DARK_SLATE_GREY)
        score_int_rect = score_int.get_rect()
        score_int_rect.topright = (
            self.line_thickness * 2 + (self.square_size + self.line_thickness) * (self.cols + 3.5),
            self.line_thickness + (self.square_size + self.line_thickness) * 2.7)
        screen.blit(score_int, score_int_rect)

        # next figure text
        score_font = pygame.font.SysFont("arial.ttf", 36)
        next_figure_text = score_font.render("NEXT FIGURE", True, menu.BLACK, menu.DARK_SLATE_GREY)
        next_figure_text_rect = next_figure_text.get_rect()
        next_figure_text_rect.center = (
            self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 2),
            self.line_thickness + (self.square_size + self.line_thickness) * 5)
        screen.blit(next_figure_text, next_figure_text_rect)

        # next figure form
        next_figure.i = 8
        next_figure.j = self.cols
        self.draw_figure(next_figure)

        # score text
        score_text_font = pygame.font.SysFont("arial.ttf", 36)
        score_text = score_text_font.render("DIFFICULTY:", True, menu.BLACK, menu.DARK_SLATE_GREY)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 2),
                                  self.line_thickness + (self.square_size + self.line_thickness) * 12)
        screen.blit(score_text, score_text_rect)

        # score int
        score_int_font = pygame.font.SysFont("arial.ttf", 48)
        score_int = score_int_font.render(f"{self.score // 100}", True, menu.BLACK, menu.DARK_SLATE_GREY)
        score_int_rect = score_int.get_rect()
        score_int_rect.topright = (
            self.line_thickness * 2 + (self.square_size + self.line_thickness) * (self.cols + 3.5),
            self.line_thickness + (self.square_size + self.line_thickness) * 12.7)
        screen.blit(score_int, score_int_rect)

        # Draw info lines
        # Draw vertical lines
        # left
        pygame.draw.line(screen, menu.GRAY18,
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 1),
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 21),
                         self.line_thickness)
        # right
        pygame.draw.line(screen, menu.GRAY18,
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 1),
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 21),
                         self.line_thickness)

        # upper 0
        pygame.draw.line(screen, menu.DARK_GREY,
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 1),
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 1), self.line_thickness)

        # upper 1
        pygame.draw.line(screen, menu.DARK_GREY,
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 4),
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 4), self.line_thickness)

        # upper 2
        pygame.draw.line(screen, menu.DARK_GREY,
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 11),
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 11), self.line_thickness)

        # upper 3
        pygame.draw.line(screen, menu.DARK_GREY,
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 14),
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 14), self.line_thickness)

        # bottom
        pygame.draw.line(screen, menu.DARK_GREY,
                         (self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 21),
                         (self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                                 self.square_size + self.line_thickness) / 2,
                          self.line_thickness + (self.square_size + self.line_thickness) * 21), self.line_thickness)

        # Draw the frame
        pygame.display.flip()

    # def GAME_START(self):
    #     pass


# initializing objects
menu = Menu()
figure = Figure()
next_figure = Figure()
board = Board()
figure.spawn()

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((board.width * 1.5 - (board.square_size + board.line_thickness), board.height))

# Title and Icon
pygame.display.set_caption("Tetris")
icon = pygame.image.load("tetris.png")
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        menu.draw_menu()

        # Проверка нажатия клавиши
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:

                menu.GAME_OVER = False
                while not menu.GAME_OVER:

                    # here would be main game logic

                    # detecting keypress
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            menu.GAME_OVER = True

                        # keyboard controls
                        if event.type == pygame.KEYDOWN:
                            if event.key == menu.LEFT and figure.can_move_left():
                                figure.move(0, -1)
                            if event.key == menu.RIGHT and figure.can_move_right():
                                figure.move(0, 1)
                            if event.key == menu.DOWN:
                                if figure.can_move_down():
                                    figure.move(1, 0)
                                else:
                                    figure.fix_at_board()
                                    board.full_row(figure.i + figure.f_height[1] - figure.f_height[2] - 1)
                                    figure = next_figure
                                    figure.spawn()
                                    next_figure = Figure()
                            if event.key == menu.ROTATE and figure.can_rotate():
                                figure.rotate()
                            if event.key == menu.DROP:
                                while figure.can_move_down():
                                    figure.move(1, 0)
                                else:
                                    figure.fix_at_board()
                                    board.full_row(figure.i + figure.f_height[1] - figure.f_height[2] - 1)
                                    figure = next_figure
                                    figure.spawn()
                                    next_figure = Figure()
                            if event.key == menu.EXIT:
                                menu.GAME_OVER = True
                            if event.key == pygame.K_i:
                                print(figure.i, figure.j)

                    # figures moves
                    # Движение фигуры вниз
                    current_time = pygame.time.get_ticks()
                    delta_time = current_time - menu.last_move_down_time
                    if delta_time >= menu.MOVE_DOWN_DELAY and figure.can_move_down():  # if tick passed and figure can move down - move it down
                        figure.move(1, 0)
                        menu.last_move_down_time = current_time
                    if delta_time >= menu.MOVE_DOWN_DELAY * 2 and not figure.can_move_down():  # if two ticks passed and figure can't move down fix it to the board!
                        figure.fix_at_board()
                        board.full_row(figure.i + figure.f_height[1] - figure.f_height[2] - 1)
                        figure = next_figure
                        figure.spawn()
                        next_figure = Figure()
                        menu.last_move_down_time = current_time

                    # difficulty levels
                    diff = board.score // 100
                    if diff in board.difficulty:
                        menu.MOVE_DOWN_DELAY = board.difficulty[diff]

                    # filling reach top
                    if board.filled():
                        menu.GAME_OVER = True

                    # win conditions
                    if board.score >= 10000:
                        waiting_for_input = True
                    else:
                        waiting_for_input = False

                    while waiting_for_input:
                        # YOU WON TEXT
                        won_font = pygame.font.SysFont("arial.ttf", 48)
                        win_text = won_font.render("YOU WON", True, menu.BLACK, menu.DARK_SLATE_GREY)
                        win_text_rect = win_text.get_rect()
                        win_text_rect.center = (
                        board.line_thickness + (board.square_size + board.line_thickness) * (board.cols / 2),
                        board.line_thickness + (board.square_size + board.line_thickness) * 8)
                        screen.blit(win_text, win_text_rect)

                        # RETRY TEXT
                        retry_font = pygame.font.SysFont("arial.ttf", 48)
                        win_text = retry_font.render("RETRY? Y\\N", True, menu.BLACK, menu.DARK_SLATE_GREY)
                        win_text_rect = win_text.get_rect()
                        win_text_rect.center = (
                        board.line_thickness + (board.square_size + board.line_thickness) * (board.cols / 2),
                        board.line_thickness + (board.square_size + board.line_thickness) * 10)
                        screen.blit(win_text, win_text_rect)

                        # detect choice
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                waiting_for_input = False
                                menu.GAME_OVER = True
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    board = Board()
                                    waiting_for_input = False
                                if event.key == pygame.K_n:
                                    board = Board()
                                    menu.GAME_OVER = True
                                    waiting_for_input = False

                        pygame.display.flip()

                    # frame draw
                    board.draw_board(figure)


            elif event.key == pygame.K_o:
                print("o")
                # menu.options_init()
            elif event.key == pygame.K_e:
                running = False

# Quit pygame
pygame.quit()
