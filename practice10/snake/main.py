import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Window and grid settings
WIDTH = 800
HEIGHT = 600
CELL = 40
FOOD_SIZE = int(CELL * 1.3)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Fonts
font = pygame.font.SysFont("Verdana", 24)
game_over_font = pygame.font.SysFont("Verdana", 48)

# Load images
background_img = pygame.image.load("assets/images/background.png").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

head_img = pygame.image.load("assets/images/head.png").convert_alpha()
head_img = pygame.transform.scale(head_img, (CELL, CELL))

body_img = pygame.image.load("assets/images/body.png").convert_alpha()
body_img = pygame.transform.scale(body_img, (CELL, CELL))

food_img = pygame.image.load("assets/images/food.png").convert_alpha()

# Snake start position
snake = [
    [200, 200],
    [160, 200],
    [120, 200]
]

# Start direction
dx = CELL
dy = 0

# Score, level, speed
score = 0
level = 1
speed = 3

FOOD_LIFETIME = 7000  # 7 seconds in milliseconds

# Generate food with random weight and timer
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if [x, y] not in snake:
            value = random.choice([1, 3, 5, 10])          # Different weights
            spawn_time = pygame.time.get_ticks()
            return [x, y, value, spawn_time]

# Show game over screen
def show_game_over():
    screen.blit(background_img, (0, 0))

    game_over_text = game_over_font.render("Game Over", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    level_text = font.render(f"Final Level: {level}", True, WHITE)

    screen.blit(game_over_text, game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
    screen.blit(score_text, score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
    screen.blit(level_text, level_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 45)))

    pygame.display.update()
    pygame.time.delay(2000)

# First food
food = generate_food()

# Main game loop
while True:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Change direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx = -CELL
                dy = 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = CELL
                dy = 0
            elif event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -CELL
            elif event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = CELL

    # Check if current food expired
    if current_time - food[3] > FOOD_LIFETIME:
        food = generate_food()

    # Current head
    head_x, head_y = snake[0]

    # New head
    new_head = [head_x + dx, head_y + dy]

    # Border collision
    if (new_head[0] < 0 or new_head[0] >= WIDTH or 
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        show_game_over()
        pygame.quit()
        sys.exit()

    # Check if food is eaten
    ate_food = (new_head[0] == food[0] and new_head[1] == food[1])

    # Self collision
    if ate_food:
        if new_head in snake:
            show_game_over()
            pygame.quit()
            sys.exit()
    else:
        if new_head in snake[:-1]:
            show_game_over()
            pygame.quit()
            sys.exit()

    # Move snake
    snake.insert(0, new_head)

    if ate_food:
        score += food[2]                    # Add food's weight (value)
        food = generate_food()
    else:
        snake.pop()

    # Update level and speed
    level = score // 5 + 1                  # Changed to 5 for better pacing
    speed = 10 + (level - 1) * 2

    # Draw background
    screen.blit(background_img, (0, 0))

    # Draw snake
    for i, segment in enumerate(snake):
        if i == 0:
            screen.blit(head_img, (segment[0], segment[1]))
        else:
            screen.blit(body_img, (segment[0], segment[1]))

    # Draw food with size based on value + shrinking effect near expiration
    age = current_time - food[3]
    life_ratio = max(0.5, 1 - (age / FOOD_LIFETIME))   # shrink when almost expired

    current_size = int(FOOD_SIZE * life_ratio)
    scaled_food = pygame.transform.scale(food_img, (current_size, current_size))

    draw_x = food[0] - (current_size - CELL) // 2
    draw_y = food[1] - (current_size - CELL) // 2

    screen.blit(scaled_food, (draw_x, draw_y))

    # Draw score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()
    clock.tick(speed)