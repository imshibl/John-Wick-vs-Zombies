import math
import pygame


class Zombie:
    def __init__(self, x, y, name, max_hp, strength, direction):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.direction = direction
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # 0 = walk left, 1 = walk right, 2 = attack left, 3 = attack right, 4 = hurt left, 5 = hurt right, 6 = death left, 7 = death right
        self.update_time = pygame.time.get_ticks()

        # 0 walk left
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f"assets/{self.name}/walk/{i}.png")
            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2.5, img.get_height() / 2.5)
            )  # scale up/down image
            image = pygame.transform.flip(scaled_image, True, False)

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 1 walk right
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f"assets/{self.name}/walk/{i}.png")
            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2.5, img.get_height() / 2.5)
            )  # scale up/down image
            image = scaled_image

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 2 attack left
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f"assets/{self.name}/attack/{i}.png")
            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2.5, img.get_height() / 2.5)
            )  # scale up/down image
            image = pygame.transform.flip(scaled_image, True, False)

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 3 attack right
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f"assets/{self.name}/attack/{i}.png")
            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2.5, img.get_height() / 2.5)
            )  # scale up/down image
            image = scaled_image

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 4 hurt left
        temp_list = []
        for i in range(5):
            img = pygame.image.load(f"assets/{self.name}/hurt/{i}.png")
            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2.5, img.get_height() / 2.5)
            )  # scale up/down image
            image = pygame.transform.flip(scaled_image, True, False)

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 5 hurt right
        temp_list = []
        for i in range(5):
            img = pygame.image.load(f"assets/{self.name}/hurt/{i}.png")
            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2.5, img.get_height() / 2.5)
            )  # scale up/down image
            image = scaled_image

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 6 death left
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f"assets/{self.name}/dead/{i}.png")
            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2.5, img.get_height() / 2.5)
            )  # scale up/down image
            image = pygame.transform.flip(scaled_image, True, False)

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 7 death right
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f"assets/{self.name}/dead/{i}.png")
            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2.5, img.get_height() / 2.5)
            )  # scale up/down image
            image = scaled_image

            temp_list.append(image)

        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 1  # Speed of the zombie
        self.attack_cooldown = 0  # Cooldown timer for the attack
        self.got_hit_cooldown = 0
        self.death_cooldown = 0

    def update(self):
        animation_cooldown = 80

        # update animation
        if self.action < len(self.animation_list):
            action_frames = self.animation_list[self.action]

            if self.frame_index < len(action_frames):
                self.image = action_frames[self.frame_index]
            else:
                self.frame_index = 0
                self.image = action_frames[self.frame_index]

            # check if enough time has passed since the last update
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1

            # check if the animation has run out

            if self.frame_index >= len(self.animation_list[self.action]):
                if self.alive:

                    self.frame_index = 0
        else:
            # Handle the case where the action is out of range
            raise ValueError(
                f"Action {self.action} is out of range for the animation list."
            )

    def draw(self, screen):

        screen.blit(self.image, self.rect)

    def move_towards_player(self, player):

        if self.got_hit_cooldown == 0 and self.alive:

            if self.rect.centerx < player.rect.centerx - 50:

                self.rect.x += self.speed
                self.direction = "right"
                self.action = 1
            elif self.rect.centerx > player.rect.centerx + 50:
                self.rect.x -= self.speed
                self.direction = "left"
                self.action = 0

    def attack(self, player):

        if self.attack_cooldown == 0 and self.got_hit_cooldown == 0 and self.alive:
            distance = math.sqrt(
                (self.rect.centerx - player.rect.centerx) ** 2
                + (self.rect.centery - player.rect.centery) ** 2
            )
            attack_threshold = 60  # Adjust this value as needed
            if distance < attack_threshold:
                # Attack logic here
                if self.direction == "right":
                    self.action = 3
                else:
                    self.action = 2

                player.hp -= self.strength

                self.attack_cooldown = 60

    def update_cooldown(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def update_got_hit_cooldown(self):
        if self.got_hit_cooldown > 0:
            self.got_hit_cooldown -= 1
            
    def update_death_cooldown(self):
        if self.death_cooldown > 0:
            self.death_cooldown -= 1

    def take_damage(self, damage, john_wick):
        self.hp -= damage
        if self.direction == "right":
            self.action = 5
        else:
            self.action = 4
        self.got_hit_cooldown = 30

        if self.hp <= 0:

            if self.direction == "right":
                self.action = 7
            else:
                self.action = 6
        
            self.alive = False
            john_wick.kills += 1
