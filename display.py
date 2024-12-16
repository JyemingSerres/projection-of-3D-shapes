"""
Created on 12/16/2024
by Jye-Ming Serres
"""
from shape import Shape
from camera import Camera

import pygame
from pygame import Vector2

class Display:
    """
    Display doc
    """

    def __init__(self, screen) -> None:
        self.screen = screen

    def draw_world(self, camera: Camera, shapes: list[Shape]):
        for shape in shapes:
            vertices_screen = []
            for vertex in shape.vertices:
                vrtx_rel_pupil = vertex - camera.pupil
                vrtx_ima_dist = vrtx_rel_pupil.project(camera.orientation)
                # vect_pos is the position of the vertex relative to the image center
                vrtx_ima_pos = (vrtx_rel_pupil - vrtx_ima_dist)*camera.pupil_distance/(camera.pupil_distance + vrtx_ima_dist.length())
                # convert vect_pos to a vector relative to the origin of the screen (this is hardcoded for it to work in the default orientation of the camera)
                # 2 is an arbitrary multiplier at this point
                vrtx_screen = 2*Vector2(vrtx_ima_pos.z, -vrtx_ima_pos.y) + Vector2(self.screen.get_width()/2, self.screen.get_height()/2)
                vertices_screen.append(vrtx_screen)
            print(vertices_screen)
            for edge in shape.edges:
                pygame.draw.line(self.screen, (255, 0 ,0), vertices_screen[edge[0]], vertices_screen[edge[1]])
        print("-----")

    def draw_ui(self):
        pass
