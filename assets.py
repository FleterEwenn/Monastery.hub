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

jay1_sprite = pygame.image.load("assets/ninjas/JAY1/JAY1_idle.png")
jay1_idle_list = [
    jay1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(2)
]

def get_jay1()->dict:
    jay1_dict = {}
    jay1_dict['head'] = jay1_head_list
    jay1_dict['back'] = jay1_back_list
    jay1_dict['left'] = jay1_left_list
    jay1_dict['right'] = jay1_right_list
    jay1_dict['idle'] = jay1_idle_list
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

cole1_sprite = pygame.image.load("assets/ninjas/COLE1/COLE1_idle.png")
cole1_idle_list = [
    cole1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(2)
]


def get_cole1()->dict:
    cole1_dict = {}
    cole1_dict["head"] = cole1_head_list
    cole1_dict["back"] = cole1_back_list
    cole1_dict["left"] = cole1_left_list
    cole1_dict["right"] = cole1_right_list
    cole1_dict["idle"] = cole1_idle_list
    return cole1_dict

kai1_sprite = pygame.image.load("assets/ninjas/KAI1/KAI1_head.png")
kai1_head_list = [
    kai1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

kai1_sprite = pygame.image.load("assets/ninjas/KAI1/KAI1_back.png")
kai1_back_list = [
    kai1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

kai1_sprite = pygame.image.load("assets/ninjas/KAI1/KAI1_left.png")
kai1_left_list = [
    kai1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

kai1_sprite = pygame.image.load("assets/ninjas/KAI1/KAI1_right.png")
kai1_right_list = [
    kai1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

kai1_sprite = pygame.image.load("assets/ninjas/KAI1/KAI1_idle.png")
kai1_idle_list = [
    kai1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(2)
]

def get_kai1()->dict:
    kai1_dict = {}
    kai1_dict["head"] = kai1_head_list
    kai1_dict["back"] = kai1_back_list
    kai1_dict["right"] = kai1_right_list
    kai1_dict["left"] = kai1_left_list
    kai1_dict["idle"] = kai1_idle_list
    return kai1_dict

jay2_sprite = pygame.image.load("assets/ninjas/JAY2/JAY2_head.png")
jay2_head_list = [
    jay2_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]
jay2_sprite = pygame.image.load("assets/ninjas/JAY2/JAY2_back.png")
jay2_back_list = [
    jay2_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]
jay2_sprite = pygame.image.load("assets/ninjas/JAY2/JAY2_left.png")
jay2_left_list = [
    jay2_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]
jay2_sprite = pygame.image.load("assets/ninjas/JAY2/JAY2_right.png")
jay2_right_list = [
    jay2_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

jay2_sprite = pygame.image.load("assets/ninjas/JAY2/JAY2_idle.png")
jay2_idle_list = [
    jay2_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(2)
]


def get_jay2()->dict:
    jay2_dict = {}
    jay2_dict['head'] = jay2_head_list
    jay2_dict['back'] = jay2_back_list
    jay2_dict['left'] = jay2_left_list
    jay2_dict['right'] = jay2_right_list
    jay2_dict['idle'] = jay2_idle_list
    return jay2_dict

wu1_sprite = pygame.image.load("assets/ninjas/WU1/WU1_head.png")
wu1_head_list = [
    wu1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

wu1_sprite = pygame.image.load("assets/ninjas/WU1/WU1_back.png")
wu1_back_list = [
    wu1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

wu1_sprite = pygame.image.load("assets/ninjas/WU1/WU1_right.png")
wu1_right_list = [
    wu1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

wu1_sprite = pygame.image.load("assets/ninjas/WU1/WU1_left.png")
wu1_left_list = [
    wu1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

wu1_sprite = pygame.image.load("assets/ninjas/WU1/WU1_idle.png")
wu1_idle_list = [
    wu1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(2)
]

def get_wu1()->dict:
    wu1_dict = {}
    wu1_dict["head"] = wu1_head_list
    wu1_dict["back"] = wu1_back_list
    wu1_dict["right"] = wu1_right_list
    wu1_dict["left"] = wu1_left_list
    wu1_dict["idle"] = wu1_idle_list
    return wu1_dict

lloyd1_sprite = pygame.image.load("assets/ninjas/LLOYD1/LLOYD1_head.png")
lloyd1_head_list = [
    lloyd1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

lloyd1_sprite = pygame.image.load("assets/ninjas/LLOYD1/LLOYD1_back.png")
lloyd1_back_list = [
    lloyd1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

lloyd1_sprite = pygame.image.load("assets/ninjas/LLOYD1/LLOYD1_right.png")
lloyd1_right_list = [
    lloyd1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

lloyd1_sprite = pygame.image.load("assets/ninjas/LLOYD1/LLOYD1_left.png")
lloyd1_left_list = [
    lloyd1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

lloyd1_sprite = pygame.image.load("assets/ninjas/LLOYD1/LLOYD1_idle.png")
lloyd1_idle_list = [
    lloyd1_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(2)
]

def get_lloyd1()->dict:
    lloyd1_dict = {}
    lloyd1_dict["head"] = lloyd1_head_list
    lloyd1_dict["back"] = lloyd1_back_list
    lloyd1_dict["right"] = lloyd1_right_list
    lloyd1_dict["left"] = lloyd1_left_list
    lloyd1_dict["idle"] = lloyd1_idle_list
    return lloyd1_dict