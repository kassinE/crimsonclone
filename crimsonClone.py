# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 8:23:51 2022

@author: Ernst
"""
import pygame
import random
import numpy as np

pygame.init()

#init dictionary of words
font = pygame.font.SysFont('cambria', 33)
dictionary = ['nerd','cube','zeta','gate','harry','over','tail','nose','pie','cat',
'leg','lamb','mary','head','ice','stab','low','cow','fly','dick','mate',
'lazy','brown','quick','jack','call','unique','tom','jumper','shot','dog',
'road','bill','hat','king','earl','lord','fox','high','the']


# init screen
screen = pygame.display.set_mode((1200,900))
# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 600
playerY = 800
playerX_change = 0
user_text = ''
#kill_count = 0


# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyWord = []
num_enemies = 7

for i in range(num_enemies):
    enemyImg.append(pygame.image.load('monster.png'))
    enemyWord.append(dictionary[np.random.randint(40)])
    enemyX.append(random.randint(0,1100))
    enemyY.append(random.randint(-100,0))
    #enemyX_change.append(0.5)
    enemyY_change = 0.05

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 6
bullet_state = "ready"

score = 0

def player(x,y):
    screen.blit(playerImg,(x,y))
    

def score_(x,y,score,user_text):
    s_score = font.render(str(score),True,(0,0,0))
    s_text = font.render(str(''.join(user_text)),True,(0,0,0))
    screen.blit(s_score,(x,y))
    screen.blit(s_text,(x+600,y+700))
    

def enemy(x,y,i):
    text = font.render(enemyWord[i], True, (0,0,255))
    screen.blit(enemyImg[i],(x,y))
    screen.blit(text,(x,y+20))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x,y))
    
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = np.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
    return (distance < 27)



# game loop

while 1:
    screen.fill((0,128,128))
    #user_text = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## defined in pygame.locals
            pygame.quit()
 #           sys.exit()
        if event.type == pygame.KEYDOWN:

           
           if event.key == pygame.K_RETURN:
               word = ''.join(user_text)
               if word in enemyWord:
                  # enemyWord2 = np.array(enemyWord)
                  # enemyWord2 = enemyWord2[np.array(enemyY).argsort()[::-1]]
                  # enemyWord2 = list(enemyWord2)
                   i = enemyWord.index(word)
                   playerX = enemyX[i]
                   bulletX = playerX
                   fire_bullet(bulletX,bulletY)
                   #(bulletX,bulletY) = (enemyX[i],enemyY[i])
                   if np.mod(score,10) == 0:
                       enemyY_change *= 1.15
              # print(word)
               user_text = []
           elif event.key == pygame.K_BACKSPACE:
               user_text = user_text[:-1]
           else:
               user_text += event.unicode
        
    for i in range(num_enemies):
        if enemyY[i] > 777:
            for j in range(num_enemies):
                enemyY[j] = 2000
            break
            print("Score:",score)
        enemyY[i] += enemyY_change
            
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bullet_state = "ready"
            bulletY = 800
            enemyX[i] = random.randint(0,768)
            enemyY[i] = random.randint(-300,-50)
            enemyWord[i] = dictionary[np.random.randint(40)]
            score += 1
            #if np.mod(score,5) == 0:
            #    enemyX_change  = [i * 1.2 for i in enemyX_change]

        enemy(enemyX[i],enemyY[i],i)
    
    if bulletY <= -300:
        bulletY = 800
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    
    
    
    
    player(playerX,playerY)
    score_(20,20,score,user_text)
    

    pygame.display.update()
    
    
    
