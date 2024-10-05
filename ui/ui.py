import pygame
pygame.font.init()

def read_high_score(filepath):
    try:
        with open(filepath, 'r') as file:
            high_score = int(file.read())
            return high_score
    except FileNotFoundError:
        return 0
    
def write_high_score(filepath, high_score):
    with open(filepath,'w') as file:
        file.write(str(high_score))
    


lives = 3
score = 0
high_score = read_high_score("high_score.txt")
message_display_time =  0
message_time_remaining = 0
last_live_score = 0
message_shown = False
def get_high_score (high_score, score):
    if score > high_score:
        high_score =  score
        write_high_score("high_score.txt", high_score)
    else:
        return high_score 
    
class UIManager:
    def __init__(self):
        self.messages = []
    
    def add_message(self, text, position, duration):
        self.messages.append(
            {
            "text": text,
            "position": position,
            "remaining": duration
            }
        )
        return self.messages
    
    def update(self, delta_time):
        for message in self.messages:
            message["remaining"] -= delta_time


        self.messages = [m for m in self.messages if m["remaining"] > 0]
            
    def render(self, screen):
        for message in self.messages:
            render_text(screen,
                        message["text"],
                        message["position"]
                    )



def render_text(
        screen,
        text,
        position,
        font_size =30,
        outline_color = (255, 255,255),
        inside_color = (0, 0, 0),
        outline_thickness = 2
        ):
    #first the regular font
    font = pygame.font.Font(None, font_size)
    #no lets init the outline text by rendering it!
    outline_text = font.render(text, True, outline_color)

    for offset_x in range(-outline_thickness, outline_thickness + 1):
        for offset_y in range(-outline_thickness, outline_thickness + 1):
             if offset_x != 0 or offset_y != 0:
                screen.blit(outline_text, (position[0] + offset_x, position[1] + offset_y))    
    inside_text = font.render(text, True, inside_color)

    screen.blit(inside_text, position)
