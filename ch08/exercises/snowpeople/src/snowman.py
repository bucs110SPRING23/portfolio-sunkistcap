import pygame
import random

class Snowman(pygame.sprite.Sprite):
    
    def __init__(self, x, y, img="assets/snowman.png"):
        super().__init__()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
    def update(self):
        """
        We can have an update method to call for updates that should happen every frame
        This often contains the movement updates for the AI/NPC objects
        """
        self.rect.y += random.randint(-10, 10)   
        self.rect.x += random.randint(-10, 10)