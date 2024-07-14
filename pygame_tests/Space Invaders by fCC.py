import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.png")

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(0, 200)
enemyX_change = 2
enemyY_change = 40

# Shoot
# Ready - you can't see the bullet on the screen
# Fire - the bullet is currently moving
shootImg = pygame.image.load("shoot.png")
shootX = 0
shootY = 480
shootX_change = 0
shootY_change = 10
shoot_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def shoot(x, y):
    global shoot_state
    shoot_state = "fire"
    screen.blit(shootImg, (x + 16, y))  # y + 10


# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check wether its right or left
        if event.type == pygame.KEYDOWN:  # i'll try to remake movement https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_UP:
                playerY_change = -3
            if event.key == pygame.K_DOWN:
                playerY_change = 3
            if event.key == pygame.K_SPACE:
                if shoot_state == "ready":
                    # Get the current x coordinate of the spaceship
                    shootX = playerX
                    shoot(playerX, playerY)  # shootY?

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change, playerY_change = 0, 0

    # Player movement and border collisions
    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # Enemy movement and border collisions
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX = 0
        enemyX_change *= -1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX = 736
        enemyX_change *= -1
        enemyY += enemyY_change
    if enemyY <= 0:
        enemyY = 0
        enemyY_change *= -1
    elif enemyY >= 536:
        enemyY = 536
        enemyY_change *= -1

    # Shoot movement and respawn
    if shootY <= 0:
        shootY = playerY
        shoot_state = "ready"

    if shoot_state == "fire":
        shoot(shootX, shootY)  # shootY?
        shootY -= shootY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
