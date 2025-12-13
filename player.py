import pygame
from assets import get_jay1

class Player:
    def __init__(self):
        self.image_index = 0
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
            self.image_index = (self.image_index + 1)%6
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
            self.frame = self.all_frames['head'][self.image_index]
        elif keys[pygame.K_UP]:
            self.rect.y -= 5
            self.frame = self.all_frames['back'][self.image_index]
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.frame = self.all_frames['left'][self.image_index]
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.frame = self.all_frames['right'][self.image_index]
        else :
            self.frame = self.all_frames['head'][0]
    
    def draw(self, surface:pygame.Surface):
        surface.blit(self.frame, (self.rect.x, self.rect.y))
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 1)
    
    def change_perso(self, id:int):
        if id == 1:
            self.all_frames = get_jay1()
            print('changement de personnage')