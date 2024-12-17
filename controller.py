"""
Created on 12/16/2024
by Jye-Ming Serres
"""
import pygame

class Controller:
    """
    Controller doc
    """

    def __init__(self) -> None:
        pass

    def handle_inputs(self) -> None:
        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_a] is is_key_pressed[pygame.K_d]:
            #print("left-right neutral")
            pass
        elif is_key_pressed[pygame.K_a]:
            #print("left")
            pass
        elif is_key_pressed[pygame.K_d]:
            #print("right")
            pass
        
        if is_key_pressed[pygame.K_w] is is_key_pressed[pygame.K_s]:
            #print("front-back neutral")
            pass
        elif is_key_pressed[pygame.K_w]:
            #print("front")
            pass
        elif is_key_pressed[pygame.K_s]:
            #print("back")
            pass