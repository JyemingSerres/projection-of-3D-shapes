"""
Created on 12/16/2024
by Jye-Ming Serres
"""
import pygame
from pygame import Vector2

from world import World

class Display:
    """
    Display doc
    """
    BACKGROUND_COLOR = (0, 0, 0)

    def __init__(self, screen) -> None:
        self.screen = screen
        self.font = pygame.font.SysFont('comicsans', 16)

    def update(self, world: World, clock: pygame.time.Clock) -> None:
        self.screen.fill(Display.BACKGROUND_COLOR)
        self.__draw_world(world)
        self.__draw_ui(clock)
        pygame.display.flip()

    def __draw_world(self, world: World) -> None:
        camera = world.camera
        shapes = world.shapes

        for shape in shapes:
            vertices_screen_pos = []
            for vertex in shape.vertices:
                # relative position of the vertex with respect to the aperture
                vrtx_rel_aperture = vertex - camera.aperture_pos

                # calculate the projection of the vector on the orientation of the camera
                vrtx_ima_dist = vrtx_rel_aperture.project(camera.orientation)

                # vect_ima_pos is the position of the vertex on a virtual plane (representing the image captured) 
                # relative to camera.center in 3D vector space
                vrtx_ima_pos = (vrtx_rel_aperture - vrtx_ima_dist)*camera.aperture_distance/vrtx_ima_dist.length()

                # convert vect_ima_pos to (x, y) position on the screen relative to screen center
                vrtx_x_pos = vrtx_ima_pos.dot(camera.image_x_vect) # works because camera.image_x_vect is normalized
                vrtx_y_pos = vrtx_ima_pos.dot(camera.image_y_vect) # works because camera.image_y_vect is normalized

                # convert (x, y) to coordinates in tune with the pygame interface
                vrtx_screen = Vector2(vrtx_x_pos, -vrtx_y_pos) + Vector2(self.screen.get_width()/2, self.screen.get_height()/2)
                vertices_screen_pos.append(vrtx_screen)
            
            for edge in shape.edges:
                pygame.draw.line(self.screen, shape.color, vertices_screen_pos[edge[0]], vertices_screen_pos[edge[1]])

    def __draw_ui(self, clock: pygame.time.Clock) -> None:
        center_x = self.screen.get_width()/2
        center_y = self.screen.get_height()/2

        # draw crosshair
        CROSSHAIR_SIZE = 5
        pygame.draw.line(self.screen, (255, 255, 255), (center_x - CROSSHAIR_SIZE, center_y), (center_x + CROSSHAIR_SIZE, center_y))
        pygame.draw.line(self.screen, (255, 255, 255), (center_x, center_y - CROSSHAIR_SIZE), (center_x, center_y + CROSSHAIR_SIZE))

        # blit current fps on the top left of the screen
        self.__blit_str(f"FPS: {round(clock.get_fps(), 1)}", (255, 255, 255), (5, 0))
    
    def __blit_str(self, str: str, color: tuple, coord: tuple[float]) -> None:
        fps_surface = self.font.render(str, True, color)
        self.screen.blit(fps_surface, coord)