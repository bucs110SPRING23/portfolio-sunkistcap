import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        #just the first line you have to put in the sprite class init
        super().__init__(self)
        #this is required
        self.image = pygame.image.load("assets/projectile.png")
        self.rect = self.image.get_rect()
        self.speed = 1

    def update(self):
        self.rect.x += self.speed