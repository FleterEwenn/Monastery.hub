import subprocess
import sys
import pygame
from player import Player

pygame.init()

window = pygame.display.set_mode((1000, 667))

player = Player()
list_module = [pygame.Rect(690, 360, 70, 60), pygame.Rect(720, 200, 75, 75), pygame.Rect(525, 450, 75, 75), pygame.Rect(280, 400, 75, 60)]

run = True
draw_char = False

def run_checkpassword():
    subprocess.Popen([sys.executable, "CheckPassword.py"])

bgimage = pygame.image.load("assets/maps/bgimageR.png")
setimage = pygame.image.load("assets/setting.png")

jay2_ico = pygame.image.load("assets/ninjas/JAY2/JAY2_icon.png")
jay1_ico = pygame.image.load("assets/ninjas/JAY1/JAY1_icon.png")
cole_ico = pygame.image.load("assets/ninjas/COLE1/COLE1_icon.png")
kai_ico = pygame.image.load("assets/ninjas/KAI1/KAI1_icon.png")
lloyd_ico = pygame.image.load("assets/ninjas/LLOYD1/LLOYD1_icon.png")
wu_ico = pygame.image.load("assets/ninjas/WU1/WU1_icon.png")
zane_ico = pygame.image.load("assets/ninjas/ZANE1/ZANE1_icon.png")

clock = pygame.time.Clock()
timer = 0

while run:
    dt = clock.tick(60)
    timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    player.update(dt)
    
    window.blit(bgimage, (0, 0))
    window.blit(setimage, (936, 0))

    for i in range(len(list_module)):
        #pygame.draw.rect(window, (0, 255, 0), list_module[i], 1)

        if player.rect.left <= list_module[i].right and  player.rect.right >= list_module[i].left \
        and player.rect.bottom >= list_module[i].top and player.rect.top <= list_module[i].bottom :
            if i == 0:
                run_checkpassword()
            player.reset_pos()
    
    if draw_char:
        window.blit(jay1_ico, (936, 64))
        window.blit(kai_ico, (936, 2*64))
        window.blit(cole_ico, (936, 3*64))
        window.blit(lloyd_ico, (936, 4*64))
        window.blit(wu_ico, (936, 5*64))
        window.blit(zane_ico, (936, 6*64))
        window.blit(jay2_ico, (936, 7*64))

        if pygame.mouse.get_pos()[0] >= 936 and pygame.mouse.get_pos()[0] <= 1000:

            for i in range(1, 8):
                if pygame.mouse.get_pos()[1] >= 64*i and pygame.mouse.get_pos()[1] <= 64*(i+1) \
                  and pygame.mouse.get_pressed()[0] and timer >= 200:
                    timer = 0
                    player.change_perso(i)

    
    if pygame.mouse.get_pos()[0] >= 936 and pygame.mouse.get_pos()[0] <= 1000 \
      and pygame.mouse.get_pos()[1] >= 0 and pygame.mouse.get_pos()[1] <= 64 \
      and pygame.mouse.get_pressed()[0] and timer >= 200:
        timer = 0
        draw_char = not draw_char

    player.draw(window)

    pygame.display.flip()