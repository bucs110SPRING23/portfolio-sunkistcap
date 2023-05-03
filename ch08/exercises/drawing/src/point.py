import random

import pygame


# sprites - anything that moves and interacts on screen
# inheritance
class Point(pygame.sprite.Sprite):
  def __init__(self, x=0, y=0, color=None, size=10):
    super().__init__()

    self.dot_size = size
    
    if not color:
       self.color = [
         random.randrange(256), 
         random.randrange(256), 
         random.randrange(256)
    ]
    else:
      self.color = color

    # self.image - instance variable, must be a Surface object
    self.image = pygame.Surface((size, size))
    self.image.fill(self.color)


    self.rect = self.image.get_rect() # from the Surface
    self.rect.centerx = x
    self.rect.centery = y

  def set_to_comp_color(self):
    red_comp = 255 - self.color[0]
    blue_comp = 255 - self.color[1]
    green_comp = 255 - self.color[2]
    self.color = [red_comp, blue_comp, green_comp]
    self.image.fill(self.color)

  # hook method (callbacks)
  
  def update(self):
    print("hi")
    self.rect += 1