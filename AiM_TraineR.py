import pygame
import random

pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

COLORS = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN]

x, y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
RADIUS = 30
font = pygame.font.SysFont("Arial", 30)
start_time = pygame.time.get_ticks()
last_move_time = 0
MOVE_INTERVAL = 750
score = 0
running = True
circle_color = random.choice(COLORS)
background_color = random.choice(COLORS)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - x) ** 2 + (mouse_y - y) ** 2) ** 0.5
            if distance <= RADIUS:
                score += 1
                circle_color = random.choice(COLORS)
                background_color = random.choice(COLORS)
                while circle_color == background_color:
                    circle_color = random.choice(COLORS)

    current_time = pygame.time.get_ticks()
    if current_time - last_move_time >= MOVE_INTERVAL:
        x, y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        last_move_time = current_time

    screen.fill(background_color)
    pygame.draw.circle(screen, circle_color, (x, y), RADIUS)
    score_text = font.render(f"Влучань: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    elapsed_time = (current_time - start_time) // 1000
    time_text = font.render(f"Час: {elapsed_time}, c", True, BLACK)
    screen.blit(time_text, (10, 40))
    pygame.draw.rect(screen, GREEN, (0, 0, 500, 500), 10)
    pygame.display.flip()

pygame.quit()