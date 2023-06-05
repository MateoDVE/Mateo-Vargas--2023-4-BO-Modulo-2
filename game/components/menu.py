import pygame
from game.utils.constants import FONT_STYLE2, SCREEN_HEIGHT, SCREEN_WIDTH, BG2




class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDHT = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        screen.fill((225, 225, 225))
        self.font = pygame.font.Font(FONT_STYLE2, 30)
        self.text = self.font.render(message, True, (255, 255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDHT, self.HALF_SCREEN_HEIGHT)
        self.background_image = BG2
    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen, message, x = HALF_SCREEN_WIDHT, y = HALF_SCREEN_HEIGHT, color = (255, 255,255)):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen):
        screen.blit(self.background_image, (0, 0))

    def update_message(self, message):
        self.text = self.font.render(message, True, (255, 255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDHT, self.HALF_SCREEN_HEIGHT)