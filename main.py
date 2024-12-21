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
pygame.event.set_grab(True)
pygame.event.set_keyboard_grab(False)

# Default state of the world
camera = Camera()
tetrahedron = Shape([Vector3(300, 0, -100), Vector3(300, 200, 0), Vector3(200, 50, 0), Vector3(300, 0, 200)], 
              [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)], (255, 0, 0))
cube = Shape([Vector3(300, 500, -100), Vector3(300, 500, 100), Vector3(300, 700, -100), Vector3(300, 700, 100), Vector3(500, 500, -100), Vector3(500, 500, 100), Vector3(500, 700, -100), Vector3(500, 700, 100)], 
              [(0, 1), (1, 3), (3, 2), (2, 0), (4, 5), (5, 7), (7, 6), (6, 4), (0, 4), (1, 5), (3, 7), (2,6)], (0, 0, 255))
world = World(camera, [tetrahedron, cube])
display = Display(screen)
engine = Engine(world, display, clock)

while engine.running:
    elapsed = clock.tick(TARGET_FRAME_RATE)
    engine.handle_events()
    engine.update_world(elapsed)
    engine.render()

pygame.quit()
sys.exit()