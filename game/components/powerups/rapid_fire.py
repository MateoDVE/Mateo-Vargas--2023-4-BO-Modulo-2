import pygame
from game.components.powerups.power_up import PowerUp
from game.utils.constants import RAPID_FIRE, DEFAULT_TYPE

class RapidFire(PowerUp):
    def __init__(self):
        super().__init__(RAPID_FIRE, DEFAULT_TYPE)

    def activate_power_up(self, player):
        player.activate_rapid_fire()
        player.rapid_fire_time = self.duration  
        
    def deactivate_power_up(self, player):
        player.reset_shoot_delay()  
