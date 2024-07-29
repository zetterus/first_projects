import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Отслеживание нажатия клавиш")

# Словарь для сопоставления названий клавиш с их кодами
key_names = {
    pygame.K_UP: "up",
    pygame.K_DOWN: "down",
    pygame.K_LEFT: "left",
    pygame.K_RIGHT: "right",
    pygame.K_SPACE: "space",
    pygame.K_a: "a",
    pygame.K_b: "b",
    pygame.K_c: "c",
    # Добавьте другие клавиши по мере необходимости
}

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Проверка нажатия клавиши
        if event.type == pygame.KEYDOWN:
            if event.key in key_names:  # Проверяем, есть ли клавиша в словаре
                key_name = key_names[event.key]
                print(f"{key_name}, pygame.K_{key_name.upper()}")  # Выводим название и код клавиши
            if event.key == pygame.K_i:
                print("i", "K_i")

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    pygame.time.Clock().tick(60)