import pygame

pygame.init()

#game window
SCREEN_WIDTH = 800
SCREEN_HIGHT = 400

fps = 60
clock = pygame.time.Clock()

#define fonts
font = pygame.font.SysFont("Times New Roman", 24)




#define colors
red = (255, 0, 0)
green = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("John Wick VS Zombie")