"""
Created on 12/16/2024
by Jye-Ming Serres
"""
import pygame
from pygame import Vector2, draw
from pygame.surface import Surface

from config import *
from world import World

class Display:
    """
    Display doc
    """

    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.screen_center = Vector2(screen.get_width(), screen.get_height())/2
        self.font = pygame.font.SysFont("Times New Roman", 16)
        self.crosshair_size = 10
        self.ui_color = Color.WHITE
        self.background_color = Color.DEEP_SPACE
        pygame.mouse.set_visible(False)

    def draw(self, world: World, fps: float) -> None:
        self.screen.fill(self.background_color.value)
        self._draw_world(world)
        self._draw_ui(fps)

    def _draw_world(self, world: World) -> None:
        camera = world.camera
        shapes = world.shapes

        for shape in shapes:
            vertices_screen = []
            within_frame = True

            for vertex in shape.vertices:
                # relative position with respect to the aperture (i.e. the projection line)
                vrtx_rel = vertex - camera.aperture

                # calculate the coefficient of the projection on camera orientation 
                # The dot product is equal to distance since orientation is normalized
                vrtx_dist = vrtx_rel.dot(camera.orientation)

                # vertex needs to be strictly in front of the aperture
                if vrtx_dist > 0:
                    # find (x, y) position on the projection plane relative to image center
                    vrtx_ima = vrtx_rel*camera.focal_length/vrtx_dist
                    vrtx_x = vrtx_ima.dot(camera.image_x_vect) # works since image_x_vect is normalized
                    vrtx_y = vrtx_ima.dot(camera.image_y_vect) # works since image_y_vect is normalized

                    # convert (x, y) to coordinates matching the pygame interface
                    vrtx_screen = Vector2(vrtx_x, -vrtx_y) + self.screen_center

                    vertices_screen.append(vrtx_screen)
                else:
                    within_frame = False
                    break

            if within_frame:
                for edge in shape.edges:
                    draw.aaline(self.screen, shape.color.value, vertices_screen[edge[0]], vertices_screen[edge[1]])

    def _draw_ui(self, fps: float) -> None:
        # draw crosshair
        x = self.screen_center.x
        y = self.screen_center.y
        offset = self.crosshair_size/2
        draw.line(self.screen, self.ui_color.value, (x - offset, y), (x + offset, y))
        draw.line(self.screen, self.ui_color.value, (x, y - offset), (x, y + offset))

        margin = 5
        self._blit_string("[ESC] to quit", self.ui_color, (margin, 5))
        self._blit_string(f"FPS: {round(fps, 1)}", self.ui_color, (margin, self.screen.get_height() - 24))
    
    def _blit_string(self, str: str, color: Color, coord: tuple[float,  float]) -> None:
        surface = self.font.render(str, True, color.value)
        self.screen.blit(surface, coord)