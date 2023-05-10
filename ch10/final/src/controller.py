from src import imagegenerator
import pygame

class Controller:
    def __init__(self):
        '''
        intializes pygame and what kind of image is going to be mad
        '''
        pygame.init()
        self.img_gen = imagegenerator.ImageGenerator()
    def mainloop(self):
            '''
            extracts image size to properly get the resolution of image 
            then displays the image made within imagegenerator
            '''
            image = self.img_gen.get()
            image_size = image.get_size()
            self.screen = pygame.display.set_mode((image_size))
            self.screen.blit(image,(0,0))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()