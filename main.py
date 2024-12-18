"""
Created on 12/15/2024
by Jye-Ming Serres
"""
import sys
import pygame
from pygame import Vector3

# Project modules
from config import *
from shape import Shape
from camera import Camera
from world import World
from display import Display
from engine import Engine

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Default state of the world
camera = Camera()
shape = Shape([Vector3(200, 0, -100), Vector3(200, 200, 0), Vector3(100, 50, 0), Vector3(200, 0, 200)], 
              [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)])
world = World(camera, [shape])
display = Display(screen)
engine = Engine(world, display, clock)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            engine.handle_event(event)

    engine.update_world()
    engine.render()
    
    clock.tick(TARGET_FRAME_RATE)

pygame.quit()
sys.exit()