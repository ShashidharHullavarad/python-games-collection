import pygame
import random
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
GRID_SIZE = 25
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
INITIAL_FPS = 8
MAX_FPS = 20

# Modern Color Palette
BACKGROUND = (15, 15, 25)
SNAKE_HEAD = (50, 255, 100)
SNAKE_BODY = (40, 200, 80)
SNAKE_GRADIENT = (30, 150, 60)
FOOD_COLOR = (255, 220, 50)
FOOD_GLOW = (255, 240, 100)
TEXT_COLOR = (255, 255, 255)
SCORE_BG = (25, 25, 40)
GAME_OVER_BG = (40, 20, 20)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.length = 3
        self.positions = [((GRID_WIDTH // 2), (GRID_HEIGHT // 2))]
        self.direction = RIGHT
        self.score = 0
        self.game_over = False

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + x) % GRID_WIDTH), (cur[1] + y) % GRID_HEIGHT)
        
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.game_over = True
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 3
        self.positions = [((GRID_WIDTH // 2), (GRID_HEIGHT // 2))]
        self.direction = RIGHT
        self.score = 0
        self.game_over = False

    def render(self, surface):
        for i, p in enumerate(self.positions):
            center_x = p[0] * GRID_SIZE + GRID_SIZE // 2
            center_y = p[1] * GRID_SIZE + GRID_SIZE // 2
            
            if i == 0:
                # Head - larger and brighter
                pygame.draw.circle(surface, SNAKE_HEAD, (center_x, center_y), GRID_SIZE // 2 - 1)
                
                # Eyes based on direction
                eye_offset = 5
                if self.direction == UP:
                    eye1 = (center_x - 4, center_y - 3)
                    eye2 = (center_x + 4, center_y - 3)
                elif self.direction == DOWN:
                    eye1 = (center_x - 4, center_y + 3)
                    eye2 = (center_x + 4, center_y + 3)
                elif self.direction == LEFT:
                    eye1 = (center_x - 3, center_y - 4)
                    eye2 = (center_x - 3, center_y + 4)
                else:  # RIGHT
                    eye1 = (center_x + 3, center_y - 4)
                    eye2 = (center_x + 3, center_y + 4)
                
                pygame.draw.circle(surface, (0, 0, 0), eye1, 3)
                pygame.draw.circle(surface, (0, 0, 0), eye2, 3)
            else:
                # Body with gradient
                ratio = i / max(len(self.positions), 1)
                r = int(SNAKE_BODY[0] + (SNAKE_GRADIENT[0] - SNAKE_BODY[0]) * ratio)
                g = int(SNAKE_BODY[1] + (SNAKE_GRADIENT[1] - SNAKE_BODY[1]) * ratio)
                b = int(SNAKE_BODY[2] + (SNAKE_GRADIENT[2] - SNAKE_BODY[2]) * ratio)
                color = (r, g, b)
                
                radius = int((GRID_SIZE // 2 - 2) * (1 - ratio * 0.3))
                pygame.draw.circle(surface, color, (center_x, center_y), radius)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT
                elif event.key == pygame.K_SPACE and self.game_over:
                    self.reset()

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.pulse = 0
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        self.pulse = 0

    def render(self, surface):
        # Pulsing effect
        self.pulse += 0.12
        pulse_size = int(2 * math.sin(self.pulse))
        
        center_x = self.position[0] * GRID_SIZE + GRID_SIZE // 2
        center_y = self.position[1] * GRID_SIZE + GRID_SIZE // 2
        
        # Outer glow layers
        for i in range(4):
            alpha_surface = pygame.Surface((GRID_SIZE * 2, GRID_SIZE * 2), pygame.SRCALPHA)
            glow_alpha = 40 - i * 8
            glow_color = (*FOOD_GLOW, glow_alpha)
            radius = GRID_SIZE // 2 + 8 - i * 2 + pulse_size
            pygame.draw.circle(alpha_surface, glow_color, (GRID_SIZE, GRID_SIZE), radius)
            surface.blit(alpha_surface, (center_x - GRID_SIZE, center_y - GRID_SIZE))
        
        # Main food circle
        pygame.draw.circle(surface, FOOD_COLOR, (center_x, center_y), GRID_SIZE // 2 - 2 + pulse_size)
        
        # Highlight for 3D effect
        highlight_pos = (center_x - 3, center_y - 3)
        pygame.draw.circle(surface, FOOD_GLOW, highlight_pos, 4)

def draw_ui(surface, score, high_score, game_over, level):
    # Top panel
    panel_height = 70
    panel = pygame.Surface((WINDOW_WIDTH, panel_height), pygame.SRCALPHA)
    pygame.draw.rect(panel, (*SCORE_BG, 220), (0, 0, WINDOW_WIDTH, panel_height))
    surface.blit(panel, (0, 0))
    
    # Fonts
    title_font = pygame.font.Font(None, 52)
    score_font = pygame.font.Font(None, 38)
    small_font = pygame.font.Font(None, 26)
    
    # Title with emoji
    title = title_font.render('🐍 SNAKE', True, SNAKE_HEAD)
    surface.blit(title, (25, 12))
    
    # Level indicator
    level_text = small_font.render(f'Level {level}', True, (150, 255, 150))
    surface.blit(level_text, (25, 48))
    
    # Score
    score_text = score_font.render(f'Score: {score}', True, TEXT_COLOR)
    surface.blit(score_text, (WINDOW_WIDTH - 280, 12))
    
    # High Score
    high_text = small_font.render(f'Best: {high_score}', True, (200, 200, 200))
    surface.blit(high_text, (WINDOW_WIDTH - 280, 48))
    
    # Game Over overlay
    if game_over:
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(overlay, (*GAME_OVER_BG, 200), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        surface.blit(overlay, (0, 0))
        
        game_over_font = pygame.font.Font(None, 80)
        restart_font = pygame.font.Font(None, 40)
        
        game_over_text = game_over_font.render('GAME OVER!', True, (255, 100, 100))
        restart_text = restart_font.render('Press SPACE to Restart', True, TEXT_COLOR)
        final_score = score_font.render(f'Final Score: {score}', True, FOOD_COLOR)
        level_reached = small_font.render(f'Level Reached: {level}', True, (200, 200, 200))
        
        surface.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - 120))
        surface.blit(final_score, (WINDOW_WIDTH // 2 - final_score.get_width() // 2, WINDOW_HEIGHT // 2 - 30))
        surface.blit(level_reached, (WINDOW_WIDTH // 2 - level_reached.get_width() // 2, WINDOW_HEIGHT // 2 + 10))
        surface.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, WINDOW_HEIGHT // 2 + 60))

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('🐍 Snake Game - Progressive Difficulty')
    
    snake = Snake()
    food = Food()
    high_score = 0
    current_fps = INITIAL_FPS
    
    while True:
        snake.handle_keys()
        
        if not snake.game_over:
            snake.update()
            
            # Check if snake ate food
            if snake.get_head_position() == food.position:
                snake.length += 1
                snake.score += 10
                food.randomize_position()
                
                # Progressive difficulty - increase speed every 50 points
                current_fps = min(INITIAL_FPS + (snake.score // 50), MAX_FPS)
                
                # Update high score
                if snake.score > high_score:
                    high_score = snake.score
        else:
            # Reset FPS when game over
            current_fps = INITIAL_FPS
        
        # Calculate current level
        level = (snake.score // 50) + 1
        
        # Drawing
        screen.fill(BACKGROUND)
        
        # Render game objects
        food.render(screen)
        snake.render(screen)
        
        # Draw UI
        draw_ui(screen, snake.score, high_score, snake.game_over, level)
        
        pygame.display.flip()
        clock.tick(current_fps)

if __name__ == '__main__':
    main()
