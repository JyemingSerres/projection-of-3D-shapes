"""
Created on 12/15/2024
by Jye-Ming Serres
"""
import sys
import pygame
from pygame import Vector3

# My own modules
from config import *
from shape import Shape
from camera import Camera
from world import World
from display import Display
from controller import Controller

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Default state of the world
camera = Camera()
shape = Shape([Vector3(60, 0, -100), Vector3(60, 200, 0), Vector3(10, 50, 0), Vector3(60, 0, 200)], 
              [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)])
world = World(camera, [shape])
display = Display(screen)
controller = Controller()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # continuous inputs
        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_a] is is_key_pressed[pygame.K_d]:
            #print("neutral")
            pass
        elif is_key_pressed[pygame.K_a]:
            #print("left")
            pass
        elif is_key_pressed[pygame.K_d]:
            #print("right")
            pass
    
    controller.handle_events()
    world.update()
    display.render(world, clock)
    
    clock.tick(TARGET_FRAME_RATE)

pygame.quit()
sys.exit()