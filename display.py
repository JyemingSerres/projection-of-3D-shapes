"""
Created on 12/16/2024
by Jye-Ming Serres
"""
import pygame
from pygame import Vector3, Vector2, draw
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
        self.font = pygame.font.SysFont("Verdana", 12)
        self.crosshair_size = 10
        self.ui_color = Color.WHITE
        self.background_color = Color.DEEP_SPACE
        pygame.mouse.set_visible(False)

    def draw(self, world: World, fps: float) -> None:
        self.screen.fill(self.background_color.value)
        self._draw_world(world)
        self._draw_ui(fps, world.camera.aperture)

    def _draw_world(self, world: World) -> None:
        camera = world.camera
        shapes = world.shapes

        # sort by shape center distance to aperture in descending order
        shapes.sort(key=lambda shape: (shape.center - camera.aperture).dot(camera.orientation), reverse=True)

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
                    vrtx_rel_scaled = vrtx_rel*camera.focal_length/vrtx_dist
                    vrtx_x = vrtx_rel_scaled.dot(camera.image_x_vect) # works since image_x_vect is normalized
                    vrtx_y = vrtx_rel_scaled.dot(camera.image_y_vect) # works since image_y_vect is normalized

                    # convert (x, y) to coordinates matching the pygame interface
                    vrtx_screen = Vector2(vrtx_x, -vrtx_y) + self.screen_center

                    vertices_screen.append(vrtx_screen)
                else:
                    within_frame = False
                    break

            if within_frame:
                for edge in shape.edges:
                    draw.aaline(self.screen, shape.color.value, vertices_screen[edge[0]], vertices_screen[edge[1]])

    def _draw_ui(self, fps: float, camera_pos: Vector3) -> None:
        margin = 5
        
        # draw crosshair
        x = self.screen_center.x
        y = self.screen_center.y
        offset = self.crosshair_size/2
        draw.line(self.screen, self.ui_color.value, (x - offset, y), (x + offset, y))
        draw.line(self.screen, self.ui_color.value, (x, y - offset), (x, y + offset))

        # draw text
        str_controls = """[ESC] quit
            [W] forward
            [A] left
            [S] backward
            [D] right
            [LSHIFT] down
            [SPACE] up"""
        str_fps = f"FPS: {round(fps, 1)}"
        str_position = f"({camera_pos.x:.2f}, {camera_pos.y:.2f}, {camera_pos.z:.2f})"

        self._blit_lines(str_controls, self.ui_color, (margin, margin), line_spacing=2)
        self._blit_line(str_fps, self.ui_color, (margin, self.screen.get_height() - margin), bottom_just=True)
        self._blit_line(str_position, self.ui_color, (self.screen.get_width() - margin, margin), right_just=True)
    
    def _blit_line(
            self,
            line: str,
            color: Color,
            coord: tuple[int,  int],
            right_just: bool = False,
            bottom_just: bool = False) -> pygame.Rect:
        surface = self.font.render(line.strip(), True, color.value)
        x = coord[0] - surface.get_width() if right_just else coord[0]
        y = coord[1] - surface.get_height() if bottom_just else coord[1]
        return self.screen.blit(surface, (x, y))

    def _blit_lines(
            self, 
            lines: str, 
            color: Color, 
            coord: tuple[int,  int], 
            right_just: bool = False, 
            bottom_just: bool = False, 
            line_spacing: int = 0) -> None:
        strings = lines.split("\n")
        y_offset = 0
        for string in strings:
            rect = self._blit_line(string, color, (coord[0], coord[1] + y_offset), right_just, bottom_just)
            if bottom_just:
                y_offset -= rect.height + line_spacing
            else:
                y_offset += rect.height + line_spacing