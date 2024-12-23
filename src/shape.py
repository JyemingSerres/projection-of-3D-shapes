"""
Created on 12/15/2024
by Jye-Ming Serres
"""
from pygame import Vector3

from config import Color

class Shape:
    """
    Shape doc
    """

    def __init__(self, center: Vector3,
                 vertices: list[Vector3],
                 edges: list[tuple[int, int]],
                 color: Color) -> None:
        self._center = center
        self._color = color
        self._vertices = vertices
        self._edges = edges

    @property
    def center(self) -> Vector3:
        return self._center

    @property
    def color(self) -> Color:
        return self._color

    @property
    def vertices(self) -> list[Vector3]:
        return self._vertices

    @property
    def edges(self) -> list[tuple]:
        return self._edges

    def update(self, dt: float) -> None: pass

    def move(self, displacement: Vector3) -> None:
        for vertex in self._vertices:
            vertex += displacement
        self._center += displacement

    def rotate(self, angular_displacement: Vector3) -> None:
        center_pos = self._center.copy()
        self.move(-center_pos)
        for vertex in self._vertices:
            vertex.rotate_x_ip(angular_displacement.x)
            vertex.rotate_y_ip(angular_displacement.y)
            vertex.rotate_z_ip(angular_displacement.z)
        self.move(center_pos)
