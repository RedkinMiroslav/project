import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Рух_Квадрата_За_Допомогою_Стілок - [вліво] або [вправо]")

square_color = (0, 128, 255)
square_size = 50
square_x = width // 2 - square_size // 2
square_y = height // 2 - square_size // 2
square_position = pygame.math.Vector2(square_x, square_y)
speed = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_position.x -= speed
        if square_position.x < 0:
            square_position.x = 0
    if keys[pygame.K_RIGHT]:
        square_position.x += speed
        if square_position.x > width - square_size:
            square_position.x = width - square_size

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, square_color, (square_position.x, square_position.y, square_size, square_size))
    pygame.display.flip()

pygame.quit()
