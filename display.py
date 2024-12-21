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

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.screen = screen
        self.screen_center = (screen.get_width()/2, screen.get_height()/2)
        self.font = pygame.font.SysFont('comicsans', 16)

        pygame.mouse.set_visible(False)

    def draw(self, world: World, clock: pygame.time.Clock) -> None:
        self.screen.fill(Display.BACKGROUND_COLOR)
        self._draw_world(world)
        self._draw_ui(clock)
        pygame.display.flip()

    def _draw_world(self, world: World) -> None:
        camera = world.camera
        shapes = world.shapes

        for shape in shapes:
            vertices_screen_pos = []
            within_frame = True

            for vertex in shape.vertices:
                # relative position of the vertex with respect to the aperture (i.e. the projection line)
                vrtx_rel_pos = vertex - camera.aperture

                # calculate the coefficient of the projection on the orientation of the camera. The dot product is equal to distance 
                # because camera.orientation is normalized
                vrtx_dist = vrtx_rel_pos.dot(camera.orientation)

                # vertex needs to be strictly in front of the aperture
                if vrtx_dist > 0:
                    # find the position of the vertex on the projection plane (principal plane) 
                    # relative to the image center (principal point) in 3D vector space
                    vrtx_ima_pos = (vrtx_rel_pos - (vrtx_dist*camera.orientation))*camera.focal_length/vrtx_dist

                    # convert vrtx_ima_pos to (x, y) position on the screen relative to screen center
                    vrtx_x = vrtx_ima_pos.dot(camera.image_x_vect) # works because camera.image_x_vect is normalized
                    vrtx_y = vrtx_ima_pos.dot(camera.image_y_vect) # works because camera.image_y_vect is normalized

                    # convert (x, y) to coordinates matching the pygame interface
                    vrtx_screen_pos = Vector2(vrtx_x, -vrtx_y) + Vector2(self.screen_center)

                    vertices_screen_pos.append(vrtx_screen_pos)
                else:
                    within_frame = False
                    break

            if within_frame:
                # draw lines corresponding to the edges of the shape
                for edge in shape.edges:
                    pygame.draw.aaline(self.screen, shape.color, vertices_screen_pos[edge[0]], vertices_screen_pos[edge[1]], 1)

    def _draw_ui(self, clock: pygame.time.Clock) -> None:
        center_x = self.screen.get_width()/2
        center_y = self.screen.get_height()/2

        # draw crosshair
        CROSSHAIR_SIZE = 5
        pygame.draw.line(self.screen, (255, 255, 255), (center_x - CROSSHAIR_SIZE, center_y), (center_x + CROSSHAIR_SIZE, center_y))
        pygame.draw.line(self.screen, (255, 255, 255), (center_x, center_y - CROSSHAIR_SIZE), (center_x, center_y + CROSSHAIR_SIZE))

        # blit current fps on the top left of the screen
        self._blit_str(f"FPS: {round(clock.get_fps(), 1)}", (255, 255, 255), (5, 0))
    
    def _blit_str(self, str: str, color: tuple, coord: tuple[float]) -> None:
        fps_surface = self.font.render(str, True, color)
        self.screen.blit(fps_surface, coord)