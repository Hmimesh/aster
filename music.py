    
import pygame
class MusicManager:

    def __init__(self):
        pygame.mixer.init()
        self.power_up_sound = pygame.mixer.Sound('/home/hmimesh/workspace/github.com/hmimesh/Astreoid/sounds/music/sound_effects/Get_item.wav')
        self.explosion_sound = pygame.mixer.Sound('/home/hmimesh/workspace/github.com/hmimesh/Astreoid/sounds/music/sound_effects/asteroid_got_hit.wav')
        self.shooting_sound = pygame.mixer.Sound('/home/hmimesh/workspace/github.com/hmimesh/Astreoid/sounds/music/sound_effects/lazer_firing.wav')
        self.player_got_hit = pygame.mixer.Sound('/home/hmimesh/workspace/github.com/hmimesh/Astreoid/sounds/music/sound_effects/Player_hit.wav')
        
        self.music_loop1 = '/home/hmimesh/workspace/github.com/hmimesh/Astreoid/sounds/music/Music_loop.wav'
        self.music_loop2 = '/home/hmimesh/workspace/github.com/hmimesh/Astreoid/sounds/music/Music_loop2.wav'
        self.music_loop3 = '/home/hmimesh/workspace/github.com/hmimesh/Astreoid/sounds/music/Music_loop3.wav'
        self.power_up_music = '/home/hmimesh/workspace/github.com/hmimesh/Astreoid/sounds/music/Power_up.wav'
        
        self.current_music = None
        self.power_up_active = False

    def play_music(self, music_track):
        pygame.mixer.music.load(music_track)
        pygame.mixer.music.play(-1)
        self.current_music = music_track
    
    def stop_music(self):
        pygame.mixer.music.stop()

    def switch_music(self, score):
        if self.power_up_active:
            return 
        elif score < 1000:
            new_music = self.music_loop1
        elif 1000 <= score < 4500:
            new_music = self.music_loop2
        else:
            new_music = self.music_loop3

        if self.current_music != new_music:
            self.play_music(new_music) 


    def play_power_up_sound(self, ):
        self.power_up_active = True
        pygame.mixer.music.load(self.power_up_music)
        pygame.mixer.music.play(-1)

    def stop_power_up_music(self, score):
        """Stops power-up music and resumes background music based on the score."""
        self.power_up_active = False
        self.switch_music(score)

    def play_explosion_sound(self):
        self.explosion_sound.play()

    def play_shooting_sound(self):
        self.shooting_sound.play()

    def play_player_hit_sound(self):
        self.player_got_hit.play()

    def resume_music(self, score):
        self.power_up_active = False
        self.switch_music(score)