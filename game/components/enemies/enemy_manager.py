import pygame
import random
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy_count = 1  # Inicialmente 1 enemigo
        self.time_since_increase = 0  # Tiempo transcurrido desde el último aumento
        self.increase_interval = 10  # Intervalo de aumento en segundos

    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)

        self.time_since_increase += 1  # Incrementar el tiempo transcurrido

        # Verificar si ha pasado el intervalo de aumento
        if self.time_since_increase >= self.increase_interval * 60:  # Multiplicar por 60 para convertir a frames (considerando 60 FPS)
            self.time_since_increase = 0  # Reiniciar el contador de tiempo
            self.enemy_count += 3  # Aumentar en 3 el número de enemigos

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < self.enemy_count:
            enemy = Enemy()
            self.enemies.append(enemy)

