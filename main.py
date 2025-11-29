import subprocess
import sys
import pygame
from player import Player

pygame.init()

window = pygame.display.set_mode((1000, 667))

player = Player()

run = True

def run_checkpassword():
    subprocess.Popen([sys.executable, "CheckPassword.py"])

bgimage = pygame.image.load("assets/maps/bgimageR.png")

clock = pygame.time.Clock()

while run:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
    
    player.update(dt)
    
    window.blit(bgimage, (0, 0))

    player.draw(window)

    pygame.display.flip()