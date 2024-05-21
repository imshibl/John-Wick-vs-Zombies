import random
import pygame
from player import Player

from zombie import Zombie
from health import HealthBar
from settings import *
from helpers import *


john_wick = Player(400, 280, "jhon_wick", 100, 10, 3)

jhon_wick_health_bar = HealthBar(10, 50, john_wick.hp, john_wick.max_hp)

zombies = []
zombie1 = Zombie(900, 280, "zombie", 20, 3, "left")
zombie2 = Zombie(-100, 280, "zombie", 20, 3, "right")
zombie3 = Zombie(1050, 280, "zombie", 20, 3, "left")
zombie4 = Zombie(-250, 280, "zombie", 20, 3, "right")
zombie5 = Zombie(1200, 280, "zombie", 20, 3, "left")
zombie6 = Zombie(-400, 280, "zombie", 20, 3, "right")


zombies.append(zombie1)
zombies.append(zombie2)
zombies.append(zombie3)
zombies.append(zombie4)
zombies.append(zombie5)
zombies.append(zombie6)


run = True
while run:
    clock.tick(fps)
    # draw background
    draw_bg()
    # draw text(name and hp)
    draw_text(text=f"John Wick - HP:{john_wick.hp}",font= font, text_col= red,x= 10,y= 10)
    jhon_wick_health_bar.draw(screen, red, green, john_wick.hp)
    
    draw_text(text=f"Kills:{john_wick.kills}",font=font, text_col=red,x= 700,y= 10)           

    # draw player
    john_wick.update()
    john_wick.draw(screen)
    john_wick.update_cooldown()
    
   
        
    zombies = [zombie for zombie in zombies if zombie.alive]
    if len(zombies) <= 2:
        
        new_zombie_direction = random.choice(["left", "right"])
        if new_zombie_direction == "left":
            new_zombie_start_position = random.randint(900, 1300)
        else:
            new_zombie_start_position = random.randint(-500, -50)
        
        
        new_zombie = Zombie(new_zombie_start_position, 280, "zombie", 20, 3, new_zombie_direction)
        zombies.append(new_zombie)
        

        
    for zombie in zombies:

        zombie.update()
        zombie.draw(screen)
        if zombie.alive:
            zombie.move_towards_player(john_wick)
            zombie.attack(john_wick)
            play_zombie_sound()
            zombie.update_cooldown()
            zombie.update_got_hit_cooldown()
           

            for bullet in john_wick.bullets:
                if bullet.rect.colliderect(zombie.rect):

                    john_wick.bullets.remove(bullet)
                    zombie.take_damage(damage=john_wick.strength, player=john_wick)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            john_wick.action = 2
            john_wick.direction = "right"
            john_wick.move(SCREEN_WIDTH)
        if keys[pygame.K_a]:
            john_wick.action = 3
            john_wick.direction = "left"
            john_wick.move(SCREEN_WIDTH)

        if keys[pygame.K_SPACE]:
            if john_wick.direction == "right":
                john_wick.action = 4
                john_wick.shoot()
                
            else:
                john_wick.action = 5
                john_wick.shoot()
               

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #          if john_wick.direction == "right":
        #             john_wick.action = 4
        #             john_wick.shoot()
        #          else:
        #             john_wick.action = 5
        #             john_wick.shoot()

        # if event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 1:
        #          if john_wick.direction == "right":
        #             john_wick.action = 0
        #          else:
        #             john_wick.action = 1

        if event.type == pygame.KEYUP:

            if (
                event.key == pygame.K_d
                or event.key == pygame.K_a
                or event.key == pygame.K_SPACE
            ):
                if john_wick.direction == "right":
                    john_wick.action = 0
                else:
                    john_wick.action = 1
               
                
  
        
    pygame.display.update()

pygame.quit()
