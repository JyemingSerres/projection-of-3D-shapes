"""
Created on 12/16/2024
by Jye-Ming Serres
"""
import pygame
from pygame import Vector2
from pygame.colordict import THECOLORS as COLOR

from world import World

class Display:
    """
    Display doc
    """

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.screen = screen
        self.screen_center = (screen.get_width()/2, screen.get_height()/2)
        self.font = pygame.font.SysFont("Times New Roman", 16)
        pygame.mouse.set_visible(False)

        self.CROSS_SIZE = 5
        self.UI_COLOR = COLOR["white"]
        self.BACKGROUND_COLOR = COLOR["black"]

    def draw(self, world: World, fps: float) -> None:
        self.screen.fill(self.BACKGROUND_COLOR)
        self._draw_world(world)
        self._draw_ui(fps)
        pygame.display.flip()

    def _draw_world(self, world: World) -> None:
        camera = world.camera
        shapes = world.shapes

        for shape in shapes:
            vertices_screen = []
            within_frame = True

            for vertex in shape.vertices:
                # relative position of the vertex with respect to the aperture (i.e. the projection line)
                vrtx_rel = vertex - camera.aperture

                # calculate the coefficient of the projection on the orientation of the camera. 
                # The dot product is equal to distance because camera.orientation is normalized
                vrtx_dist = vrtx_rel.dot(camera.orientation)

                # vertex needs to be strictly in front of the aperture
                if vrtx_dist > 0:
                    # find the position of the vertex on the projection plane (principal plane) 
                    # relative to the image center (principal point) in 3D vector space
                    vrtx_ima = (vrtx_rel - (vrtx_dist*camera.orientation))*camera.focal_length/vrtx_dist

                    # convert vrtx_ima_pos to (x, y) position on the screen relative to screen center
                    vrtx_x = vrtx_ima.dot(camera.image_x_vect) # works because camera.image_x_vect is normalized
                    vrtx_y = vrtx_ima.dot(camera.image_y_vect) # works because camera.image_y_vect is normalized

                    # convert (x, y) to coordinates matching the pygame interface
                    vrtx_screen = Vector2(vrtx_x, -vrtx_y) + Vector2(self.screen_center)

                    vertices_screen.append(vrtx_screen)
                else:
                    within_frame = False
                    break

            if within_frame:
                # draw lines corresponding to the edges of the shape
                for edge in shape.edges:
                    pygame.draw.aaline(self.screen, shape.color, vertices_screen[edge[0]], vertices_screen[edge[1]])

    def _draw_ui(self, fps: float) -> None:
        # draw crosshair
        pygame.draw.line(self.screen, self.UI_COLOR, (self.screen_center[0] - self.CROSS_SIZE, self.screen_center[1]), 
                         (self.screen_center[0] + self.CROSS_SIZE, self.screen_center[1]))
        pygame.draw.line(self.screen, self.UI_COLOR, (self.screen_center[0], self.screen_center[1] - self.CROSS_SIZE), 
                         (self.screen_center[0], self.screen_center[1] + self.CROSS_SIZE))

        self._blit_str(f"FPS: {round(fps, 1)}", self.UI_COLOR, (5, 5))
        self._blit_str(f"[ESC] to quit", self.UI_COLOR, (5, 25))
    
    def _blit_str(self, str: str, color: tuple[int, int, int, int], coord: tuple[float,  float]) -> None:
        surface = self.font.render(str, True, color)
        self.screen.blit(surface, coord)