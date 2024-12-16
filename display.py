"""
Created on 12/16/2024
by Jye-Ming Serres
"""
from world import World

import pygame
from pygame import Vector2

class Display:
    """
    Display doc
    """

    def __init__(self, screen) -> None:
        self.screen = screen
        self.font = pygame.font.SysFont('comicsans', 16)

    def update(self, world: World, clock: pygame.time.Clock) -> None:
        self.screen.fill((0, 0, 0))
        self.__draw_world(world)
        self.__draw_ui(clock)
        pygame.display.flip()

    def __draw_world(self, world: World) -> None:
        camera = world.camera
        shapes = world.shapes
        for shape in shapes:
            vertices_screen_pos = []
            for vertex in shape.vertices:
                vrtx_rel_pupil = vertex - camera.pupil
                vrtx_ima_dist = vrtx_rel_pupil.project(camera.orientation)
                # vect_pos is the position of the vertex relative to the image center
                vrtx_ima_pos = (vrtx_rel_pupil - vrtx_ima_dist)*camera.pupil_distance/vrtx_ima_dist.length()
                # convert vect_pos to a vector relative to the origin of the screen (this is hardcoded for it to work in the default orientation of the camera)
                vrtx_screen = Vector2(vrtx_ima_pos.z, -vrtx_ima_pos.y) + Vector2(self.screen.get_width()/2, self.screen.get_height()/2)
                vertices_screen_pos.append(vrtx_screen)
            print(vertices_screen_pos)
            for edge in shape.edges:
                pygame.draw.line(self.screen, (255, 0 ,0), vertices_screen_pos[edge[0]], vertices_screen_pos[edge[1]])
        print("-----")

    def __draw_ui(self, clock: pygame.time.Clock) -> None:
        # show fps
        self.__blit_str(f"FPS: {round(clock.get_fps(), 1)}", (5, 0))
    
    def __blit_str(self, str: str, coord: tuple[float]) -> None:
        fps_surface = self.font.render(str, True, (200, 200, 200))
        self.screen.blit(fps_surface, coord)