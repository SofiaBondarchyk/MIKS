import pygame
import sys
from utils import update_player_state_text
from player import Player

# Опреділення кольорів
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ініціалізація Pygame
pygame.init()

# Створення екрану
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Joystick Emulation')

# Створення гравця
player = Player()

# Створення шрифту
font = pygame.font.Font(None, 36)

# Початковий текст стану гравця
player_state_text = ""

# Функція для створення тексту та його розміщення на екрані
def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Функція для відображення стану гравця
def draw_player_state():
    draw_text(player_state_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Функція для оновлення текстового відображення стану гравця
def update_player_state_text(new_text=""):
    global player_state_text
    player_state_text = new_text

# Основний цикл гри
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if jump_button_rect.collidepoint(event.pos):
                player.jump()
            elif run_button_rect.collidepoint(event.pos):
                player.run()
            elif squat_button_rect.collidepoint(event.pos):
                player.squat()
            elif long_jump_button_rect.collidepoint(event.pos):
                player.long_jump()

    # Заповнення екрану чорним кольором
    screen.fill(BLACK)

    # Створення та відображення кнопок
    jump_button_rect = pygame.draw.rect(screen, RED, (50, 50, 150, 60))
    run_button_rect = pygame.draw.rect(screen, RED, (200, 50, 150, 60))
    squat_button_rect = pygame.draw.rect(screen, RED, (50, 150, 150, 60))
    long_jump_button_rect = pygame.draw.rect(screen, RED, (200, 150, 150, 60))

    draw_text('Jump', jump_button_rect.centerx, jump_button_rect.centery)
    draw_text('Run', run_button_rect.centerx, run_button_rect.centery)
    draw_text('Squat', squat_button_rect.centerx, squat_button_rect.centery)
    draw_text('Long Jump', long_jump_button_rect.centerx, long_jump_button_rect.centery)

    # Відображення стану гравця
    draw_player_state()

    pygame.display.flip()
