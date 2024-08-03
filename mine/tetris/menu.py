import pygame


class Menu:
    def __init__(self):
        self.left = pygame.K_LEFT
        self.right = pygame.K_RIGHT
        self.down = pygame.K_DOWN
        self.rotate = pygame.K_UP

        self.setting_key = None  # Атрибут для отслеживания, какую клавишу нужно изменить

    def set_key(self, key_name):
        if key_name == 'left':
            self.setting_key = 'left'
        elif key_name == 'right':
            self.setting_key = 'right'
        elif key_name == 'down':
            self.setting_key = 'down'
        elif key_name == 'rotate':
            self.setting_key = 'rotate'

    def change_key(self, event_key):
        if self.setting_key:
            if self.setting_key == 'left':
                self.left = event_key
            elif self.setting_key == 'right':
                self.right = event_key
            elif self.setting_key == 'down':
                self.down = event_key
            elif self.setting_key == 'rotate':
                self.rotate = event_key
            self.setting_key = None


def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Key Change Example')

    font = pygame.font.SysFont(None, 48)

    menu = Menu()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == menu.left:
                    menu.set_key('left')
                    menu.left = None
                elif event.key == menu.right:
                    menu.set_key('right')
                    menu.right = None
                elif event.key == menu.down:
                    menu.set_key('down')
                    menu.down = None
                elif event.key == menu.rotate:
                    menu.set_key('rotate')
                    menu.rotate = None
                else:
                    menu.change_key(event.key)

        screen.fill((255, 255, 255))

        # Отображение текущих назначенных клавиш
        left_text = font.render(f"Left: {pygame.key.name(menu.left) if menu.left else 'None'}", True, (0, 0, 0))
        screen.blit(left_text, (50, 50))

        right_text = font.render(f"Right: {pygame.key.name(menu.right) if menu.right else 'None'}", True, (0, 0, 0))
        screen.blit(right_text, (50, 100))

        down_text = font.render(f"Down: {pygame.key.name(menu.down) if menu.down else 'None'}", True, (0, 0, 0))
        screen.blit(down_text, (50, 150))

        rotate_text = font.render(f"Rotate: {pygame.key.name(menu.rotate) if menu.rotate else 'None'}", True, (0, 0, 0))
        screen.blit(rotate_text, (50, 200))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
