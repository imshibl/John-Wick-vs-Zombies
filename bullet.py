import pygame

class Bullet:
    def __init__(self,x,y, direction):
        img = pygame.image.load("assets/bullet.png")
        scaled_img = pygame.transform.scale(img, (img.get_width() / 25, img.get_height() / 25))
        self.image = scaled_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.speed = 10
     
        
    def update(self):
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
            
   
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)