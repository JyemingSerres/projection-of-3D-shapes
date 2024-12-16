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

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Default state for testing
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
    
    world.update()
    display.update(world, clock)
    clock.tick(TARGET_FRAME_RATE)

pygame.quit()
sys.exit()