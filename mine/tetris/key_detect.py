import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Отслеживание нажатия клавиш")

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Проверка нажатия клавиши
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)  # Получаем имя нажатой клавиши
            print(f"Нажата клавиша: {key_name}, pygame.K_{key_name}")  # Выводим название и код клавиши

    # Очистка экрана
    screen.fill((0, 0, 0))  # Черный фон

    # Обновление экрана
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
sys.exit()
