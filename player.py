from circleshape import *
from constants import *
import pygame 
from shot import Shot
import random
class Player (CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.rotational_velocity = 0
        self.velocity = pygame.Vector2(0, 0)
        self.timer = 0
        self.mega_lazer = 0
        self.screen_h = SCREEN_HEIGHT
        self.screen_w = SCREEN_WIDTH
        
# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            2
            )
    def rotate(self, direction, dt):
        self.rotational_velocity += direction * PLAYER_TURN_SPEED * dt

    def move(self, direction, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * direction * PLAYER_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        if self.mega_lazer > 0:
            self.mega_lazer -= dt 
            if self.mega_lazer < 0:
                self.mega_lazer = 0
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(1, dt)
        if keys[pygame.K_w]:
            self.move(1, dt)
        if keys[pygame.K_s]:
            self.move(-1, dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
        self.rotation += self.rotational_velocity * dt
        self.rotational_velocity *= 0.99 
        self.position += self.velocity * dt
        self.velocity *= 0.99
        self.is_off_screen()

    def shoot(self):
        if self.mega_lazer > 0:
            lazer_color = random.choice(RAINBOW_COLORS)
            shot = Shot(self.position.x, self.position.y, color = lazer_color)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOTS_SPEED
            self.timer = PLAYER_SHOTS_COOLDOWN
    
        else:
            lazer_color =(255, 255, 0)
        if self.timer > 0:
            return f"oh no we need to wait:{self.timer}"
        if self.timer < 0: 
            shot = Shot(self.position.x, self.position.y, color = lazer_color)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOTS_SPEED
            self.timer = PLAYER_SHOTS_COOLDOWN
    
    def activate_mega_lazer(self):
        self.mega_lazer += 5
        if self.mega_lazer > 15:
            self.mega_lazer = 15  

    def is_off_screen(self):
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH 

        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0  
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT 
