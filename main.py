"""
Created on 12/15/2024
by Jye-Ming Serres
"""
import sys
import pygame
from pygame import Vector3

# Project modules
from config import *
from shape_factory import ShapeFactory
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

# Initialize the program
camera = Camera()
shape_factory = ShapeFactory()
tetrahedron = shape_factory.make_shape("tetrahedron", Vector3(600, -600, 0), 100, COLOR["red"])
cube = shape_factory.make_shape("cube", Vector3(600, -300, 0), 100, COLOR["blue"])
octahedron = shape_factory.make_shape("octahedron", Vector3(600, 0, 0), 100, COLOR["green"])
dodecahedron = shape_factory.make_shape("dodecahedron", Vector3(600, 300, 0), 100, COLOR["yellow"])
icosahedron = shape_factory.make_shape("icosahedron", Vector3(600, 600, 0), 100, COLOR["cyan"])
world = World(camera, [tetrahedron, cube, octahedron, dodecahedron, icosahedron])
display = Display(screen)
engine = Engine(world, display, clock)

while engine.running:
    elapsed = clock.tick(TARGET_FRAME_RATE)
    engine.handle_events()
    engine.update_world(elapsed)
    engine.render()

pygame.quit()
sys.exit()