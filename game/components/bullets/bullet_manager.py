import pygame
from game.components.powerups.Life import Life
from game.components.powerups.rapid_fire import RapidFire
from game.utils.constants import SHIELD_TYPE
class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.over_sound = pygame.mixer.Sound('game/assets/Sonidos/GameOver.mp3')
        self.over_sound.set_volume(0.1) 

    def update(self, game):
        for power_up in game.power_up_manager.power_ups:
            if isinstance(power_up, RapidFire) and game.player.rect.colliderect(power_up.rect):
                game.player.activate_rapid_fire()
                game.power_up_manager.power_ups.remove(power_up)
            elif isinstance(power_up, Life) and game.player.rect.colliderect(power_up.rect):
                game.add_life()
                game.live = True
                game.life_count += 1
                game.power_up_manager.power_ups.remove(power_up)
                
        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                   game.enemy_manager.enemies.remove(enemy)
                   game.update_score()
                   self.bullets.remove(bullet)
                   
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.death_count += 1
                    game.playing = False
                    self.over_sound.play()
                    pygame.time.delay(100)

                    break
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) <50:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player':
            self.bullets.append(bullet)
    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
