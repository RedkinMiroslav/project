# --- Импорт модулей --- #
import pygame
import random
import time

# --- Инициализация PyGame --- #
pygame.init()

# --- Загрузка изображений --- #
try:
    background_img = pygame.image.load("background.png")
    original_snake_img = pygame.image.load("snake.png")
    snake_size = 20
    snake_img = pygame.transform.scale(original_snake_img, (snake_size, snake_size))

    original_apple_img = pygame.image.load("apple.png")
    apple_size = 20
    apple_img = pygame.transform.scale(original_apple_img, (apple_size, apple_size))

# --- На случай если нет изображения --- #
except pygame.error as e:
    print(f"Ошибка загрузки изображения: {e}")
    pygame.quit()
    exit()

# --- Получаем размеры фона --- #
background_width = background_img.get_width()
background_height = background_img.get_height()

# --- Настройка экрана --- #
screen_width = background_width
screen_height = background_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyThon_SnaKe")

# --- Цвета --- #
white = (255, 255, 255)

# --- Скорость змейки --- #
snake_speed = 15

# --- Шрифт для отображения счета и таймера --- #
font_style = pygame.font.SysFont(None, 30)

# --- Функция для отображения счета --- #
def display_score(score):
    value = font_style.render(f"Счет: {score}", True, white)
    screen.blit(value, [screen_width // 2 - value.get_width() // 2, 30])

# --- Функция для отображения таймера ---#
def display_timer(time_left):
    minutes = time_left // 60
    seconds = time_left % 60
    timer_text = font_style.render(f"Время: {minutes:02d}:{seconds:02d}", True, white)
    screen.blit(timer_text, [screen_width // 2 - timer_text.get_width() // 2, 0])

# --- Функция для отрисовки змейки --- #
def draw_snake(snake_body):
    for segment in snake_body:
        screen.blit(snake_img, [segment[0], segment[1]])

# --- Функция для генерации случайной позиции для яблока --- #
def generate_apple():
    apple_x = round(random.randrange(0, screen_width - apple_size) / 10.0) * 10.0
    apple_y = round(random.randrange(0, screen_height - apple_size) / 10.0) * 10.0
    return apple_x, apple_y

# --- Основной игровой цикл --- #
def game_loop():
    game_over = False
    game_close = False
    game_won = False

    # --- Начальная позиция змейки --- #
    x1 = screen_width / 2
    y1 = screen_height / 2

    # --- Изменение позиции змейки --- #
    x1_change = 0
    y1_change = 0

    # --- Тело змейки --- #
    snake_body = [[x1, y1]]
    snake_length = 1

    # --- Список позиций яблок --- #
    apples = []
    num_apples = 15
    for _ in range(num_apples):
        apples.append(generate_apple())

    # --- Счет --- #
    score = 0

    # --- Таймер --- #
    game_time = 180  
    start_time = time.time()

    clock = pygame.time.Clock()

    while not game_over:
        current_time = int(game_time - (time.time() - start_time))
        if current_time <= 0:
            game_over = True
            game_won = True  

        # --- Управление змейкой --- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_won = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        # --- Обновление Позиции Змейки --- #
        x1 += x1_change
        y1 += y1_change

        # --- Проверка столкновения со стенкой (теперь это проигрыш) --- #
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_over = True

        # Отрисовка фона
        screen.blit(background_img, [0, 0])

        # --- Отображение таймера и счета --- #
        display_timer(current_time)
        display_score(score)

        # --- Отрисовка яблок --- #
        for apple_x, apple_y in apples:
            screen.blit(apple_img, [apple_x, apple_y])

        # --- Обновление тела змейки --- #
        snake_head = [x1, y1]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # --- Проверка столкновения с яблоком --- #
        for i, (apple_x, apple_y) in enumerate(apples):
            if x1 < apple_x + apple_size and x1 + snake_size > apple_x and \
               y1 < apple_y + apple_size and y1 + snake_size > apple_y:
                del apples[i]
                apples.append(generate_apple())
                snake_length += 1
                score += 1
                break

        # --- Проверка столкновения змейки с самой собой (проигрыш) --- #
        for segment in snake_body[:-1]:
            if segment[0] == x1 and segment[1] == y1:
                game_over = True
                break

        # --- Отрисовка змейки --- #
        draw_snake(snake_body)

        pygame.display.update()

        clock.tick(snake_speed)

    # --- Результат игры --- #
    pygame.quit()
    if game_won:
        print("---------------------------------")
        print("Игра окончена!")
        print(f"Собранные яблоки (очки): {score}")
        print("Молодец! :D")
        print("---------------------------------")
    else:
        print("---------------------------------")
        print("Вы проиграли!")
        print(f"Собранные яблоки (счет): {score}")
        print("Плохо! D:")
        print("---------------------------------")
    quit()

# --- Запуск игры --- #
if __name__ == "__main__":
    game_loop()
