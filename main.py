import pygame
import random
import numpy as np
import time

pygame.init()
print("Initializing game...")  # Debugging initialization

# Init dictionary of words
#dictionary = np.genfromtxt('crimsonwords.txt', delimiter='\n', dtype='str')
# Init dictionary of words
dictionary = np.array([
    "nerd", "cube", "zeta", "gate", "harry", "over", "tail", "nose", "pie", 
    "cat", "leg", "lamb", "mary", "head", "ice", "stab", "low", "cow", 
    "fly", "dick", "mate", "lazy", "brown", "quick", "jack", "call", 
    "unique", "tom", "jumper", "shot", "dog", "road", "bill", "hat", 
    "king", "earl", "lord", "fox", "high", "the"
])
print(f"Loaded {len(dictionary)} words.")  # Debug

# Init screen
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Space Invaders")
print("Screen initialized.")  # Debug

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BACKGROUND = (0, 128, 128)

# Font for text
font = pygame.font.SysFont('cambria', 33)

# Player variables
playerX = 600
playerY = 800
playerX_change = 0
user_text = ''

# Enemy variables
enemyX = []
enemyY = []
enemyWord = []
num_enemies = 4

# Create enemies
for _ in range(num_enemies):
    enemyX.append(random.randint(0, 1100))
    enemyY.append(random.randint(0, 50))
    enemyWord.append(random.choice(dictionary))

enemyY_change = 0.05 * (1.1) ** 5

# Bullet variables
bulletX = 0
bulletY = 480
bulletY_change = 8
bullet_state = "ready"

# Score variables
score = 0
high_score = 0


playerImg = pygame.image.load('player.png')

def draw_player(x, y):
    #pygame.draw.polygon(screen, BLUE, [(x, y), (x + 50, y + 100), (x - 50, y + 100)])
    screen.blit(playerImg,(x,y))

def draw_enemy(x, y, word):
    pygame.draw.rect(screen, RED, (x, y, 50, 50))
    text = font.render(word, True, BLACK)
    screen.blit(text, (x, y + 60))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    pygame.draw.rect(screen, YELLOW, (x, y, 12, 12))

def display_score(x, y, score, user_text):
    score_text = font.render(f"Score: {score}", True, BLACK)
    high_score_text = font.render(f"High Score: {high_score}", True, BLACK)
    input_text = font.render(f"Input: {''.join(user_text)}", True, BLACK)
    screen.blit(score_text, (x, y))
    screen.blit(high_score_text, (x + 930, y))
    screen.blit(input_text, (x + 600, y + 700))

# Game loop
running = True
while running:
    screen.fill(BACKGROUND)  # Background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                word = ''.join(user_text)
                if word in enemyWord:
                    i = enemyWord.index(word)
                    enemyWord[i] = random.choice(dictionary)
                    enemyX[i] = random.randint(0, 1100)
                    enemyY[i] = random.randint(-50, 50)
                    score += 1
                    print(f"Hit! Word: {word}, Score: {score}")  # Debug
                user_text = []
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    # Update player position
    playerX += playerX_change
    playerX = max(0, min(1150, playerX))  # Bound player to screen

    # Update and draw enemies
    for i in range(num_enemies):
        enemyY[i] += enemyY_change
        if enemyY[i] > 850:
            enemyY[i] = random.randint(-100, -50)
            enemyX[i] = random.randint(0, 1100)
        draw_enemy(enemyX[i], enemyY[i], enemyWord[i])

    # Draw player
    draw_player(playerX, playerY)

    # Display score and input text
    display_score(20, 20, score, user_text)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
