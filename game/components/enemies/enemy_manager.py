import pygame
import random
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy_count = 1  
        self.time_since_increase = 0  
        self.increase_interval = 10  

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

        self.time_since_increase += 1  


        if self.time_since_increase >= self.increase_interval * 60:  
            self.time_since_increase = 0  
            self.enemy_count += 3  

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < self.enemy_count:
            enemy = Enemy()
            self.enemies.append(enemy)
    def reset(self):
        self.enemies = []

