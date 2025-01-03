"""
"""

import pygame
from pygame import Vector3, Vector2, draw
from pygame.surface import Surface

from config import Color
from world import World
from shape import Shape

__author__ = "Jye-Ming Serres"


class Display:
    """
    Display doc
    """

    def __init__(self, screen: Surface) -> None:
        self._screen = screen
        self._screen_center = Vector2(screen.get_width(), screen.get_height())/2
        self._font = pygame.font.SysFont("Verdana", 12)
        self._crosshair_size = 10
        self._ui_color = Color.WHITE
        self._background_color = Color.DEEP_SPACE
        pygame.mouse.set_visible(False)

    def draw(self, world: World, fps: float) -> None:
        self._screen.fill(self._background_color.value)
        self._draw_world(world)
        self._draw_ui(fps, world.camera.aperture)

    def _draw_world(self, world: World) -> None:
        camera = world.camera
        shapes = world.shapes

        # sort shapes by the distance of their center to the aperture
        # we make sure to draw shapes that are closer on top of shapes that are further
        def center_to_aperture_dist(shape: Shape):
            return (shape.center - camera.aperture).dot(camera.orientation)
        shapes.sort(key=center_to_aperture_dist, reverse=True)

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
                    # find vertex (x, y) position on the projection plane relative to image center
                    vrtx_rel_scaled = vrtx_rel*camera.focal_length/vrtx_dist
                    vrtx_x = vrtx_rel_scaled.dot(camera.image_x) # works since image_x is normalized
                    vrtx_y = vrtx_rel_scaled.dot(camera.image_y) # works since image_y is normalized

                    # convert (x, y) to coordinates matching the pygame interface
                    vrtx_screen = Vector2(vrtx_x, -vrtx_y) + self._screen_center

                    vertices_screen.append(vrtx_screen)
                else:
                    within_frame = False
                    break

            if within_frame:
                for edge in shape.edges:
                    draw.aaline(self._screen, shape.color.value,
                                vertices_screen[edge[0]], vertices_screen[edge[1]])

    def _draw_ui(self, fps: float, camera_pos: Vector3) -> None:
        # draw crosshair
        x = self._screen_center.x
        y = self._screen_center.y
        offset = self._crosshair_size/2
        draw.line(self._screen, self._ui_color.value, (x - offset, y), (x + offset, y))
        draw.line(self._screen, self._ui_color.value, (x, y - offset), (x, y + offset))

        # draw text
        str_controls = """[ESC] quit
            [W] forward
            [A] left
            [S] backward
            [D] right
            [LSHIFT] down
            [SPACE] up"""
        str_fps = f"FPS: {round(fps, 1)}"
        str_pos = f"({camera_pos.x:.1f}, {camera_pos.y:.1f}, {camera_pos.z:.1f})"

        height = self._screen.get_height()
        width = self._screen.get_width()
        margin = 5
        self._blit_strings(str_controls, self._ui_color, (margin, margin), line_spacing=2)
        self._blit_string(str_fps, self._ui_color, (margin, height - margin), b_just=True)
        self._blit_string(str_pos, self._ui_color, (width - margin, margin), r_just=True)

    def _blit_string(
            self,
            line: str,
            color: Color,
            coord: tuple[int,  int],
            r_just: bool = False,
            b_just: bool = False) -> pygame.Rect:
        surface = self._font.render(line.strip(), True, color.value)
        x = coord[0] - surface.get_width() if r_just else coord[0]
        y = coord[1] - surface.get_height() if b_just else coord[1]
        return self._screen.blit(surface, (x, y))

    def _blit_strings(
            self,
            lines: str,
            color: Color,
            coord: tuple[int,  int],
            r_just: bool = False,
            b_just: bool = False,
            line_spacing: int = 0) -> None:
        strings = lines.split("\n")
        total_offset = 0
        for string in strings:
            rect = self._blit_string(
                string, color, (coord[0], coord[1] + total_offset), r_just, b_just)
            offset = rect.height + line_spacing
            total_offset += -offset if b_just else offset
