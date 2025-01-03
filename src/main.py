"""
Created on 12/15/2024
by Jye-Ming Serres
"""
import sys
import pygame
from pygame import Vector3

import config
from config import Color
from shape_factory import ShapeFactory
from camera import Camera
from world import World
from display import Display
from engine import Engine


# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Projection of 3D shapes")
pygame.event.set_grab(True)
pygame.event.set_keyboard_grab(False)

# Initialize the program
camera = Camera()
shape_factory = ShapeFactory()
tetrahedron = shape_factory.make_shape("tetrahedron", Vector3(600, -600, 0), 100, Color.RED)
cube = shape_factory.make_shape("cube", Vector3(600, -300, 0), 100, Color.BLUE)
octahedron = shape_factory.make_shape("octahedron", Vector3(600, 0, 0), 100, Color.GREEN)
dodecahedron = shape_factory.make_shape("dodecahedron", Vector3(600, 300, 0), 100, Color.YELLOW)
icosahedron = shape_factory.make_shape("icosahedron", Vector3(600, 600, 0), 100, Color.CYAN)
world = World(camera, [tetrahedron, cube, octahedron, dodecahedron, icosahedron])
display = Display(screen)
engine = Engine(world, display, clock)

while engine.running:
    elapsed = clock.tick(config.TARGET_FRAME_RATE)
    engine.handle_events()
    engine.update_world(elapsed)
    engine.render()

pygame.quit()
sys.exit()
