import pygame


class Player:
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.starting_potions = potions
        self.potions = potions
        self.alive = True
        self.direction = "right"
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # 0 = idle right, 1 = idle left,  2 = run right , 3 = run left, 4 = shoot right, 5 = shoot left, 6 = death right, 7 = death left
        self.update_time = pygame.time.get_ticks()

        # 0 idle right
        temp_list = []
        for i in range(15):
            img = pygame.image.load(f"assets/{self.name}/idle/{i}.png")
            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2, img.get_height() / 2)
            )  # scale up/down image
            image = scaled_image

            temp_list.append(image)

        self.animation_list.append(temp_list)
        
        # 1 idle left
        temp_list = []
        for i in range(15):
            img = pygame.image.load(f"assets/{self.name}/idle/{i}.png")
            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2, img.get_height() / 2)
            )  # scale up/down image
            image = image = pygame.transform.flip(scaled_image, True, False)

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 2 run right
        temp_list = []
        for i in range(15):
            img = pygame.image.load(f"assets/{self.name}/run/{i}.png")

            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2, img.get_height() / 2)
            )  # scale up/down image
            image = scaled_image

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 3 run left
        temp_list = []
        for i in range(15):
            img = pygame.image.load(f"assets/{self.name}/run/{i}.png")

            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2, img.get_height() / 2)
            )  # scale up/down image
            image = pygame.transform.flip(scaled_image, True, False)

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 4 shoot right
        temp_list = []
        for i in range(15):
            img = pygame.image.load(f"assets/{self.name}/shoot/{i}.png")

            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2, img.get_height() / 2)
            )  # scale up/down image
            image = scaled_image

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 5 shoot right
        temp_list = []
        for i in range(15):
            img = pygame.image.load(f"assets/{self.name}/shoot/{i}.png")

            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2, img.get_height() / 2)
            )  # scale up/down image
            image = pygame.transform.flip(scaled_image, True, False)

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 6 death right
        temp_list = []
        for i in range(12):
            img = pygame.image.load(f"assets/{self.name}/death/{i}.png")

            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2, img.get_height() / 2)
            )  # scale up/down image
            image = scaled_image

            temp_list.append(image)

        self.animation_list.append(temp_list)

        # 7 death left
        temp_list = []
        for i in range(12):
            img = pygame.image.load(f"assets/{self.name}/death/{i}.png")

            scaled_image = pygame.transform.scale(
                img, (img.get_width() / 2, img.get_height() / 2)
            )  # scale up/down image
            image = pygame.transform.flip(scaled_image, True, False)

            temp_list.append(image)

        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 3

    def move(self, SCREEN_WIDTH):
        if self.direction == "left" and self.rect.left > 0:

            self.rect.x -= self.speed
            print(self.rect.x)

        elif self.direction == "right" and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
            print(self.rect.x)

    def update(self):
        animation_cooldown = 80
        # update animation
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # check if the animation has run out
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
