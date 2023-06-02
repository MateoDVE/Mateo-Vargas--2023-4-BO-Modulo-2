import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE,FONT_STYLE, FONT_STYLE2
from game.components.Spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.death_count = 0
        self.score = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu('Press any key to Start...', self.screen)
        self.max_score = 0
        
    

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
    


    def run(self):
        # Game loop: events - update - draw
        self.reset_all()
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_imput = pygame.key.get_pressed()
        self.player.update(user_imput, self.bullet_manager)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) 
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_socore()
        pygame.display.update()


    def draw_background(self):

        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_width =SCREEN_WIDTH // 2
        half_screen_height =SCREEN_HEIGHT // 2
        if self.death_count > 0:
            self.menu.update_message('GAME OVER:(')
            score_text = f"Your Score: {self.score}"
            death_text = f"Death count: {self.death_count}"
            max_score_text = f"Max Score: {self.max_score}"

            score_font = pygame.font.Font(FONT_STYLE2, 20)
            death_font = pygame.font.Font(FONT_STYLE2, 20)
            max_score_font = pygame.font.Font(FONT_STYLE2, 20)
            
            

            score_surface = score_font.render(score_text, True, (0, 0, 0))
            death_surface = death_font.render(death_text, True, (0, 0, 0))
            max_score_surface = max_score_font.render(max_score_text, True, (0, 0, 0))

            score_rect = score_surface.get_rect(center=(half_screen_width, half_screen_height + 100))
            death_rect = death_surface.get_rect(center=(half_screen_width, half_screen_height + 150))
            max_score_rect = max_score_surface.get_rect(center=(half_screen_width, half_screen_height + 200))

            self.screen.blit(score_surface, score_rect)
            self.screen.blit(death_surface, death_rect)
            self.screen.blit(max_score_surface, max_score_rect)

        icon = pygame.transform.scale(ICON, (80,120))
        self.screen.blit(icon, (half_screen_width - 50, half_screen_height - 150))
        self.menu.draw(self.screen)
        self.menu.update(self)
    

    def update_score(self):
        self.score += 1
        if self.score > self.max_score:
            self.max_score = self.score

    
    def draw_socore(self):
        font = pygame.font.Font(FONT_STYLE2,20)
        text = font.render(F'Score: {self.score}', True,(255, 255,255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)
    
    def reset_all(self):
        self.score = 0
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        self.player.reset()