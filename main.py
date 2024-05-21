import sys
import pygame
from settings import *
from helpers import *
from game import *



def main_menu():
    text_y = 300
    text_x = 80
    text_top_limit = 290
    text_bottom_limit = 300
    direction = 1  # 1 for moving up, -1 for moving down
    speed = 1 # Speed of the animation
    
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_game()
                    print("game started")

        # Draw background and button
        draw_bg(img=main_menu_bg_image)
        
        #Animate text
        text_y += direction * speed
        if text_y < text_top_limit or text_y > text_bottom_limit:
            direction *= -1  
    
        # Draw text  
        draw_text(text="Enter 'space' to start", font=font, text_col=white, x=80, y=text_y)

        # Update the display
        pygame.display.update()
        
        
# Run the main menu
main_menu()
        
