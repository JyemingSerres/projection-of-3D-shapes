"""
Created on 12/15/2024
by Jye-Ming Serres
"""
import sys
import pygame
from config import *

from shape import Shape
from camera import Camera
from world import World
from display import Display

from pygame import Vector3

# Initialiser Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialiser l'état par défaut de world
camera = Camera()
shape = Shape([Vector3(10, 0, -50), Vector3(15, 100, 0), Vector3(15, 50, 0), Vector3(15, 0, 100)], 
              [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)])
world = World(camera, [shape])
display = Display(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    display.draw_world(world.camera, world.shapes)
    #display.draw_ui()

    blit_fps("FPS: " + str(round(clock.get_fps(), 1)), screen)
    pygame.display.flip()
    clock.tick(TARGET_FRAME_RATE)

pygame.quit()
sys.exit()