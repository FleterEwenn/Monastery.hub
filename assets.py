import pygame

image_size = 64

jay1_sprite = pygame.image.load("assets/ninjas/JAY1/JAY1_head.png")
jay1_head_list = [
    jay1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]
jay1_sprite = pygame.image.load("assets/ninjas/JAY1/JAY1_back.png")
jay1_back_list = [
    jay1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]
jay1_sprite = pygame.image.load("assets/ninjas/JAY1/JAY1_left.png")
jay1_left_list = [
    jay1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]
jay1_sprite = pygame.image.load("assets/ninjas/JAY1/JAY1_right.png")
jay1_right_list = [
    jay1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

def get_jay1()->dict:
    jay1_dict = {}
    jay1_dict['head'] = jay1_head_list
    jay1_dict['back'] = jay1_back_list
    jay1_dict['left'] = jay1_left_list
    jay1_dict['right'] = jay1_right_list
    return jay1_dict

cole1_sprite = pygame.image.load("assets/ninjas/COLE1/COLE1_head.png")
cole1_head_list = [
    cole1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

cole1_sprite = pygame.image.load("assets/ninjas/COLE1/COLE1_back.png")
cole1_back_list = [
    cole1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

cole1_sprite = pygame.image.load("assets/ninjas/COLE1/COLE1_right.png")
cole1_right_list = [
    cole1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

cole1_sprite = pygame.image.load("assets/ninjas/COLE1/COLE1_left.png")
cole1_left_list = [
    cole1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

def get_cole1()->dict:
    cole1_dict = {}
    cole1_dict["head"] = cole1_head_list
    cole1_dict["back"] = cole1_back_list
    cole1_dict["left"] = cole1_left_list
    cole1_dict["right"] = cole1_right_list
    return cole1_dict