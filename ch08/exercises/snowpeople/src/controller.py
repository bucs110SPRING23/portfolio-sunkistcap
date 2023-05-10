import pygame

## import models ##
from src.snowman import Snowman

LIGHT_BG = (200, 200, 250)
MAX_SNOWMEN = 20

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()
        self.background = pygame.Surface((self.width, self.height))
        self.background_color = LIGHT_BG
        self.background.fill(self.background_color)
        
        ### initialize models and other data ###

        self.snowpeoples = pygame.sprite.Group()    
        self.max_snowmen = 20
        
        number_of_starting_snowpeople = 3
        interval = self.width/(number_of_starting_snowpeople+1)
        xpos = interval
        for _ in range(number_of_starting_snowpeople):
            new_sm = Snowman(xpos, self.height/2)
            self.snowpeoples.add(new_sm)
            xpos += interval


    def mainloop(self):
        # one time through the loop is one frame (picture)
        while True:  
            
            # check for events since the last time through the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                ## handle any important events ##
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for s in self.snowpeoples:
                        if s.rect.collidepoint(event.pos):
                            s.kill() #remove from all Groups and delete

            ## update models ##

            self.snowpeoples.update()
            
            #remove offscreen sprites
            for s in self.snowpeoples:
                if not s.rect.colliderect(self.background.get_rect()):
                    s.kill()

            #quit if no snowpeople left
            if len(self.snowpeoples) == 0:
                pygame.quit()
                exit()

            #multiply colliding sprites
            for s in self.snowpeoples:
                result = pygame.sprite.spritecollide(s, self.snowpeoples, False)
                if len(result) > 1 and len(self.snowpeoples) < self.max_snowmen:
                    self.snowpeoples.add(Snowman(s.rect.x, s.rect.y))

            ## redraw ##
            self.background.fill(self.background_color)
            self.screen.blit(self.background, (0, 0))
            
            self.snowpeoples.draw(self.screen)

            # update the screen
            pygame.display.flip()