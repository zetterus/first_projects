import pygame
import random

from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.png")

# Background sound
mixer.music.load("background.mp3")
mixer.music.set_volume(0.45)
mixer.music.play(-1)

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

# Enemy  # THIS SHOULD BE REFORGED WITH HOLY FIRE AND OOP!!!!!
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 400))
    enemyX_change.append(2)
    enemyY_change.append(40)

# Shoot
# Ready - you can't see the bullet on the screen
# Fire - the bullet is currently moving
shootImg = pygame.image.load("shoot.png")
shootX = 0
shootY = 480
shootX_change = 0
shootY_change = 10
shoot_state = "ready"

# Score

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render(f"Score: {score_value}", True, (0, 255, 255))
    screen.blit(score, (x, y))


def game_over_text(x, y):
    over_text = over_font.render(f"GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def shoot(x, y):
    global shoot_state
    shoot_state = "fire"
    screen.blit(shootImg, (x + 16, y))  # y + 10


def isCollision(enemyX, enemyY, shootX, shootY):
    distance = ((enemyX - shootX) ** 2 + (enemyY - shootY) ** 2) ** 0.5
    if distance < 27:
        return True
    else:
        return False


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
                    shoot_sound = mixer.Sound("laser.wav")
                    shoot_sound.play()
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
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 536:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX[i] = 736
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
        if enemyY[i] <= 0:
            enemyY[i] = 0
            enemyY_change[i] *= -1
        elif enemyY[i] >= 536:
            enemyY[i] = 536
            enemyY_change[i] *= -1

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], shootX, shootY)
        if collision:
            explosion_Sound = mixer.Sound("explosion.wav")
            explosion_Sound.play()
            shootY = playerY
            shoot_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(0, 200)

        enemy(enemyX[i], enemyY[i], i)

    # Shoot movement and respawn
    if shootY <= 0:
        shootY = playerY
        shoot_state = "ready"

    if shoot_state == "fire":
        shoot(shootX, shootY)  # shootY?
        shootY -= shootY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
