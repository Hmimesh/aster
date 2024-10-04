import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, color =[255,255,0]):
        super().__init__(x, y, SHOT_RADIUS)
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.is_off_screen()
    
    def is_off_screen(self):
        self.position.x < 0 or self.position.x > SCREEN_WIDTH
        self.position.y < 0 or self.position.y > SCREEN_HEIGHT