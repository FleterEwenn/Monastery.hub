import pygame
from assets import get_jay1, get_cole1, get_kai1, get_jay2, get_wu1, get_lloyd1, get_nya1, get_zane1

class Player:
    def __init__(self):
        self.image_index = 0
        self.direction = "head"
        self.all_frames = get_jay1()
        self.frame = self.all_frames['head'][self.image_index]
        self.rect = pygame.Rect(455, 280, 64, 64)
        self.frame_timer = 0
    
    def reset_pos(self):
        self.rect.x = 455
        self.rect.y = 280
    
    def update(self, dt:int):
        self.frame_timer += dt

        if self.frame_timer >= 100:
            self.frame_timer = 0
            self.image_index = (self.image_index + 1) % 6
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.rect.y += 3
            self.frame = self.all_frames['head'][self.image_index]
            self.direction = "head"
        elif keys[pygame.K_UP]:
            self.rect.y -= 3
            self.frame = self.all_frames['back'][self.image_index]
            self.direction = "back"
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 3
            self.frame = self.all_frames['left'][self.image_index]
            self.direction = "head"
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 3
            self.frame = self.all_frames['right'][self.image_index]
            self.direction = "head"
        else :
            if self.direction == "head" :
                self.frame = self.all_frames['idle'][0]
            elif self.direction == "back":
                self.frame = self.all_frames['idle'][1]
    
    def draw(self, surface:pygame.Surface):
        surface.blit(self.frame, (self.rect.x, self.rect.y))
        #pygame.draw.rect(surface, (255, 0, 0), self.rect, 1)
    
    def change_perso(self, id:int):
        if id == 1:
            self.all_frames = get_jay1()
        elif id == 2:
            self.all_frames = get_kai1()
        elif id == 3:
            self.all_frames = get_cole1()
        elif id == 4:
            self.all_frames = get_lloyd1()
        elif id == 5:
            self.all_frames = get_wu1()
        elif id == 6:
            self.all_frames = get_zane1()
        elif id == 7:
            self.all_frames = get_jay2()
        elif id == 8:
            self.all_frames = get_nya1()