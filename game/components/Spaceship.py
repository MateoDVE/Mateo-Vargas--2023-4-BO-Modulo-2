
import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH , SCREEN_HEIGHT, DEFAULT_TYPE
from game.components.bullets.bullet import Bullet
import random

class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2)- SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10

    def __init__(self):
        pygame.mixer.init()
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.shooting_time = 0
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0
        self.shoot_sound = pygame.mixer.Sound('game/assets/Sonidos/DisparoNave.mp3')
        self.shoot_sound.set_volume(0.1) 
        self.rapid_fire = False
        self.rapid_fire_time = 0
        self.lives = 3



    def update(self, user_input, bullet_manager):
       if user_input[pygame.K_LEFT]:
           self.move_left()
       elif user_input[pygame.K_RIGHT]:
           self.move_right()
       elif user_input[pygame.K_UP]:
           self.move_up()
       elif user_input[pygame.K_DOWN]:
           self.move_down()
        
       if user_input[pygame.K_SPACE]:
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
         self.shoot_sound.play()

        
    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def set_image(self, size = (SHIP_WIDTH, SHIP_HEIGTH), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def activate_rapid_fire(self):
       self.rapid_fire = True
       self.rapid_fire_time = pygame.time.get_ticks() + (self.rapid_fire_time * 1000)
    
    def add_life(self):
        self.lives += 1  # Aumenta en 1 el conteo de vidas del jugador





    
    