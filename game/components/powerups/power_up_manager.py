import pygame
import random

from game.components.powerups.shield import Shield
from game.components.powerups.Life import Life
from game.utils.constants import SPACESHIP_SHIELD
from game.components.powerups.rapid_fire import RapidFire

class PowerUpManager:
    def __init__ (self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3, 5)
    

    def generate_power_up(self):
        power_up_type = random.choice([Shield, RapidFire, Life])
        power_up = power_up_type()
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if power_up.rect.colliderect(game.player.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.add_life()

                if isinstance(power_up, RapidFire):  # Verifica si es el power-up "Rapid Fire"
                    game.player.rapid_fire_active = True  # Activar disparo rápido
                    game.player.rapid_fire_duration = self.duration * 100  # Establecer duración del disparo rápido
                    game.player.rapid_fire_end_time = power_up.start_time + game.player.rapid_fire_duration

                else:
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration*1000)
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + 5000, now +10000 )