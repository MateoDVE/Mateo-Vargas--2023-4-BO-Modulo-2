import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants

ASTEROID1 = pygame.image.load(os.path.join(IMG_DIR, "Other/asteroid1.png"))
ASTEROID2 = pygame.image.load(os.path.join(IMG_DIR, "Other/asteroid2.png"))
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))   
BG2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/StarWarsF.png'))   

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
HEART2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart1.png'))
RAPID_FIRE = pygame.image.load(os.path.join(IMG_DIR, 'Other/Up1.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/nave.png"))
FONT_STYLE = 'freesansbold.ttf'
FONT_STYLE2 = "fonts/PressStart2P-vaV7.ttf"

