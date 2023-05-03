from src import player
from src import enemy
from src import projectile

import pygame
import random

class Controller:
    def __init__(self):
        pygame.key.set_repeat(50, 500)

        self.screen = pygame.display.set_mode()
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background_color = (200, 200, 250)
        self.background.fill(self.background_color)
        # held keys act like repeated strike

        #create modle objects
        self.player = player.Player()

        self.enemies = pygame.sprite.Group()
        num_enemies = 3
        for _ in range(0, num_enemies):
            self.enemies.add(enemy.Enemy())

        self.projectiles = pygame.sprite.Group()

        # cast existing groups to a tuple to add them together with other sprites and make a new group
        self.all_sprites = pygame.sprite.Group(tuple(self.enemies) + (self.player, ))

    def mainloop(self):
        while True:  # one time through the loop is one frame (picture)
            #reset the background to the default color
            background_color = (200, 200, 250)

            # check for events since the last time through the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.move("U")
                    if event.key == pygame.K_DOWN:
                        self.player.move("D")
                    if event.key == pygame.K_LEFT:
                        self.player.move("L")
                    if event.key == pygame.K_RIGHT:
                        self.player.move("R")
                    if event.key == pygame.K_SPACE:
                        if len(self.projectiles.sprites()) <= 5:
                            p = projectile.Projectile(pygame.display.get_window_size()[0])
                            pos = player.rect.midright
                            p.rect.x = pos[0]
                            p.rect.y = pos[1]
                            self.projectiles.add(p)
                            self.all_sprites.add(p)
                        else:
                            print("can't shoot ", len(self.projectiles.sprites()))

            # update models
            for enemy in self.enemies:
                enemy.update()
            for projectile in self.projectiles:
                self.projectile.update()

            # detect and respond to collisions
            fight = pygame.sprite.spritecollide(self.player, self.enemies, False)
            if fight:
                for enemy in fight:
                    if self.player.fight(enemy):
                        enemy.kill()
                    else:
                        self.player.health -= 1
                        #add a bounce effect and visual cue
                        self.player.rect.x -= enemy.rect.w
                        self.background_color = (255, 0, 0)


            bullets = pygame.sprite.groupcollide(self.enemies, self.projectiles, False, True)
            if bullets:
                for enemy in bullets:
                    enemy.pause()

            # check if we need to end the program
            if self.player.health == 0:
                return

            # redraw background
            self.background.fill(self.background_color)
            self.screen.blit(self.background, (0, 0))


            #redraw all models
            self.all_sprites.draw(self.screen)
            #projectiles.draw(screen)

            # update the screen
            pygame.display.flip()