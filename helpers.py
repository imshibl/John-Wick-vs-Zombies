
# load images
from pygame.font import Font
from settings import *



bg_img = pygame.image.load("assets/background.png").convert_alpha()

# function for drawing background
def draw_bg():
    screen.blit(bg_img, (0, 0))
    
    
# function to drawing text
def draw_text(text:str, font: Font , text_col: tuple, x:int, y:int):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
# Load gun shoot sound effect
shoot_sound = pygame.mixer.Sound("assets/sounds/gun_shoot.wav")  
shoot_sound.set_volume(0.4)  # Set volume (0.0 to 1.0) 

zombie_sound = pygame.mixer.Sound("assets/sounds/zombie_growling.wav") 
zombie_sound.set_volume(0.5)  
def play_gun_shoot_sound():
   zombie_sound.stop()
   shoot_sound.play()

def stop_gun_shoot_sound():
    shoot_sound.stop()
    
# Load zombie growling sound effect

def play_zombie_sound():
    # Set volume (0.0 to 1.0)
   zombie_sound.play()

def stop_zombie_sound():
    zombie_sound.stop()
   
   
   
