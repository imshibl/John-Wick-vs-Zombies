
# load images
import pygame
from settings import *


bg_img = pygame.image.load("assets/background.png").convert_alpha()

# function for drawing background
def draw_bg():
    screen.blit(bg_img, (0, 0))
    
    
# function to drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))