# 불정초 6학년 코딩부 (2023)



import pygame
from pygame.locals import *
from math import pi
import sys
import random
import asyncio
from time import sleep

PI = pi
pygame.init()

WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH,  HEIGHT])
timer  = pygame.time.Clock()
fps = 60




color = 'blue'
randcolor = random.choice(['red', 'cyan', 'blue', 'yellow', 'green', 'purple'])


level = [
[6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
[3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
[0, 0, 0, 0, 0, 0, 3, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 3, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 3, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 3, 0, 0, 0, 0, 0, 0],
[5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
[3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
[3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
[3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
[7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
         ]


initial_level = [
[6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
[3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
[0, 0, 0, 0, 0, 0, 3, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 3, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 3, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 3, 0, 0, 0, 0, 0, 0],
[5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
[3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
[3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
[3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
[7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
         ]


collide_l = []

collide_r = []

collide_u = []

collide_d = []




counter = 0
player_images = []
flicker = True

(435, 686)
player_x = 412
player_y = 662
center_x = player_x + 23
center_y = player_y + 24
direction = 0 # 0 - RIGHT, 1 - UP, 2 - LEFT, 3 - DOWN

player_images.append(pygame.transform.scale(pygame.image.load('pac_man.png'), (45, 45)))
player_images.append(pygame.transform.scale(pygame.image.load('pac_man_closed.png'), (45, 45)))


def in_tile_center(center_x, center_y, htl, vtl):
    if htl/2 - 2 <= center_x % htl <= htl/2 + 1 and vtl/2 - 1 <= center_y % vtl <= vtl/2 + 2:
        return True
    return False




def draw_board(level):
    num1 = round((HEIGHT - 50) / 32)
    num2 = round(WIDTH / 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)

            if level[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, randcolor, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3:
                a = pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
                
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)


def draw_player():
    if direction == 0:
        if counter % 20 < 10:
            screen.blit(player_images[1], (player_x, player_y))
        else:
            screen.blit(player_images[0], (player_x, player_y))
    if direction == 1:
        if counter % 20 < 10:
            screen.blit(pygame.transform.rotate(player_images[1], 90), (player_x, player_y))
        else:
            screen.blit(pygame.transform.rotate(player_images[0], 90), (player_x, player_y))
    if direction == 2:
        if counter % 20 < 10:
            screen.blit(pygame.transform.flip(player_images[1], True, False), (player_x, player_y))
        else:
            screen.blit(pygame.transform.flip(player_images[0], True, False), (player_x, player_y))
    if direction == 3:
        if counter % 20 < 10:
            screen.blit(pygame.transform.rotate(player_images[1], 270), (player_x, player_y))
        else:
            screen.blit(pygame.transform.rotate(player_images[0], 270), (player_x, player_y))





def check_position(centerx, centery):
    turns = [False, False, False, False]
    num1 = (HEIGHT - 50) // 32
    num2 = (WIDTH // 30)
    num3 = 15
    if centerx // 30 < 29:
        if direction == 0:
            if level[centery // num1][(centerx - num3) // num2] < 3:
                turns[1] = True
        if direction == 1:
            if level[centery // num1][(centerx + num3) // num2] < 3:
                turns[0] = True
        if direction == 2:
            if level[(centery + num3) // num1][centerx // num2] < 3:
                turns[3] = True
        if direction == 3:
            if level[(centery - num3) // num1][centerx // num2] < 3:
                turns[2] = True

        if direction == 2 or direction == 3:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num3) // num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num3) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num2) // num2] < 3:
                    turns[1] = True
                if level[centery // num1][(centerx + num2) // num2] < 3:
                    turns[0] = True
        if direction == 0 or direction == 1:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num1) // num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num1) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num3) // num2] < 3:
                    turns[1] = True
                if level[centery // num1][(centerx + num3) // num2] < 3:
                    turns[0] = True
    else:
        turns[0] = True
        turns[1] = True

    return turns


def get_text(text:str) -> pygame.Surface:####################################################################################
    font = pygame.font.Font('font.ttf', 40)
    return font.render(text, True, 'white')
def get_ctext(text:str) -> pygame.Surface:####################################################################################
    font = pygame.font.Font('font.ttf', 40)
    return font.render(text, True, 'cyan')
def get_colored_text(text:str, color:str) -> pygame.Surface:####################################################################################
    font = pygame.font.Font('font.ttf', 80)
    return font.render(text, True, color)

def gameover() -> pygame.Surface:
    font = pygame.font.Font('font.ttf', 50)
    return font.render("READY!", True, 'green')
def real_gameover() -> pygame.Surface:
    font = pygame.font.Font('font.ttf', 50)
    return font.render("GAME OVER", True, 'red')
async def main():
    
    global screen, timer, fps, randcolor, counter, flicker, player_x, player_y, center_x, center_y, direction, level, initial_level

    direction_command = 1
    dir_before = 2
    speed = 3

    centerx = player_x + 23
    centery = player_y + 24

    ghost_positions = []




    def available_paths(hk_x, hk_y, board): # 0-right, 1-up, 2-left, 3-down
        paths = []
        right_tile = board[hk_y][hk_x+1]
        up_tile = board[hk_y-1][hk_x]
        left_tile = board[hk_y][hk_x-1]
        down_tile = board[hk_y+1][hk_x]

        if right_tile <=2:
            paths.append(0)
        if up_tile <=2:
            paths.append(1)
        if left_tile <=2:
            paths.append(2)
        if down_tile <=2:
            paths.append(3)
        
        return paths

    def move_ghost(g_hkx:int, g_hky:int, speed:int, g_dir:int, g_x:int, g_y:int, level:list):
        # if direction_command in turns and in_tile_center(centerx, centery, htl, vtl):
        #     direction = direction_command
        direction = g_dir
        hawkeye_x, hawkeye_y = g_hkx, g_hky
        centerx = g_x
        centery = g_y

        vtl = round((HEIGHT-15) / 33)
        htl = round((WIDTH) / 30)

        turns = available_paths(hawkeye_x, hawkeye_y, level)

        player_x = g_x - 23
        player_y = g_y - 24

        if direction == 0 and direction in turns:
            player_x += speed
        elif direction == 0 and level[hawkeye_y][hawkeye_x] <= 2 and not in_tile_center(centerx, centery, htl, vtl):
            player_x += speed
        elif direction == 1 and direction in turns:
            player_y -= speed
        elif direction == 1 and level[hawkeye_y][hawkeye_x] <= 2 and not in_tile_center(centerx, centery, htl, vtl):
            player_y -= speed
        elif direction == 2 and direction in turns:
            player_x -= speed
        elif direction == 2 and level[hawkeye_y][hawkeye_x] <= 2 and not in_tile_center(centerx, centery, htl, vtl):
            player_x -= speed
        elif direction == 3 and direction in turns:
            player_y += speed
        elif direction == 3 and level[hawkeye_y][hawkeye_x] <= 2 and not in_tile_center(centerx, centery, htl, vtl):
            player_y += speed

        return [player_x, player_y]

    def ideal_turns(ghost_pos:tuple, target_pos:tuple):
        vertical = ghost_pos[1] - target_pos[1]
        horizontal = ghost_pos[0] -target_pos[0]

        turns = []


        if vertical < 0:
            turns.append(3)
        else:
            turns.append(1)
        if horizontal < 0:
            turns.append(0)
        else:
            turns.append(2)
        return random.choice(turns)

    def collide(coordx, coordy) -> bool:
        if abs(coordx[0] - coordy[0]) <= 20 and abs(coordx[1] - coordy[1]) <= 20:
            return True
        return False






    blinky_img = pygame.image.load("blinky.png")
    blinky_img = pygame.transform.scale(blinky_img, (45, 45))
    blinky_direction = 0

    inky_img = pygame.image.load("inky.png")
    inky_img = pygame.transform.scale(inky_img, (45, 45))
    inky_direction = 2

    pinky_img = pygame.image.load("pinky.png")
    pinky_img = pygame.transform.scale(pinky_img, (45, 45))
    pinky_direction = 2

    clyde_img = pygame.image.load("clyde.png")
    clyde_img = pygame.transform.scale(clyde_img, (45, 45))
    clyde_direction = 2


    scared_img = pygame.image.load("scared.png")
    scared_img = pygame.transform.scale(scared_img, (45, 45))



    ghost_initial_positions = [[495, 72], [225, 686], [403,72], [675, 686]]
    ghost_positions = [[495, 72], [225, 686], [403,72], [675, 686]]

    vtl = round((HEIGHT-15) / 33)
    htl = round((WIDTH) / 30)

    tile_border_x = range(0, WIDTH, htl)
    tile_border_y = range(0, HEIGHT, vtl)

    pac_dots = 0
    powerup = False
    powerup_counter = 0
    show_menu = False

    powerup_termination = -1
    dead = False
    dead_termination = -1
    lives = 2

    blinky_collide = False
    inky_collide = False
    pinky_collide = False
    clyde_collide = False

    ghost_dead = [False, False, False, False]
    ghost_dead_termination = [-1, -1, -1, -1]

    run_m = True
    deadforgood = False

    glv = 1

    success = False
    score = 0
    newscore = 0

    nth_ghost = 1


#########################################################################################################
#########################################################################################################
#########################################################################################################  ^o^
########################################################################################################
    run_game = True

    logo = pygame.image.load("paclogo.png")
    logo = pygame.transform.scale(logo, (600, 300))

    cherry = pygame.image.load("cherry.png")
    cherry = pygame.transform.scale(cherry, (45, 45))

    sound_siren = pygame.mixer.Sound("siren.ogg")
	
	
    while run_game:

        with open("hiscore.txt") as f:

            hiscore = int(f.read())

                
        level = [
        [6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
        [3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
        [3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
        [3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
        [3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
        [8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 3, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 3, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
        [3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
        [3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
        [3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
        [3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
        [3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
        [3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
        [7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
                ]

        screen.fill('black')
        pygame.display.flip()
        dead = False
        deadforgood = False
        deadforgood_termination = -1
        player_x, player_y = 412, 662

        pac_dots = 0
        powerup = False
        powerup_counter = 0
        show_menu = False

        powerup_termination = -1
        dead = False
        dead_termination = -1
        lives = 2

        blinky_collide = False
        inky_collide = False
        pinky_collide = False
        clyde_collide = False
        ghost_positions = [[495, 72], [225, 686], [403,72], [675, 686]]

        blinky_direction = 0
        pinky_direction = 2
        inky_direction = 2
        clyde_direction = 2

        ghost_dead = [False, False, False, False]
        ghost_dead_termination = [-1, -1, -1, -1]

        run_m = True
        deadforgood = False

        glv = 1

        success = False
        score = 0
        newscore = 0
        nth_ghost = 1

        eaten1 = False
        eaten2 = False

        blinky_img = pygame.image.load("blinky.png")
        blinky_img = pygame.transform.scale(blinky_img, (45, 45))


        inky_img = pygame.image.load("inky.png")
        inky_img = pygame.transform.scale(inky_img, (45, 45))


        pinky_img = pygame.image.load("pinky.png")
        pinky_img = pygame.transform.scale(pinky_img, (45, 45))


        clyde_img = pygame.image.load("clyde.png")
        clyde_img = pygame.transform.scale(clyde_img, (45, 45))
        run = True
        while run:
            screen.fill('black')
            screen.blit(logo, (200, 200))
            screen.blit(get_text('PRESS ANY KEY'), (365, 400))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    run = False
            pygame.display.flip()

            await asyncio.sleep(0)


        blinky_img = pygame.image.load("blinky.png")
        blinky_img = pygame.transform.scale(blinky_img, (45, 45))


        inky_img = pygame.image.load("inky.png")
        inky_img = pygame.transform.scale(inky_img, (45, 45))


        pinky_img = pygame.image.load("pinky.png")
        pinky_img = pygame.transform.scale(pinky_img, (45, 45))


        clyde_img = pygame.image.load("clyde.png")
        clyde_img = pygame.transform.scale(clyde_img, (45, 45))
        direction = 0
        direction_command = 1
        level = [
        [6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
        [3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
        [3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
        [3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
        [3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
        [8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 3, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 3, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
        [3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
        [3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
        [3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
        [3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
        [3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
        [3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
        [7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
                ]

        screen.fill('black')
        pygame.display.flip()
        dead = False
        deadforgood = False
        deadforgood_termination = -1
        player_x, player_y = 412, 662

        pac_dots = 0
        powerup = False
        powerup_counter = 0
        show_menu = False

        powerup_termination = -1
        dead = False
        dead_termination = -1
        lives = 2

        blinky_collide = False
        inky_collide = False
        pinky_collide = False
        clyde_collide = False
        ghost_positions = [[495, 72], [225, 686], [403,72], [675, 686]]

        blinky_direction = 0
        pinky_direction = 2
        inky_direction = 2
        clyde_direction = 2

        ghost_dead = [False, False, False, False]
        ghost_dead_termination = [-1, -1, -1, -1]

        run_m = True
        deadforgood = False

        glv = 1

        success = False
        score = 0
        nth_ghost = 1

        eaten1 = False
        eaten2 = False

        cherry = pygame.image.load("cherry.png")
        cherry = pygame.transform.scale(cherry, (45, 45))
        
        
        sound_chomp = pygame.mixer.Sound("pacman_chomp.ogg")
        sound_eatfruit = pygame.mixer.Sound("pacman_eatfruit.ogg")
        sound_eatghost = pygame.mixer.Sound("pacman_eatghost.ogg")
        sound_start = pygame.mixer.Sound("pacman_start.ogg")
        sound_death = pygame.mixer.Sound("pacman_death.ogg")
        
        
        sound_siren = pygame.mixer.Sound("siren.ogg")
        
        pygame.mixer.stop()
        
        sound_start.play()
        sound_siren.play(-1)

        while run_m:

            
            if score >= hiscore:
                with open("hiscore.txt", 'w') as f:
                    f.write(str(hiscore))

                hiscore = score


            
            centerx = player_x + 23
            centery = player_y + 24

            hawkeye_x = centerx // htl 
            hawkeye_y = centery // vtl 
            turns = available_paths(hawkeye_x, hawkeye_y, level)
            tot = level[hawkeye_y][hawkeye_x] # type of tile

            

            blinky_hkx = ghost_positions[0][0] // htl
            blinky_hky = ghost_positions[0][1] // vtl

            inky_hkx = ghost_positions[1][0] // htl
            inky_hky = ghost_positions[1][1] // vtl

            pinky_hkx = ghost_positions[2][0] // htl
            pinky_hky = ghost_positions[2][1] // vtl

            clyde_hkx = ghost_positions[3][0] // htl
            clyde_hky = ghost_positions[3][1] // vtl

            if collide(ghost_positions[0], (centerx, centery)):
                blinky_collide = True
                if not ghost_dead[0] and not dead:
                	sound_eatghost.play()
            else:blinky_collide = False
            if collide(ghost_positions[1], (centerx, centery)):
                inky_collide = True
                if not ghost_dead[1] and not dead:
                	sound_eatghost.play()
            else:inky_collide = False
            if collide(ghost_positions[2],(centerx, centery)):
                pinky_collide = True
                if not ghost_dead[2] and not dead:
                	sound_eatghost.play()
            else:pinky_collide = False
            if collide(ghost_positions[3], (centerx, centery)):
                clyde_collide = True
                if not ghost_dead[3] and not dead:
                	sound_eatghost.play()
            else:clyde_collide = False

            powerup_counter += 1
            if powerup_counter == powerup_termination:
                powerup = False
                nth_ghost = 1
                blinky_img = pygame.image.load("blinky.png")
                blinky_img = pygame.transform.scale(blinky_img, (45, 45))


                inky_img = pygame.image.load("inky.png")
                inky_img = pygame.transform.scale(inky_img, (45, 45))


                pinky_img = pygame.image.load("pinky.png")
                pinky_img = pygame.transform.scale(pinky_img, (45, 45))


                clyde_img = pygame.image.load("clyde.png")
                clyde_img = pygame.transform.scale(clyde_img, (45, 45))

            if (powerup_termination - powerup_counter) < 80 and powerup:
                if powerup_counter%10 < 5:
                    blinky_img = pygame.image.load("blinky.png")
                    blinky_img = pygame.transform.scale(blinky_img, (45, 45))


                    inky_img = pygame.image.load("inky.png")
                    inky_img = pygame.transform.scale(inky_img, (45, 45))


                    pinky_img = pygame.image.load("pinky.png")
                    pinky_img = pygame.transform.scale(pinky_img, (45, 45))


                    clyde_img = pygame.image.load("clyde.png")
                    clyde_img = pygame.transform.scale(clyde_img, (45, 45))
                else:
                    blinky_img = scared_img
                    inky_img = scared_img
                    pinky_img = scared_img
                    clyde_img = scared_img

            if powerup_counter == ghost_dead_termination[0]:
                ghost_dead[0] = False
            if powerup_counter == ghost_dead_termination[1]:
                ghost_dead[1] = False
            if powerup_counter == ghost_dead_termination[2]:
                ghost_dead[2] = False
            if powerup_counter == ghost_dead_termination[3]:
                ghost_dead[3] = False

            if powerup_counter == dead_termination:
                dead = False


            # if deadforgood_termination == powerup_counter:
            #     run_m = False

            if counter < 19:
                counter += 1
                if counter > 10:
                    flicker = False

            else:
                counter = 0
                flicker = True
            if counter % 20 == 0:
                randcolor = random.choice(['red', 'cyan', 'blue', 'yellow', 'green', 'purple'])


            if (blinky_collide or pinky_collide or inky_collide or clyde_collide) and not powerup and not ((ghost_dead[0] or ghost_dead[1] or ghost_dead[2] or ghost_dead[3])):
                ghost_positions = ghost_initial_positions
                player_x = 412
                player_y = 662
                direction = 0
                dead = True
                dead_termination  = powerup_counter + 200
                lives -= 1
            elif blinky_collide and powerup and not ghost_dead[0]:
                ghost_dead[0] = True
                ghost_dead_termination[0] = powerup_counter + 200
                score += 2**nth_ghost * 100
                newscore = 2**nth_ghost * 100
                nth_ghost += 1

            elif inky_collide and powerup and not ghost_dead[1]:
                ghost_dead[1] = True
                ghost_dead_termination[1] = powerup_counter + 200
                score += 2**nth_ghost * 100
                newscore = 2**nth_ghost * 100
                nth_ghost += 1
            elif pinky_collide and powerup and not ghost_dead[2]:
                ghost_dead[2] = True
                ghost_dead_termination[2] = powerup_counter + 200
                score += 2**nth_ghost * 100
                newscore = 2**nth_ghost * 100
                nth_ghost += 1
            elif clyde_collide and powerup and not ghost_dead[3]:
                ghost_dead[3] = True
                ghost_dead_termination[3] = powerup_counter + 200
                score += 2**nth_ghost * 100
                newscore = 2**nth_ghost * 100
                nth_ghost += 1

            timer.tick(fps)
            screen.fill('black')
            draw_board(level)

            if lives == -1:
                deadforgood = True

            if dead and not deadforgood:
                screen.blit(gameover(), (365, 420))
                ghost_positions = [[495, 72], [225, 686], [403,72], [675, 686]]
                sound_eatghost.stop()
                
               	# sound_death.play()
                	


            if show_menu:
                screen.blit(get_text(f'x: {centerx}'), (50, 100))
                screen.blit(get_text(f'y: {centery}'), (50, 150))
                screen.blit(get_text(f'hawkeye_x: {hawkeye_x}'), (50, 200))
                screen.blit(get_text(f'hawkeye_y: {hawkeye_y}'), (50, 250))
                screen.blit(get_text(f'TOT: {tot}'), (50, 300))
                screen.blit(get_text(f'pac-dot: {pac_dots}'), (50, 350))
                screen.blit(get_text(f'IN CENTER?: {in_tile_center(centerx, centery, htl, vtl)}'), (50, 400))
                screen.blit(get_text(f'turns: {turns}'), (50, 450))
                screen.blit(get_text(f'dir command: {direction_command}'), (50, 500))
                screen.blit(get_text(f'direction: {direction}'), (50, 550))
                screen.blit(get_text(f'PWUP: {powerup}'), (50, 600))
                screen.blit(get_text(f'lives: {lives}'), (50, 650))
            screen.blit(get_text(f'SCORE {score}'), (20, 5))
            screen.blit(get_text(f'HI {hiscore}'), (340, 5))
            screen.blit(get_ctext(f'+ {newscore}'), (540, 5))
            if lives > 0:
                screen.blit(player_images[0], (240, 5))
            if lives > 1:
                screen.blit(player_images[0], (290, 5))



            if tot == 1:
                level[hawkeye_y][hawkeye_x] = 0
                pac_dots += 1
                score += 10


                sound_chomp.play()
            elif tot == 2:
                level[hawkeye_y][hawkeye_x] = 0
                powerup = True
                powerup_termination = powerup_counter + 400
                blinky_img = scared_img
                inky_img = scared_img
                pinky_img = scared_img
                clyde_img = scared_img
                score += 200
                newscore = 200


            if not eaten1:
                screen.blit(cherry, (412, 518-24))
            if collide((435, 518), (centerx, centery)) and not eaten1:
                eaten1 = True
                score += 100
                newscore = 100
                sound_eatfruit.play()








            # for x in tile_border_x:
            #     pygame.draw.line(screen, 'cyan', (x,0), (x, HEIGHT))
            # for y in tile_border_y:
            #     pygame.draw.line(screen, 'cyan', (0,y), (WIDTH, y))

            draw_player()

            if not ghost_dead[0]:
                screen.blit(blinky_img, (ghost_positions[0][0]-23, ghost_positions[0][1]-24))
            if not ghost_dead[1]:
                screen.blit(inky_img, (ghost_positions[1][0]-23, ghost_positions[1][1]-24))
            if not ghost_dead[2]:
                screen.blit(pinky_img, (ghost_positions[2][0]-23, ghost_positions[2][1]-24))
            if not ghost_dead[3]:
                screen.blit(clyde_img, (ghost_positions[3][0]-23, ghost_positions[3][1]-24))






            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run_game = False
                    if event.key == pygame.K_RIGHT:
                        direction_command = 0

                    if event.key == pygame.K_UP:
                        direction_command = 1

                    if event.key == pygame.K_LEFT:
                        direction_command = 2


                    if event.key == pygame.K_DOWN:
                        direction_command = 3

                    if event.key == pygame.K_TAB:
                        show_menu = True

                    if event.key == pygame.K_p:
                        if powerup == True:
                            powerup = False
                        elif powerup == False:
                            powerup = True
                    if event.key == pygame.K_d:
                        pac_dots += 20
                    if event.key == pygame.K_r:
                        level = initial_level
                    if event.key == pygame.K_s:
                        success = True
                        run_m = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_TAB:
                        show_menu = False

            if  pac_dots == 242 or pac_dots == 241:
                level = initial_level
                success = True
                run_m = False




            if dead:
                speed = 0
            elif powerup:
                speed = 2
            else:
                speed = 3
            if len(available_paths(blinky_hkx, blinky_hky, level)) > 2 and in_tile_center(ghost_positions[0][0], ghost_positions[0][1], htl, vtl):
                # blinky_direction = random.choice(available_paths(blinky_hkx, blinky_hky, level))
                turn = ideal_turns(ghost_positions[0], (centerx, centery))
                if turn in available_paths(blinky_hkx, blinky_hky, level):
                    blinky_direction = turn
                else:
                    blinky_direction = random.choice(available_paths(blinky_hkx, blinky_hky, level))

            if blinky_direction == 0 and blinky_direction in available_paths(blinky_hkx, blinky_hky, level):
                ghost_positions[0][0] = ghost_positions[0][0] + speed
            elif blinky_direction == 0 and level[blinky_hky][blinky_hkx] < 3 and not in_tile_center(ghost_positions[0][0], ghost_positions[0][1], htl, vtl):
                ghost_positions[0][0] = ghost_positions[0][0] + speed
            elif blinky_direction == 0:
                # blinky_direction = random.choice(available_paths(blinky_hkx, blinky_hky, level))
                turn = ideal_turns(ghost_positions[0], (centerx, centery))
                if turn in available_paths(blinky_hkx, blinky_hky, level):
                    blinky_direction = turn
                else:
                    blinky_direction = random.choice(available_paths(blinky_hkx, blinky_hky, level))

            elif blinky_direction == 3 and blinky_direction in available_paths(blinky_hkx, blinky_hky, level):
                ghost_positions[0][1] = ghost_positions[0][1] + speed
            elif blinky_direction == 3 and level[blinky_hky][blinky_hkx] < 3 and not in_tile_center(ghost_positions[0][0], ghost_positions[0][1], htl, vtl):
                ghost_positions[0][1] = ghost_positions[0][1] + speed
            elif blinky_direction == 3:
                # blinky_direction = random.choice(available_paths(blinky_hkx, blinky_hky, level))
                turn = ideal_turns(ghost_positions[0], (centerx, centery))
                if turn in available_paths(blinky_hkx, blinky_hky, level):
                    blinky_direction = turn
                else:
                    blinky_direction = random.choice(available_paths(blinky_hkx, blinky_hky, level))

            elif blinky_direction == 2 and blinky_direction in available_paths(blinky_hkx, blinky_hky, level):
                ghost_positions[0][0] = ghost_positions[0][0] - speed
            elif blinky_direction == 2 and level[blinky_hky][blinky_hkx] < 3 and not in_tile_center(ghost_positions[0][0], ghost_positions[0][1], htl, vtl):
                ghost_positions[0][0] = ghost_positions[0][0] - speed
            elif blinky_direction == 2:
                # blinky_direction = random.choice(available_paths(blinky_hkx, blinky_hky, level))
                turn = ideal_turns(ghost_positions[0], (centerx, centery))
                if turn in available_paths(blinky_hkx, blinky_hky, level):
                    blinky_direction = turn
                else:
                    blinky_direction = random.choice(available_paths(blinky_hkx, blinky_hky, level))

            elif blinky_direction == 1 and blinky_direction in available_paths(blinky_hkx, blinky_hky, level):
                ghost_positions[0][1] = ghost_positions[0][1] - speed
            elif blinky_direction == 1 and level[blinky_hky][blinky_hkx] < 3 and not in_tile_center(ghost_positions[0][0], ghost_positions[0][1], htl, vtl):
                ghost_positions[0][1] = ghost_positions[0][1] - speed
            elif blinky_direction == 1:
                # blinky_direction = random.choice(available_paths(blinky_hkx, blinky_hky, level))
                turn = ideal_turns(ghost_positions[0], (centerx, centery))
                if turn in available_paths(blinky_hkx, blinky_hky, level):
                    blinky_direction = turn
                else:
                    blinky_direction = random.choice(available_paths(blinky_hkx, blinky_hky, level))




            if len(available_paths(inky_hkx, inky_hky, level)) > 2 and in_tile_center(ghost_positions[1][0], ghost_positions[1][1], htl, vtl):
                inky_direction = random.choice(available_paths(inky_hkx, inky_hky, level))
            if inky_direction == 0 and inky_direction in available_paths(inky_hkx, inky_hky, level):
                ghost_positions[1][0] = ghost_positions[1][0] + speed
            elif inky_direction == 0 and level[inky_hky][inky_hkx] < 3 and not in_tile_center(ghost_positions[1][0], ghost_positions[1][1], htl, vtl):
                ghost_positions[1][0] = ghost_positions[1][0] + speed
            elif inky_direction == 0:
                inky_direction = random.choice(available_paths(inky_hkx, inky_hky, level))
            elif inky_direction == 3 and inky_direction in available_paths(inky_hkx, inky_hky, level):
                ghost_positions[1][1] = ghost_positions[1][1] + speed
            elif inky_direction == 3 and level[inky_hky][inky_hkx] < 3 and not in_tile_center(ghost_positions[1][0], ghost_positions[1][1], htl, vtl):
                ghost_positions[1][1] = ghost_positions[1][1] + speed
            elif inky_direction == 3:
                inky_direction = random.choice(available_paths(inky_hkx, inky_hky, level))
            elif inky_direction == 2 and inky_direction in available_paths(inky_hkx, inky_hky, level):
                ghost_positions[1][0] = ghost_positions[1][0] - speed
            elif inky_direction == 2 and level[inky_hky][inky_hkx] < 3 and not in_tile_center(ghost_positions[1][0], ghost_positions[1][1], htl, vtl):
                ghost_positions[1][0] = ghost_positions[1][0] - speed
            elif inky_direction == 2:
                inky_direction = random.choice(available_paths(inky_hkx, inky_hky, level))
            elif inky_direction == 1 and inky_direction in available_paths(inky_hkx, inky_hky, level):
                ghost_positions[1][1] = ghost_positions[1][1] - speed
            elif inky_direction == 1 and level[inky_hky][inky_hkx] < 3 and not in_tile_center(ghost_positions[1][0], ghost_positions[1][1], htl, vtl):
                ghost_positions[1][1] = ghost_positions[1][1] - speed
            elif inky_direction == 1:
                inky_direction = random.choice(available_paths(inky_hkx, inky_hky, level))

            if dead:
                speed = 0
            elif powerup:
                speed = 2
            else:
                speed = 4
            if len(available_paths(pinky_hkx, pinky_hky, level)) > 2 and in_tile_center(ghost_positions[2][0], ghost_positions[2][1], htl, vtl):
                # pinky_direction = random.choice(available_paths(pinky_hkx, pinky_hky, level))
                turn = ideal_turns(ghost_positions[2], (centerx, centery))
                if turn in available_paths(pinky_hkx, pinky_hky, level):
                    pinky_direction = turn
                else:
                    pinky_direction = random.choice(available_paths(pinky_hkx, pinky_hky, level))

            if pinky_direction == 0 and pinky_direction in available_paths(pinky_hkx, pinky_hky, level):
                ghost_positions[2][0] = ghost_positions[2][0] + speed
            elif pinky_direction == 0 and level[pinky_hky][pinky_hkx] < 3 and not in_tile_center(ghost_positions[2][0], ghost_positions[2][1], htl, vtl):
                ghost_positions[2][0] = ghost_positions[2][0] + speed
            elif pinky_direction == 0:
                # pinky_direction = random.choice(available_paths(pinky_hkx, pinky_hky, level))
                turn = ideal_turns(ghost_positions[2], (centerx, centery))
                if turn in available_paths(pinky_hkx, pinky_hky, level):
                    pinky_direction = turn
                else:
                    pinky_direction = random.choice(available_paths(pinky_hkx, pinky_hky, level))

            elif pinky_direction == 3 and pinky_direction in available_paths(pinky_hkx, pinky_hky, level):
                ghost_positions[2][1] = ghost_positions[2][1] + speed
            elif pinky_direction == 3 and level[pinky_hky][pinky_hkx] < 3 and not in_tile_center(ghost_positions[2][0], ghost_positions[2][1], htl, vtl):
                ghost_positions[2][1] = ghost_positions[2][1] + speed
            elif pinky_direction == 3:
                # pinky_direction = random.choice(available_paths(pinky_hkx, pinky_hky, level))
                turn = ideal_turns(ghost_positions[2], (centerx, centery))
                if turn in available_paths(pinky_hkx, pinky_hky, level):
                    pinky_direction = turn
                else:
                    pinky_direction = random.choice(available_paths(pinky_hkx, pinky_hky, level))

            elif pinky_direction == 2 and pinky_direction in available_paths(pinky_hkx, pinky_hky, level):
                ghost_positions[2][0] = ghost_positions[2][0] - speed
            elif pinky_direction == 2 and level[pinky_hky][pinky_hkx] < 3 and not in_tile_center(ghost_positions[2][0], ghost_positions[2][1], htl, vtl):
                ghost_positions[2][0] = ghost_positions[2][0] - speed
            elif pinky_direction == 2:
                # pinky_direction = random.choice(available_paths(pinky_hkx, pinky_hky, level))
                turn = ideal_turns(ghost_positions[2], (centerx, centery))
                if turn in available_paths(pinky_hkx, pinky_hky, level):
                    pinky_direction = turn
                else:
                    pinky_direction = random.choice(available_paths(pinky_hkx, pinky_hky, level))

            elif pinky_direction == 1 and pinky_direction in available_paths(pinky_hkx, pinky_hky, level):
                ghost_positions[2][1] = ghost_positions[2][1] - speed
            elif pinky_direction == 1 and level[pinky_hky][pinky_hkx] < 3 and not in_tile_center(ghost_positions[2][0], ghost_positions[2][1], htl, vtl):
                ghost_positions[2][1] = ghost_positions[2][1] - speed
            elif pinky_direction == 1:
                # pinky_direction = random.choice(available_paths(pinky_hkx, pinky_hky, level))
                turn = ideal_turns(ghost_positions[2], (centerx, centery))
                if turn in available_paths(pinky_hkx, pinky_hky, level):
                    pinky_direction = turn
                else:
                    pinky_direction = random.choice(available_paths(pinky_hkx, pinky_hky, level))
            


            if dead:
                speed = 0
            elif powerup:
                speed = 2
            else:
                speed = 3
            if len(available_paths(clyde_hkx, clyde_hky, level)) > 2 and in_tile_center(ghost_positions[3][0], ghost_positions[3][1], htl, vtl):
                clyde_direction = random.choice(available_paths(clyde_hkx, clyde_hky, level))
            if clyde_direction == 0 and clyde_direction in available_paths(clyde_hkx, clyde_hky, level):
                ghost_positions[3][0] = ghost_positions[3][0] + speed
            elif clyde_direction == 0 and level[clyde_hky][clyde_hkx] < 3 and not in_tile_center(ghost_positions[3][0], ghost_positions[3][1], htl, vtl):
                ghost_positions[3][0] = ghost_positions[3][0] + speed
            elif clyde_direction == 0:
                clyde_direction = random.choice(available_paths(clyde_hkx, clyde_hky, level))
            elif clyde_direction == 3 and clyde_direction in available_paths(clyde_hkx, clyde_hky, level):
                ghost_positions[3][1] = ghost_positions[3][1] + speed
            elif clyde_direction == 3 and level[clyde_hky][clyde_hkx] < 3 and not in_tile_center(ghost_positions[3][0], ghost_positions[3][1], htl, vtl):
                ghost_positions[3][1] = ghost_positions[3][1] + speed
            elif clyde_direction == 3:
                clyde_direction = random.choice(available_paths(clyde_hkx, clyde_hky, level))
            elif clyde_direction == 2 and clyde_direction in available_paths(clyde_hkx, clyde_hky, level):
                ghost_positions[3][0] = ghost_positions[3][0] - speed
            elif clyde_direction == 2 and level[clyde_hky][clyde_hkx] < 3 and not in_tile_center(ghost_positions[3][0], ghost_positions[3][1], htl, vtl):
                ghost_positions[3][0] = ghost_positions[3][0] - speed
            elif clyde_direction == 2:
                clyde_direction = random.choice(available_paths(clyde_hkx, clyde_hky, level))
            elif clyde_direction == 1 and clyde_direction in available_paths(clyde_hkx, clyde_hky, level):
                ghost_positions[3][1] = ghost_positions[3][1] - speed
            elif clyde_direction == 1 and level[clyde_hky][clyde_hkx] < 3 and not in_tile_center(ghost_positions[3][0], ghost_positions[3][1], htl, vtl):
                ghost_positions[3][1] = ghost_positions[3][1] - speed
            elif clyde_direction == 1:
                clyde_direction = random.choice(available_paths(clyde_hkx, clyde_hky, level))


            if dead:
                speed = 0
            else:
                speed = 4
                
            if player_x > 850: player_x = 50
            if player_y < 0: player_y = 900
            if player_x < 50: player_x = 850
            if player_y > 900: player_y = 0

            if direction_command in turns and in_tile_center(centerx, centery, htl, vtl):
                direction = direction_command
            if direction == 0 and direction in turns:
                player_x += speed
            elif direction == 0 and level[hawkeye_y][hawkeye_x] <= 2 and not in_tile_center(centerx, centery, htl, vtl):
                player_x += speed
            elif direction == 1 and direction in turns:
                player_y -= speed
            elif direction == 1 and level[hawkeye_y][hawkeye_x] <= 2 and not in_tile_center(centerx, centery, htl, vtl):
                player_y -= speed
            elif direction == 2 and direction in turns:
                player_x -= speed
            elif direction == 2 and level[hawkeye_y][hawkeye_x] <= 2 and not in_tile_center(centerx, centery, htl, vtl):
                player_x -= speed
            elif direction == 3 and direction in turns:
                player_y += speed
            elif direction == 3 and level[hawkeye_y][hawkeye_x] <= 2 and not in_tile_center(centerx, centery, htl, vtl):
                player_y += speed


            if deadforgood:
            	success = True
            	run_m = False
                
            	


                





        

            pygame.display.flip()



            await asyncio.sleep(0)

        pygame.mixer.stop()


        if success and not deadforgood:
            run = True
            while run:
                screen.fill('black')
                screen.blit(get_colored_text('CONGRATULATIONS', 'green'),(250, 300))
                screen.blit(get_text('PRESS ANY KEY'), (365, 400))

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        run = False
                pygame.display.flip()

                await asyncio.sleep(0)
                
        elif success and deadforgood:
            run = True
            while run:
                screen.fill('black')
                screen.blit(get_colored_text('GAME OVER', 'red'), (250, 300))
                screen.blit(get_text('SORRY^_^\nPRESS ANY KEY'), (365, 400))

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:

                        run = False
                pygame.display.flip()

                await asyncio.sleep(0)
                

        with open("hiscore.txt", 'w') as f:
            f.write(str(hiscore))

    await asyncio.sleep(0)
asyncio.run( main() )