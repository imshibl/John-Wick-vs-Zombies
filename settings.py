import pygame

pygame.init()
pygame.mixer.init()

#game window
SCREEN_WIDTH = 800
SCREEN_HIGHT = 400

# Load background music
pygame.mixer.music.load("assets/sounds/bg_music.wav")
pygame.mixer.music.play(-1)  # Play the music indefinitely (-1 means loop forever)
pygame.mixer.music.set_volume(0.5)  # Set volume (0.0 to 1.0)

fps = 60
clock = pygame.time.Clock()

#define fonts
font = pygame.font.SysFont("verdana", 24)


#define colors
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("John Wick VS Zombie")


main_menu_bg_image = pygame.image.load("assets/john_wick_vs_zombies_intro_img.png").convert_alpha()
start_game_button = pygame.image.load("assets/start_game_button.png").convert_alpha()
main_game_bg_image = pygame.image.load("assets/background.png").convert_alpha()


# Load gun shoot sound effect
shoot_sound = pygame.mixer.Sound("assets/sounds/gun_shoot.wav")  
shoot_sound.set_volume(0.4)  # Set volume (0.0 to 1.0) 

zombie_sound = pygame.mixer.Sound("assets/sounds/zombie_growling.wav") 
zombie_sound.set_volume(0.5)  