import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys
from shot import *
from power_up import PowerUp
import random
from ui.ui import *
from music import MusicManager

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
current_music = None
power_up_active = False

def handle_collisions(player, asteroids, shots, power_ups, ui_manager, music_manager):
    global score, high_score, power_up_active, lives, last_live_score, message_shown
    # Player vs Power-ups
    for power_up in power_ups:
        if player.collides_with(power_up):
            if player.mega_lazer <= 0:
                music_manager.stop_power_up_music(score)
            score += 50
            player.activate_mega_lazer()
            ui_manager.add_message(
                f"{power_up}! Use it quickly! {player.mega_lazer}",
                (1000, 10),
                duration = 5
            )
            ui_manager.add_message(f"{player.mega_lazer}", (10, 40), player.mega_lazer)
            power_up.kill()
            music_manager.play_power_up_sound()
            power_up_active = True
            if score > high_score:
                high_score = score
                write_high_score("high_score.txt", high_score)
                print(f"New high score: {high_score}")

    # Player vs Asteroids
    for asteroid in asteroids:
        if player.can_collide() and player.collides_with(asteroid):
            lives -= 1
            player.kill()  # This removes the player from all groups
            music_manager.play_player_hit_sound()
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
                music_manager.play_explosion_sound()

            if score > high_score:
                high_score = score
                write_high_score("high_score.txt", high_score)
                print(f"New high score: {high_score}")
                
            if score % 5000 == 0 and score > 0 and score != last_live_score:
                lives += 1
                last_live_score = score 


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
    global score, high_score, message_shown
    pygame.init()
    pygame.mixer.init()
    music_manager = MusicManager()
    music_manager.play_music(music_manager.music_loop1)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    high_score = read_high_score("high_score.txt")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_fields = AsteroidField()
    power_up_timer = 0
    power_up_spawn_interval = random.randrange(5, 15)
    ui_manager = UIManager()
   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        delta_time = clock.get_time()

        screen.fill((0, 0, 0,))

        if score >= 500 and not message_shown:
            ui_manager.add_message("You've reached 500 points!", (500, 100), 3)
            message_shown = True
        ui_manager.update(delta_time)
        ui_manager.render(screen)   

        render_text(screen, GAME_NAME, (10,10))
        render_text(screen, f"score:{score}", (10, 50))
        render_text(screen, f"live : {lives}", (10, 90))
        render_text(screen, f"high score: {high_score} !", (500, 10))
        
        music_manager.switch_music(score)
        power_up_timer += dt
        
        if player.mega_lazer == 0 and music_manager.power_up_active:
            music_manager.stop_power_up_music(score)
        
        # Spawn Power-ups
        if power_up_timer >= power_up_spawn_interval:
            PowerUp(SCREEN_WIDTH, SCREEN_HEIGHT)
            power_up_timer = 0
            power_up_spawn_interval = random.randrange(5, 25)

        # Update all updatable sprites
        for thing in updatable:
            thing.update(dt)

        # Handle collisions
        handle_collisions(player, asteroids, shots, power_ups, ui_manager, music_manager)
        
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