import pygame
from game.components.asteroids.asteroids import Asteroid

class AsteroidManager():
    def __init__(self):
        self.asteroids = []
        self.over_sound = pygame.mixer.Sound('game/assets/Sonidos/GameOver.mp3')
        self.over_sound.set_volume(0.1) 


    def update(self, game):
        self.add_asteroid()

        for asteroid in self.asteroids:
            asteroid.update(self.asteroids)
            self.destroy_player(game, asteroid)
            self.destroy_asteroid(game, asteroid)

    def draw(self, screen):
        for asteroid in self.asteroids:
            asteroid.draw(screen)
        
    def add_asteroid(self):
        if len(self.asteroids) < 1:
            asteroid = Asteroid()
            self.asteroids.append(asteroid)
            self.asteroids.append(asteroid)

    def destroy_player(self, game, asteroid):
        if asteroid.rect.colliderect(game.player.rect):
                game.death_count += 1
                game.playing = False
                pygame.time.delay(1000)
                self.over_sound.play()


    def destroy_asteroid(self, game, asteroid):
        for bullet in game.bullet_manager.bullets:
                if asteroid.rect.colliderect(bullet.rect):
                    game.bullet_manager.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)

    def reset(self):
         self.asteroids = []