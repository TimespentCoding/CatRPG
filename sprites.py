import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0
        self.facing = 'down'

        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('img/sprite_20.png'))
        self.sprites.append(pygame.image.load('img/sprite_21.png'))
        self.sprites.append(pygame.image.load('img/sprite_22.png'))
        self.sprites.append(pygame.image.load('img/sprite_23.png'))
        self.sprites.append(pygame.image.load('img/sprite_24.png'))
        self.sprites.append(pygame.image.load('img/sprite_25.png'))
        self.sprites.append(pygame.image.load('img/sprite_26.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def animate(self):
        self.is_animating = True



    def update(self):

        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


        if self.is_animating == True:
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0


            self.image = self.sprites[self.current_sprite]


    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
            self.animate()
        else:
            self.is_animating = False

        if keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
            self.animate()
        else:
            self.is_animating = False

        if keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
            self.animate()
        else:
            self.is_animating = False

        if keys[pygame.K_w]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
            self.animate()
        else:
            self.is_animating = False

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

