import pygame

pygame.init()
pygame.mixer.init()

#game window
SCREEN_WIDTH = 800
SCREEN_HIGHT = 400

# Load background music
pygame.mixer.music.load("assets/sounds/bg_music.wav")
pygame.mixer.music.play(-1)  # Play the music indefinitely (-1 means loop forever)
pygame.mixer.music.set_volume(0.3)  # Set volume (0.0 to 1.0)

fps = 60
clock = pygame.time.Clock()

#define fonts
font = pygame.font.SysFont("Times New Roman", 24)


#define colors
red = (255, 0, 0)
green = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("John Wick VS Zombie")