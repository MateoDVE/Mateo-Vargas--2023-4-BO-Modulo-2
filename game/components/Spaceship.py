
import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH , SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet
import random

class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2)- SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.shooting_time = 0
    def update(self, user_input, bullet_manager):
       if user_input[pygame.K_LEFT]:
           self.move_left()
       elif user_input[pygame.K_RIGHT]:
           self.move_right()
       elif user_input[pygame.K_UP]:
           self.move_up()
       elif user_input[pygame.K_DOWN]:
           self.move_down()
       elif user_input[pygame.K_SPACE]:
        self.shoot(bullet_manager)
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.SHIP_SPEED
        else:
            self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.SHIP_SPEED
        else:
            self.rect.x = 0        
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SHIP_SPEED  
    def draw (self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def shoot(self, bullet_manager):
       current_time = pygame.time.get_ticks()
       if current_time - self.shooting_time >= 200:
         bullet = Bullet(self)
         bullet_manager.add_bullet(bullet)
         self.shooting_time = current_time
    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    
    