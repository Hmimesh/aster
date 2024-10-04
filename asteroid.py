from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        
        colors = ["red", "green", "blue"]

        self.color= random.choice(colors)

    def draw(self, screen):
        # Assuming self.position is a pygame.Vector2
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.position.x), int(self.position.y)),  # Correctly access position
            int(self.radius),
            2
        )
    
    def update(self, dt):
        # Update the position using velocity
        self.position += self.velocity * dt  # Assuming self.position is a Vector2
