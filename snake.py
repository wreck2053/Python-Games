import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
display_width = 800
display_height = 600

# Set size of snake blocks and snake speed
block_size = 10
snake_speed = 15

# Create the display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

# Clock to control game speed
clock = pygame.time.Clock()

# Define the font
font_style = pygame.font.SysFont(None, 50)


# Function to display score
def your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    game_display.blit(value, [0, 0])


# Function to create the snake
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], block_size, block_size])


# Function to display a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])


# Function to run the game
def game_loop():
    game_over = False
    game_close = False

    # Snake initial position
    lead_x = display_width / 2
    lead_y = display_height / 2

    # Snake movement speed
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Initial position of food
    food_x = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            game_display.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if (
            lead_x >= display_width
            or lead_x < 0
            or lead_y >= display_height
            or lead_y < 0
        ):
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(blue)
        pygame.draw.rect(game_display, green, [food_x, food_y, block_size, block_size])
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(block_size, snake_list)
        your_score(snake_length - 1)

        pygame.display.update()

        if lead_x == food_x and lead_y == food_y:
            food_x = (
                round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            )
            food_y = (
                round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            )
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
