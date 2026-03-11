#Projet : monastery.hub
#Auteurs : Ewenn Fleter, Raphael Kermes

import subprocess
import sys
import pygame
from player import Player
from assets.assets import get_ewenn, get_raph
import webbrowser
from pathlib import Path

pygame.init()

chemin = Path(__file__).resolve().parent

window = pygame.display.set_mode((1000, 667))

shuriken_original = pygame.image.load(chemin / "assets" / "logo" / "shuriken_dim.png")
x_shuriken = -100
y_shuriken = 300
angle = 0

logo = pygame.image.load(chemin / "assets" / "logo" / "logo_black_dim.png")
logo_fond = pygame.image.load(chemin / "assets" / "logo" / "logo_monastery_dim.png")

run_anim = True
run_game = False
run_menu = False

shuriken = pygame.transform.rotate(shuriken_original, angle)
rect = shuriken.get_rect(center=(x_shuriken, y_shuriken))

clock = pygame.time.Clock()
timer = 0

opacity_logo = 0

while run_anim:
    dt = clock.tick(120)
    timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_anim = False

    window.fill((0, 0, 0))

    window.blit(shuriken, rect)

    if x_shuriken <= 500:
        shuriken = pygame.transform.rotate(shuriken_original, angle)
        x_shuriken += 3
        angle += 6
        rect = shuriken.get_rect(center=(x_shuriken, y_shuriken))
        timer = 0
    else:
        shuriken = shuriken_original
    
        if timer >= 300:
            opacity_logo += 1
            logo.set_alpha(opacity_logo)

            window.blit(logo, rect)
        
        if timer >= 3000:
            window.blit(logo_fond, rect)
        
        if timer >= 5000:
            run_menu = True
            run_anim = False

    pygame.display.flip()


fond = pygame.image.load(chemin / "assets" / "maps" / "bg_acc_pixelisé_dim.png")

btn_start = pygame.image.load(chemin / "assets" / "accueil" / "start_button-1.png")

clock = pygame.time.Clock()
timer = 0

ewenn_frames = get_ewenn()["idle"]
raph_frames = get_raph()["idle"]
index_frame = 0

btn_rect = pygame.Rect(280, 226, 410, 107)

while run_menu:
    dt = clock.tick(30)
    timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_menu = False
    
    if timer >= 300:
        index_frame = (index_frame+1)%2
        timer = 0

    window.fill((0, 0, 0))

    window.blit(fond, (0, 0))

    window.blit(btn_start, (250, 100))

    window.blit(ewenn_frames[index_frame], (300, 162))
    window.blit(raph_frames[index_frame], (600, 162))

    if pygame.mouse.get_pos()[0] >= btn_rect.left and pygame.mouse.get_pos()[0] <= btn_rect.right \
    and pygame.mouse.get_pos()[1] >= btn_rect.top and pygame.mouse.get_pos()[1] <= btn_rect.bottom \
    and pygame.mouse.get_pressed()[0]:
        run_game = True
        run_menu = False

    #pygame.draw.rect(window, (255, 0, 0), btn_rect, 1)
    
    pygame.display.flip()

player = Player()
list_module = [pygame.Rect(750, 100, 115, 120), pygame.Rect(740, 430, 135, 110), pygame.Rect(130, 100, 115, 120), pygame.Rect(120, 435, 140, 110)]

draw_char = False

def run_checkpassword():
    subprocess.Popen([sys.executable, chemin / "CheckPassword.py"])

def run_minilangage():
    subprocess.Popen([sys.executable, chemin / "minilangage" / "minilangage.py"])

def run_quiz():
    webbrowser.open(chemin / "quiz-lego" / "index.html")

def run_hexa():
    subprocess.Popen([sys.executable, chemin / "conversion_binaire_hexa"/"conversion_binaire_hexa.py"])

bgimage = pygame.image.load(chemin / "assets"/ "maps" / "proto4,2.png")
setimage = pygame.image.load(chemin / "assets" / "setting" / "setting_petit.png")
x = 930
y = 0

jay2_ico = pygame.image.load(chemin / "assets" / "ninjas" / "JAY2" /"JAY2_icon.png")
jay1_ico = pygame.image.load(chemin / "assets"/ "ninjas" / "JAY1" / "JAY1_icon.png")
cole_ico = pygame.image.load(chemin / "assets" / "ninjas" / "COLE1" / "COLE1_icon.png")
kai_ico = pygame.image.load(chemin / "assets" / "ninjas" / "KAI1" / "KAI1_icon.png")
lloyd_ico = pygame.image.load(chemin / "assets" / "ninjas" / "LLOYD1" / "LLOYD1_icon.png")
wu_ico = pygame.image.load(chemin / "assets" / "ninjas" / "WU1" / "WU1_icon.png")
zane_ico = pygame.image.load(chemin / "assets" / "ninjas" / "ZANE1" / "ZANE1_icon.png")
nya_ico = pygame.image.load(chemin / "assets" / "ninjas" / "NYA1" / "NYA1_icon.png")

clock = pygame.time.Clock()
timer = 0

while run_game:
    dt = clock.tick(60)
    timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    
    player.update(dt)
    
    window.blit(bgimage, (0, 0))
    window.blit(setimage, (x, y))

    if player.rect.x + player.rect.width >= 450 and player.rect.x <= 550 and player.rect.y <= 110:
        run_game = False

    for i in range(len(list_module)):
        # pygame.draw.rect(window, (0, 255, 0), list_module[i], 3)

        if player.rect.left <= list_module[i].right and player.rect.right >= list_module[i].left \
        and player.rect.bottom >= list_module[i].top and player.rect.top <= list_module[i].bottom :
            if i == 0:
                run_checkpassword()
            if i == 1:
                run_minilangage()
            if i == 2:
                run_quiz()
            if i == 3:
                run_hexa()
            player.reset_pos()
    
    if player.rect.right >= 940:
        player.rect.x = 940 - player.rect.width
    if player.rect.left <= 60:
        player.rect.x = 60
    if player.rect.top <= 110:
        player.rect.y = 110
    if player.rect.bottom >= 565:
        player.rect.y = 565 - player.rect.height

    if draw_char:
        window.blit(jay1_ico, (945, 20+64))
        window.blit(kai_ico, (945, 20+2*64))
        window.blit(cole_ico, (945, 20+3*64))
        window.blit(lloyd_ico, (945, 20+4*64))
        window.blit(wu_ico, (945, 20+5*64))
        window.blit(zane_ico, (945, 20+6*64))
        window.blit(jay2_ico, (945, 20+7*64))
        window.blit(nya_ico, (945, 20+8*64))

        if pygame.mouse.get_pos()[0] >= 936 and pygame.mouse.get_pos()[0] <= 1000:

            for i in range(1, 9):
                if pygame.mouse.get_pos()[1] >= 64*i and pygame.mouse.get_pos()[1] <= 64*(i+1) \
                  and pygame.mouse.get_pressed()[0] and timer >= 200:
                    timer = 0
                    player.change_perso(i)
    
    if pygame.mouse.get_pos()[0] >= 936 and pygame.mouse.get_pos()[0] <= 1000 \
      and pygame.mouse.get_pos()[1] >= 0 and pygame.mouse.get_pos()[1] <= 64:
        setimage = pygame.image.load(chemin / "assets" / "setting" / "setting_grand.png")
        x = 926
        y = -4

        if pygame.mouse.get_pressed()[0] and timer >= 200:
            timer = 0
            draw_char = not draw_char
    
    else:
        setimage = pygame.image.load(chemin / "assets" / "setting" / "setting_petit.png")
        x = 930
        y = 0

    player.draw(window)

    pygame.display.flip()

pygame.quit()