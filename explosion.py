import pygame as pg
from constants import *

class Explosion(pg.sprite.Sprite):
    def __init__(self, center, size, explosion_anim):
        pg.sprite.Sprite.__init__(self)
        self.size = size
        self.explosion_anim = explosion_anim  # Store the passed animation
        self.image = self.explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50  # Adjust this for the speed of the animation

    def update(self):
        # Handle the animation frames
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim[self.size]):
                self.kill()  # Remove the sprite after the animation finishes
            else:
                center = self.rect.center  # Keep the center consistent
                self.image = self.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Function to load images for explosion animations
def load_explosion_images():
    explosion_anim = {'lg': [], 'sm': []}
    for i in range(8):
        filename = f'regularExplosion0{i}.png'
        img = pg.image.load('regularExplosion00.png').convert()
        img.set_colorkey("BLACK")  # Set transparency

        # Large explosion
        img_lg = pg.transform.scale(img, (75, 75))
        explosion_anim['lg'].append(img_lg)

        # Small explosion
        img_sm = pg.transform.scale(img, (32, 32))
        explosion_anim['sm'].append(img_sm)

    return explosion_anim

# Example method to handle collisions and create explosions
def handle_trump_hits(trump, projectiles, all_sprites, explosion_anim):
    trump_hits = pg.sprite.spritecollide(trump, projectiles, True)
    for hit in trump_hits:
        print("TRUMP HIT!!!")
        expl = Explosion(hit.rect.center, 'lg', explosion_anim)
        all_sprites.add(expl)  # Add the explosion to the all_sprites group
