import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *
from power_up import PowerUp
import random
from ui.ui import *
from explosion import Explosion, load_explosion_images

explosion_anim = load_explosion_images()

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
power_ups = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers =(asteroids, updatable, drawable)
AsteroidField.containers =(updatable,)
Shot.containers = (updatable, drawable, shots)
PowerUp.containers = (updatable, drawable, power_ups)


def handle_collisions(player, asteroids, shots, power_ups, ui_manager):
    global score, high_score
    
    # Player vs Power-ups
    for power_up in power_ups:
        if player.collides_with(power_up):
            score += 50
            player.activate_mega_lazer()
            ui_manager.add_message(
                f"{power_up}! Use it quickly! {player.mega_lazer}",
                (1000, 10),
                duration = 5
            )
            ui_manager.message_display_time = player.mega_lazer
            power_up.kill()
            
            if score > high_score:
                high_score = score
                write_high_score("high_score.txt", high_score)
                print(f"New high score: {high_score}")

    # Player vs Asteroids
    for asteroid in asteroids:
        if player.can_collide() and player.collides_with(asteroid):
            global lives
            lives -= 1
            player.kill()  # This removes the player from all groups
            expl = Explosion(player.rect.center, 'lg', explosion_anim)
            updatable.add(expl)
            drawable.add(expl)

            if lives > 0:
                # Respawn the player at the center
                player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                
                # Re-add the player to the sprite groups
                updatable.add(player)
                drawable.add(player)
                
                print(f"Player respawned at center with {lives} lives remaining.")
            elif lives == 0:
                print("GAME OVER!")
                sys.exit()


        # Shots vs Asteroids
        for shot in shots:
            if asteroid.collides_with(shot):
                shot.kill()  # Also remove the shot that hit
                asteroid.split()
                score += 100
                expl = Explosion(asteroid.rect.center, 'lg', explosion_anim)
                updatable.add(expl)
                drawable.add(expl)
                
            if score > high_score:
                high_score = score
                write_high_score("high_score.txt", high_score)
                print(f"New high score: {high_score}")

def remove_offscreen_objects(shots, power_ups, screen_width, screen_height):
    # Remove off-screen shots
    for shot in shots:
        if shot.is_off_screen():
            shot.kill()

    # Remove off-screen power-ups
    for power_up in power_ups:
        if power_up.is_off_screen(screen_height):
            power_up.kill()


def main():
    global score, high_score, lives
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    high_score = read_high_score("high_score.txt")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_fields = AsteroidField()
    power_up_timer = 0
    power_up_spawn_interval = random.randrange(5, 15)
    ui_manager = UIManager()
    handle_collisions(player, asteroids, shots, power_ups, ui_manager)
    
    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        delta_time = clock.get_time()

        screen.fill((0, 0, 0,))
        
        ui_manager.update(delta_time)
        ui_manager.render(screen)

        render_text(screen, GAME_NAME, (10,10))
        render_text(screen, f"score:{score}", (10, 50))
        render_text(screen, f"live : {lives}", (10, 90))
        render_text(screen, f"high score: {high_score} !", (500, 10))
        

        power_up_timer += dt

        # Spawn Power-ups
        if power_up_timer >= power_up_spawn_interval:
            PowerUp(SCREEN_WIDTH, SCREEN_HEIGHT)
            power_up_timer = 0
            power_up_spawn_interval = random.randrange(5, 25)

        # Update all updatable sprites
        for thing in updatable:
            thing.update(dt)

        # Handle collisions
        handle_collisions(player, asteroids, shots, power_ups, ui_manager)

        # Remove off-screen shots and power-ups
        remove_offscreen_objects(shots, power_ups, SCREEN_WIDTH, SCREEN_HEIGHT)

        # Draw all drawable sprites
        for thing in drawable:
            thing.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Frame time in seconds

    pygame.quit()

if __name__ == "__main__":
    main()