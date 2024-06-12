
from pygame.font import Font
from pygame.surface import Surface
from settings import *


# function for drawing background
def draw_bg(img: Surface):
    screen.blit(img, (0, 0))
    
    
# function to drawing text
def draw_text(text:str, font: Font , text_col: tuple, x:int, y:int):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    

    
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
   
   
   
