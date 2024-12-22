"""
Created on 12/20/2024
by Jye-Ming Serres
"""
from collections.abc import Callable
from pygame import Vector3

from config import *
from shape import Shape


class ShapeFactory:
    """
    ShapeFactory doc
    """

    def make_shape(self, type: str, pos: Vector3, radius: float, color: Color) -> Shape:
        maker = self._get_maker(type)
        shape = maker(color)
        max_vect = max(shape.vertices, key=lambda vect: vect.length_squared())
        scale_factor = radius/max_vect.length()
        for vertex in shape.vertices:
            vertex *= scale_factor
        shape.move(pos)
        return shape

    def _get_maker(self, type: str) -> Callable[[Color], Shape]:
        maker = None
        match type:
            case "tetrahedron":
                maker = self._make_tetrahedron
            case "cube":
                maker = self._make_cube
            case "octahedron":
                maker = self._make_octahedron
            case "dodecahedron":
                maker = self._make_dodecahedron
            case "icosahedron":
                maker = self._make_icosahedron
            case _:
                raise ValueError(f"Unknown shape type to ShapeFactory : '{type}'")
        return maker
    
    def _make_tetrahedron(self, color: Color) -> Shape:
        vertices = [
            Vector3(-1, -1, 1),
            Vector3(-1, 1, -1),
            Vector3(1, -1, -1),
            Vector3(1, 1, 1),
            ]
        edges = [
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 2),
            (1, 3),
            (2, 3),
            ]
        return Shape(Vector3(0, 0, 0), vertices, edges, color)

    def _make_cube(self, color: Color) -> Shape:
        vertices = [
            Vector3(-1, -1, -1),
            Vector3(-1, -1, 1),
            Vector3(-1, 1, -1),
            Vector3(-1, 1, 1),
            Vector3(1, -1, -1),
            Vector3(1, -1, 1),
            Vector3(1, 1, -1),
            Vector3(1, 1, 1),
            ]
        edges = [
            (0, 1),
            (0, 2),
            (0, 4),
            (1, 3),
            (1, 5),
            (2, 3),
            (2, 6),
            (3, 7),
            (4, 5),
            (4, 6),
            (5, 7),
            (6, 7),
            ]
        return Shape(Vector3(0, 0, 0), vertices, edges, color)
    
    def _make_octahedron(self, color: Color) -> Shape:
        vertices = [
            Vector3(-1, 0, 0),
            Vector3(0, -1, 0),
            Vector3(0, 0, -1),
            Vector3(0, 0, 1),
            Vector3(0, 1, 0),
            Vector3(1, 0, 0),
            ]
        edges = [
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (1, 2),
            (1, 3),
            (1, 5),
            (2, 4),
            (2, 5),
            (3, 4),
            (3, 5),
            (4, 5),
            ]
        return Shape(Vector3(0, 0, 0), vertices, edges, color)
    
    def _make_dodecahedron(self, color: Color) -> Shape:
        vertices = [
            Vector3(-GOLDEN_RATIO, 0, -1/GOLDEN_RATIO),
            Vector3(-GOLDEN_RATIO, 0, 1/GOLDEN_RATIO),
            Vector3(-1, -1, -1),
            Vector3(-1, -1, 1),
            Vector3(-1, 1, -1),
            Vector3(-1, 1, 1),
            Vector3(-1/GOLDEN_RATIO, -GOLDEN_RATIO, 0),
            Vector3(-1/GOLDEN_RATIO, GOLDEN_RATIO, 0),
            Vector3(0, -1/GOLDEN_RATIO, -GOLDEN_RATIO),
            Vector3(0, -1/GOLDEN_RATIO, GOLDEN_RATIO),
            Vector3(0, 1/GOLDEN_RATIO, -GOLDEN_RATIO),
            Vector3(0, 1/GOLDEN_RATIO, GOLDEN_RATIO),
            Vector3(1/GOLDEN_RATIO, -GOLDEN_RATIO, 0),
            Vector3(1/GOLDEN_RATIO, GOLDEN_RATIO, 0),
            Vector3(1, -1, -1),
            Vector3(1, -1, 1),
            Vector3(1, 1, -1),
            Vector3(1, 1, 1),
            Vector3(GOLDEN_RATIO, 0, -1/GOLDEN_RATIO),
            Vector3(GOLDEN_RATIO, 0, 1/GOLDEN_RATIO),
            ]
        edges = [
            (0, 1),
            (0, 2),
            (0, 4),
            (1, 3),
            (1, 5),
            (2, 6),
            (2, 8),
            (3, 6),
            (3, 9),
            (4, 7),
            (4, 10),
            (5, 7),
            (5, 11),
            (6, 12),
            (7, 13),
            (8, 10),
            (8, 14),
            (9, 11),
            (9, 15),
            (10, 16),
            (11, 17),
            (12, 14),
            (12, 15),
            (13, 16),
            (13, 17),
            (14, 18),
            (15, 19),
            (16, 18),
            (17, 19),
            (18, 19),
            ]
        return Shape(Vector3(0, 0, 0), vertices, edges, color)

    def _make_icosahedron(self, color: Color) -> Shape:
        vertices = [
            Vector3(-GOLDEN_RATIO, 0, -1),
            Vector3(-GOLDEN_RATIO, 0, 1),
            Vector3(-1, -GOLDEN_RATIO, 0),
            Vector3(-1, GOLDEN_RATIO, 0),
            Vector3(0, -1, -GOLDEN_RATIO),
            Vector3(0, -1, GOLDEN_RATIO),
            Vector3(0, 1, -GOLDEN_RATIO),
            Vector3(0, 1, GOLDEN_RATIO),
            Vector3(1, -GOLDEN_RATIO, 0),
            Vector3(1, GOLDEN_RATIO, 0),
            Vector3(GOLDEN_RATIO, 0, -1),
            Vector3(GOLDEN_RATIO, 0, 1),
            ]
        edges = [
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 6),
            (1, 2),
            (1, 3),
            (1, 5),
            (1, 7),
            (2, 4),
            (2, 5),
            (2, 8),
            (3, 6),
            (3, 7),
            (3, 9),
            (4, 6),
            (4, 8),
            (4, 10),
            (5, 7),
            (5, 8),
            (5, 11),
            (6, 9),
            (6, 10),
            (7, 9),
            (7, 11),
            (8, 10),
            (8, 11),
            (9, 10),
            (9, 11),
            (10, 11),
            ]
        return Shape(Vector3(0, 0, 0), vertices, edges, color)
