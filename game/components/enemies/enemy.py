import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet
class Enemy(Sprite):
    Y_POS = 20
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 400, 500, 550]
    SPEED_Y = 1
    SPEED_X = 5
    MOV_X = {0: 'left', 1: 'right'}
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60

    def __init__(self):
        self.image = random.choice([ENEMY_1, ENEMY_2, ENEMY_3])
        self.image = pygame.transform.scale(self.image, (self.SHIP_HEIGHT, self.SHIP_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 8)]
        self.rect.y = self.Y_POS
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0
        self.type = 'enemy'
        self.shooting_time = random.randint(30, 50)


    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)

