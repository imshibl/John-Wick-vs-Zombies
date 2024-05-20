import pygame
from player import Player
from zombie import Zombie
from health import HealthBar
from settings import *
from helpers import *


john_wick = Player(400, 280, "jhon_wick", 100, 10, 3)

jhon_wick_health_bar = HealthBar(10, 50, john_wick.hp, john_wick.max_hp)

zombie = Zombie(900, 280, "zombie", 20, 3, "left")


run = True
while run:
    clock.tick(fps)
    # draw background
    draw_bg()
    # draw text(name and hp)
    draw_text(f"John Wick - HP:{john_wick.hp}", font, red, 10, 10)
    jhon_wick_health_bar.draw(screen, red, green, john_wick.hp)

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

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                run = False

            if event.key == pygame.K_SPACE:
                if john_wick.direction == "right":
                    john_wick.action = 4
                else:
                    john_wick.action = 5

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_SPACE:
                if john_wick.direction == "right":
                    john_wick.action = 0
                else:
                    john_wick.action = 1
                
           

    zombie.update()
    zombie.draw(screen)
    if zombie.alive:
        zombie.move_towards_player(john_wick)
        zombie.attack(john_wick)
        zombie.update_cooldown()

    # draw player
    john_wick.update()
    john_wick.draw(screen)

    pygame.display.update()

pygame.quit()
