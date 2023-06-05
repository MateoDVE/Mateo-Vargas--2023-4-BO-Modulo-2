from game.components.powerups.power_up import PowerUp
from game.utils.constants import HEART, DEFAULT_TYPE

class Life(PowerUp):
    def __init__(self):
        super().__init__(HEART, DEFAULT_TYPE)