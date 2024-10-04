import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collides_with(self, other):
        if hasattr(other, 'position'):
            distance = self.position.distance_to(other.position)
            return distance <= (self.radius + other.radius)
    
        elif hasattr(other, 'rect'):
            closest_x = max(other.rect.left, min(self.position.x, other.rect.right))
            closest_y = max(other.rect.top, min(self.position.y, other.rect.bottom))
        
            distance = pygame.Vector2(closest_x, closest_y).distance_to(self.position)
        
            return distance <= self.radius
    
        return False
