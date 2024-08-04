import pygame
import random
import pickle


# starting screen including "start", "options", "records", "exit"
class Menu:
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
        self.key_to_change = None

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

        # username
        self.username = "NONAME"

    def draw_text(self, j, i, text="NO TEXT", font_size=64, text_color=(16, 16, 16), bg_color=(47, 79, 79),
                  align="center", font="arial.ttf"):
        font = pygame.font.SysFont(font, font_size)
        text = font.render(text, True, text_color, bg_color)
        text_rect = text.get_rect()
        if align == "center":
            text_rect.center = (j, i)
        elif align == "topright":
            text_rect.topright = (j, i)
        elif align == "topleft":
            text_rect.topleft = (j, i)
        screen.blit(text, text_rect)

    def draw_line(self, start, end, width=2, color=(32, 32, 32)):
        pygame.draw.line(screen, color, start, end, width)

    def draw_menu(self):  # изменить считывание рекордов прямо из файла
        # Fill the background
        screen.fill(menu.DARK_SLATE_GREY)

        # menu text
        # start text
        menu_j = board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 / 4)
        start_i = board.line_thickness + (board.square_size + board.line_thickness) * 8
        self.draw_text(menu_j, start_i, "START")

        # options text
        options_i = board.line_thickness + (board.square_size + board.line_thickness) * 10
        self.draw_text(menu_j, options_i, "OPTIONS")

        # exit text
        exit_i = board.line_thickness + (board.square_size + board.line_thickness) * 12
        self.draw_text(menu_j, exit_i, "EXIT")

        # draw highscores text
        highscores_j = board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 * 0.55)
        highscores_i = board.line_thickness + (board.square_size + board.line_thickness) * 1.75
        self.draw_text(highscores_j, highscores_i, "HIGHSCORES:", 48, align="topleft")

        # draw champs list
        try:
            with open(r"D:\python\first_projects\mine\tetris\highscores.pkl", "rb") as file:
                champs_voc = pickle.load(file)
                for place, champ in enumerate(champs_voc.items(), 1):
                    champ_i = board.line_thickness + (board.square_size + board.line_thickness) * (2 + place)
                    self.draw_text(highscores_j, champ_i, F"{place}. {champ[0]}: {champ[1]}", 32, align="topleft")
        except:
            no_rec = board.line_thickness + (board.square_size + board.line_thickness) * 4
            self.draw_text(highscores_j, no_rec, "NO RECORDS", 48, align="topleft")

        # Draw info lines
        # Draw vertical lines
        # left
        start_left_line_j = board.line_thickness + (board.square_size + board.line_thickness) * (
                board.cols * 1.5 / 2) - (board.square_size + board.line_thickness) / 2
        start_left_line_i = board.line_thickness + (board.square_size + board.line_thickness) * 1
        end_left_line_j = board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 / 2) - (
                board.square_size + board.line_thickness) / 2
        end_left_line_i = board.line_thickness + (board.square_size + board.line_thickness) * 21
        self.draw_line((start_left_line_j, start_left_line_i), (end_left_line_j, end_left_line_i))

        # right
        start_right_line_j = board.line_thickness + (board.square_size + board.line_thickness) * (board.cols + 5) - (
                board.square_size + board.line_thickness) / 2
        start_right_line_i = board.line_thickness + (board.square_size + board.line_thickness) * 1
        end_right_line_j = board.line_thickness + (board.square_size + board.line_thickness) * (board.cols + 5) - (
                board.square_size + board.line_thickness) / 2
        end_right_line_i = board.line_thickness + (board.square_size + board.line_thickness) * 21
        self.draw_line((start_right_line_j, start_right_line_i), (end_right_line_j, end_right_line_i))

        # upper
        self.draw_line((start_left_line_j, start_left_line_i), (start_right_line_j, start_right_line_i))

        # bottom
        self.draw_line((end_left_line_j, end_left_line_i), (end_right_line_j, end_right_line_i))

        # Draw the frame
        pygame.display.flip()

    def input_dialog_box(self):
        pass

    def store_record(self):
        try:
            with open(r"D:\python\first_projects\mine\tetris\highscores.pkl", "rb") as file:
                print("try")
                champs_voc = pickle.load(file)
                champs_voc[menu.username] = board.score
                champs_voc = {k: v for k, v in sorted(champs_voc.items(), key=lambda x: x[1], reverse=True)}
                if len(champs_voc) > 10:
                    champs_voc.popitem()
        except:
            print("except")
            champs_voc = {menu.username: board.score}
        finally:
            with open(r"D:\python\first_projects\mine\tetris\highscores.pkl", "wb") as file:
                print("finally")
                pickle.dump(champs_voc, file)

    def options_draw(self):
        # Fill the background
        screen.fill(menu.DARK_SLATE_GREY)

        # options text
        options_text_j = board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 / 2)
        options_text_i = board.line_thickness + (board.square_size + board.line_thickness) * 3
        self.draw_text(options_text_j, options_text_i, "OPTIONS", font_size=96)

        # rotate text
        left_j = board.line_thickness + (board.square_size + board.line_thickness) * 2
        rotate_text_i = board.line_thickness + (board.square_size + board.line_thickness) * 5
        self.draw_text(left_j, rotate_text_i, "ROTATE KEY", align="topleft")

        # rotate value
        right_j = board.line_thickness + (board.square_size + board.line_thickness) * 11
        rotate_value_i = board.line_thickness + (board.square_size + board.line_thickness) * 5
        self.draw_text(right_j, rotate_value_i,
                       f"{pygame.key.name(self.ROTATE).upper() if self.ROTATE else '-'}", align="topleft")

        # down text
        down_text_i = board.line_thickness + (board.square_size + board.line_thickness) * 7
        self.draw_text(left_j, down_text_i, "DOWN KEY", align="topleft")

        # down value
        down_value_i = board.line_thickness + (board.square_size + board.line_thickness) * 7
        self.draw_text(right_j, down_value_i, f"{pygame.key.name(self.DOWN).upper() if self.DOWN else '-'}",
                       align="topleft")

        # right text
        right_text_i = board.line_thickness + (board.square_size + board.line_thickness) * 9
        self.draw_text(left_j, right_text_i, "RIGHT KEY", align="topleft")

        # right value
        right_value_i = board.line_thickness + (board.square_size + board.line_thickness) * 9
        self.draw_text(right_j, right_value_i, f"{pygame.key.name(self.RIGHT).upper() if self.RIGHT else '-'}",
                       align="topleft")

        # left text
        left_text_i = board.line_thickness + (board.square_size + board.line_thickness) * 11
        self.draw_text(left_j, left_text_i, "LEFT KEY", align="topleft")

        # left value
        left_value_i = board.line_thickness + (board.square_size + board.line_thickness) * 11
        self.draw_text(right_j, left_value_i, f"{pygame.key.name(self.LEFT).upper() if self.LEFT else '-'}",
                       align="topleft")

        # drop text
        drop_text_i = board.line_thickness + (board.square_size + board.line_thickness) * 13
        self.draw_text(left_j, drop_text_i, "DROP KEY", align="topleft")

        # drop value
        drop_value_i = board.line_thickness + (board.square_size + board.line_thickness) * 13
        self.draw_text(right_j, drop_value_i, f"{pygame.key.name(self.DROP).upper() if self.DROP else '-'}",
                       align="topleft")

        # name text
        name_text_i = board.line_thickness + (board.square_size + board.line_thickness) * 15
        self.draw_text(left_j, name_text_i, "YOUR NAME", align="topleft")

        # name value
        name_value_i = board.line_thickness + (board.square_size + board.line_thickness) * 15
        self.draw_text(right_j, name_value_i, f"{self.username}",
                       align="topleft")

        # first hint text
        hint_j = board.line_thickness + (board.square_size + board.line_thickness) * (board.cols * 1.5 / 2)
        hint_1_i = board.line_thickness + (board.square_size + board.line_thickness) * 18
        self.draw_text(hint_j, hint_1_i, "press enter to change your name", font_size=36)

        # second hint text
        hint_2_i = board.line_thickness + (board.square_size + board.line_thickness) * 20
        self.draw_text(hint_j, hint_2_i, "press the first letter button to change keybind", font_size=36)

        # Draw info lines
        # Draw vertical lines
        # left
        left_j = board.square_size + board.line_thickness
        right_j = board.line_thickness + (board.square_size + board.line_thickness) * (board.cols + 5) - (
                board.square_size + board.line_thickness) / 2
        top_i = board.line_thickness * 2 + board.square_size
        bottom_i = board.line_thickness + (board.square_size + board.line_thickness) * 21
        self.draw_line((left_j, top_i), (left_j, bottom_i))

        # right
        self.draw_line((right_j, top_i), (right_j, bottom_i))

        # upper
        self.draw_line((left_j, top_i), (right_j, top_i))

        # bottom
        self.draw_line((left_j, bottom_i), (right_j, bottom_i))

        # Draw the frame
        pygame.display.flip()

    def set_key(self, key_name):
        if key_name == 'rotate':
            self.key_to_change = 'rotate'
        elif key_name == 'down':
            self.key_to_change = 'down'
        elif key_name == 'right':
            self.key_to_change = 'right'
        elif key_name == 'left':
            self.key_to_change = 'left'
        elif key_name == 'drop':
            self.key_to_change = 'drop'

    def change_key(self, event_key):
        if self.key_to_change:
            if self.key_to_change == 'rotate':
                self.ROTATE = event_key
            elif self.key_to_change == 'down':
                self.DOWN = event_key
            elif self.key_to_change == 'right':
                self.RIGHT = event_key
            elif self.key_to_change == 'left':
                self.LEFT = event_key
            elif self.key_to_change == 'drop':
                self.DROP = event_key
            self.key_to_change = None


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
        self.score = 0
        self.difficulty = {0: 1000, 1: 925, 2: 850, 3: 775, 4: 700, 5: 625, 6: 550, 7: 475, 8: 400, 9: 325, 10: 250,
                           11: 175, 12: 100}
        self.paused = False

    def draw_rect(self, j=0, i=0, width=None, height=None,
                  color=(0, 100, 255)):  # Rectangle (startx, starty, width, height)
        if width is None:
            width = self.square_size
        if height is None:
            height = self.square_size
        pygame.draw.rect(screen, color, (j, i, width, height))

    def draw_figure(self, fig):
        for ii in range(fig.f_height[1]):
            for jj in range(fig.f_width[1]):
                if fig.form[ii][jj]:
                    start_j = (fig.j + jj) * (self.square_size + self.line_thickness) + self.line_thickness
                    start_i = (fig.i + ii - 2) * (self.square_size + self.line_thickness) + self.line_thickness
                    self.draw_rect(start_j, start_i)

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
            pygame.draw.line(screen, menu.BLACK, (j, 0), (j, self.height), self.line_thickness)
        # Draw horizontal lines
        for i in range(0, self.height, self.square_size + self.line_thickness):
            pygame.draw.line(screen, menu.BLACK, (0, i), (self.width, i), self.line_thickness)

        # Draw figure
        self.draw_figure(fig)

        # Draw filled board part
        for ii in range(board.rows):
            for jj in range(board.cols):
                if board.board[ii + 2][jj]:
                    start_j = jj * (self.square_size + self.line_thickness) + self.line_thickness
                    start_i = ii * (self.square_size + self.line_thickness) + self.line_thickness
                    self.draw_rect(start_j, start_i)

        # Draw board borders
        # left border
        left_border_j = 0
        left_border_i = 0
        left_border_width = self.square_size + self.line_thickness
        border_height = self.height
        self.draw_rect(left_border_j, left_border_i, color=menu.DARK_SLATE_GREY, width=left_border_width,
                       height=border_height)

        # right border
        right_border_j = self.width - self.square_size - self.line_thickness
        right_border_i = 0
        right_border_width = (self.square_size + self.line_thickness) * self.cols // 2
        self.draw_rect(right_border_j, right_border_i, color=menu.DARK_SLATE_GREY, width=right_border_width,
                       height=border_height)

        # upper border
        hor_border_height = self.square_size + self.line_thickness
        self.draw_rect(left_border_j, left_border_j, color=menu.DARK_SLATE_GREY, width=self.width,
                       height=hor_border_height)

        # bottom border
        bottom_border_j = self.height - self.square_size - self.line_thickness
        self.draw_rect(left_border_j, bottom_border_j, color=menu.DARK_SLATE_GREY, width=self.width,
                       height=hor_border_height)

        # Draw info
        # score text
        score_text_j = self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 2)
        score_text_i = self.line_thickness + (self.square_size + self.line_thickness) * 2
        menu.draw_text(score_text_j, score_text_i, "SCORE", font_size=48, text_color=menu.BLACK,
                       bg_color=menu.DARK_SLATE_GREY)

        # score int
        score_j = self.line_thickness * 2 + (self.square_size + self.line_thickness) * (self.cols + 3.5)
        score_i = self.line_thickness + (self.square_size + self.line_thickness) * 2.7
        menu.draw_text(score_j, score_i, f"{self.score}", font_size=48, text_color=menu.BLACK,
                       bg_color=menu.DARK_SLATE_GREY, align="topright")

        # next figure text
        next_figure_text_j = self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 2)
        next_figure_text_i = self.line_thickness + (self.square_size + self.line_thickness) * 5
        menu.draw_text(next_figure_text_j, next_figure_text_i, "NEXT FIGURE", font_size=36, text_color=menu.BLACK,
                       bg_color=menu.DARK_SLATE_GREY)

        # next figure form
        next_figure.i = 8
        next_figure.j = self.cols
        self.draw_figure(next_figure)

        # difficulty text
        diff_text_j = self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 2)
        diff_text_i = self.line_thickness + (self.square_size + self.line_thickness) * 12
        menu.draw_text(diff_text_j, diff_text_i, "DIFFICULTY:", font_size=36, text_color=menu.BLACK,
                       bg_color=menu.DARK_SLATE_GREY)

        # difficulty int
        diff_text_j = self.line_thickness * 2 + (self.square_size + self.line_thickness) * (self.cols + 3.5)
        diff_text_i = self.line_thickness + (self.square_size + self.line_thickness) * 12.7
        menu.draw_text(diff_text_j, diff_text_i, f"{self.score // 100}", font_size=48, text_color=menu.BLACK,
                       bg_color=menu.DARK_SLATE_GREY, align="topright")

        # Draw info lines
        # Draw vertical lines
        # left
        left_v_j = self.line_thickness + (self.square_size + self.line_thickness) * self.cols - (
                self.square_size + self.line_thickness) / 2
        top_v_i = self.line_thickness + (self.square_size + self.line_thickness) * 1
        bot_v_i = self.line_thickness + (self.square_size + self.line_thickness) * 21
        menu.draw_line((left_v_j, top_v_i), (left_v_j, bot_v_i))

        # right
        right_v_j = self.line_thickness + (self.square_size + self.line_thickness) * (self.cols + 5) - (
                self.square_size + self.line_thickness) / 2
        menu.draw_line((right_v_j, top_v_i), (right_v_j, bot_v_i))

        # Draw horizontal lines
        # top
        menu.draw_line((left_v_j, top_v_i), (right_v_j, top_v_i))

        # horizontal 1
        v_1_i = self.line_thickness + (self.square_size + self.line_thickness) * 4
        menu.draw_line((left_v_j, v_1_i), (right_v_j, v_1_i))

        # horizontal 2
        v_2_i = self.line_thickness + (self.square_size + self.line_thickness) * 11
        menu.draw_line((left_v_j, v_2_i), (right_v_j, v_2_i))

        # horizontal 3
        v_3_i = self.line_thickness + (self.square_size + self.line_thickness) * 14
        menu.draw_line((left_v_j, v_3_i), (right_v_j, v_3_i))

        # bottom
        menu.draw_line((left_v_j, bot_v_i), (right_v_j, bot_v_i))

        # Draw the frame
        pygame.display.flip()


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
options_running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        menu.draw_menu()

        # checking keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:

                menu.GAME_OVER = False
                while not menu.GAME_OVER:

                    # here would be main game logic

                    # detecting keypress
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            menu.GAME_OVER = True
                            running = False

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
                                menu.store_record()
                                menu.GAME_OVER = True
                                running = False
                            # if event.key == pygame.K_i:
                            #     print(figure.i, figure.j)

                    # figures moves
                    # figure moves down
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

                    # loose condition (filling reach top)
                    if board.filled():
                        menu.store_record()
                        menu.GAME_OVER = True

                    # win condition
                    if board.score >= 10000:
                        menu.store_record()
                        waiting_for_input = True
                    else:
                        waiting_for_input = False

                    while waiting_for_input:
                        # YOU WON TEXT
                        you_won_text_j = board.line_thickness + (board.square_size + board.line_thickness) * (
                                board.cols / 2)
                        you_won_text_i = board.line_thickness + (board.square_size + board.line_thickness) * 8
                        menu.draw_text(you_won_text_j, you_won_text_i, "YOU WON", font_size=48,
                                       bg_color=menu.DARK_SLATE_GREY, text_color=menu.BLACK)

                        # RETRY TEXT
                        retry_text_j = board.line_thickness + (board.square_size + board.line_thickness) * (
                                board.cols / 2)
                        retry_text_i = board.line_thickness + (board.square_size + board.line_thickness) * 10
                        menu.draw_text(retry_text_j, retry_text_i, "RETRY? Y\\N", font_size=48,
                                       bg_color=menu.DARK_SLATE_GREY, text_color=menu.BLACK)

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
                options_running = True
                while options_running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            options_running = False
                            running = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == menu.EXIT:
                                options_running = False
                            if event.key == menu.ROTATE:
                                menu.set_key('rotate')
                                menu.ROTATE = None
                            elif event.key == menu.DOWN:
                                menu.set_key('down')
                                menu.DOWN = None
                            elif event.key == menu.RIGHT:
                                menu.set_key('right')
                                menu.RIGHT = None
                            elif event.key == menu.LEFT:
                                menu.set_key('left')
                                menu.LEFT = None
                            elif event.key == menu.DROP:
                                menu.set_key('drop')
                                menu.DROP = None
                            elif event.key == pygame.K_RETURN:
                                name_edit = True
                                input_active = True
                                while name_edit:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            name_edit = False
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == menu.EXIT or event.key == pygame.K_RETURN:
                                                name_edit = False
                                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                                input_active = True
                                                menu.username = ""
                                            elif event.type == pygame.KEYDOWN and input_active:
                                                if event.key == pygame.K_RETURN:
                                                    input_active = False
                                                elif event.key == pygame.K_BACKSPACE:
                                                    menu.username = menu.username[:-1]
                                                else:
                                                    menu.username += event.unicode

                                            font = pygame.font.SysFont("arial.ttf", 64)
                                            text_surf = font.render(menu.username, True, (16, 16, 16), (47, 79, 79))
                                            text_rect = text_surf.get_rect()
                                            j = board.line_thickness + (
                                                        board.square_size + board.line_thickness) * 11
                                            i = board.line_thickness + (board.square_size + board.line_thickness) * 15
                                            text_rect.topleft = (j, i)
                                            screen.blit(text_surf, text_rect)
                                            pygame.display.flip()

                            else:
                                menu.change_key(event.key)

                    menu.options_draw()

            elif event.key == pygame.K_e or event.key == menu.EXIT:
                running = False

# Quit pygame
pygame.quit()
