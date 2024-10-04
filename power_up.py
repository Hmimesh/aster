import pygame
import random
from constants import *



class PowerUp(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__(PowerUp.containers)  # Ensure it's added to the containers
        self.width = 35 
        x = random.randint(0, screen_width - self.width)
        y = random.choice([0, screen_height])
        self.rect = pygame.Rect(x, y, self.width, self.width)
        self.speed = random.uniform(50, 100)
        self.direction = 1 if y == 0 else -1
        self.color_index = random.randint(0, len(RAINBOW_COLORS) - 1)
        self.color_change_speed = 0.1
        print(f"PowerUp created at ({self.rect.x}, {self.rect.y}), direction: {self.direction}")

    def update(self, dt):
        # Move the power-up vertically
        self.rect.y += self.speed * self.direction * dt
        self.color_index = (self.color_index + self.color_change_speed) % len(RAINBOW_COLORS)
        print(f"PowerUp moved to y={self.rect.y}")

    def draw(self, screen):
        color = RAINBOW_COLORS[int(self.color_index)]
        pygame.draw.rect(screen, color, self.rect)
        print(f"Drawing PowerUp at ({self.rect.x}, {self.rect.y})")

    def is_off_screen(self, screen_height):
        return self.rect.bottom < 0 or self.rect.top > screen_height
