"""
Created on 12/20/2024
by Jye-Ming Serres
"""
from collections.abc import Callable
from pygame import Vector3

from config import GOLDEN_RATIO
from shape import Shape


class ShapeFactory:
    """
    ShapeFactory doc
    """

    def make_shape(self, type: str, pos: Vector3, radius: float, color: tuple[int, int, int, int]) -> Shape:
        maker = self._get_maker(type)
        shape = maker(color)
        max_vect = max(shape.vertices, key=lambda vect: vect.length_squared())
        scale_factor = radius/max_vect.length()
        for vertex in shape.vertices:
            vertex *= scale_factor
        shape.move(pos)
        return shape

    def _get_maker(self, type: str) -> Callable:
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
    
    def _make_tetrahedron(self, color: tuple[int, int, int, int]) -> Shape:
        vertices = [
            Vector3(1, 1, 1), 
            Vector3(1, -1, -1), 
            Vector3(-1, 1, -1), 
            Vector3(-1, -1, 1), 
            ]
        edges = [
            (0, 1), 
            (1, 2), 
            (2, 0), 
            (0, 3), 
            (1, 3), 
            (2, 3), 
            ]
        return Shape(Vector3(0, 0, 0), vertices, edges, color)

    def _make_cube(self, color: tuple[int, int, int, int]) -> Shape:
        vertices = [
            Vector3(1, 1, 1), 
            Vector3(1, 1, -1), 
            Vector3(1, -1, -1), 
            Vector3(1, -1, 1), 
            Vector3(-1, 1, 1), 
            Vector3(-1, 1, -1), 
            Vector3(-1, -1, -1), 
            Vector3(-1, -1, 1), 
            ]
        edges = [
            (0, 1), 
            (1, 2), 
            (2, 3), 
            (3, 0), 
            (4, 5), 
            (5, 6), 
            (6, 7), 
            (7, 4), 
            (0, 4), 
            (1, 5), 
            (2, 6), 
            (3, 7), 
            ]
        return Shape(Vector3(0, 0, 0), vertices, edges, color)
    
    def _make_octahedron(self, color: tuple[int, int, int, int]) -> Shape:
        vertices = [
            Vector3(1, 0, 0), 
            Vector3(0, 1, 0), 
            Vector3(0, 0, 1), 
            Vector3(-1, 0, 0), 
            Vector3(0, -1, 0), 
            Vector3(0, 0, -1), 
            ]
        edges = [
            (0, 1), 
            (0, 2), 
            (0, 4), 
            (0, 5), 
            (3, 1), 
            (3, 2), 
            (3, 4), 
            (3, 5), 
            (1, 2), 
            (2, 4), 
            (4, 5), 
            (5, 1), 
            ]
        return Shape(Vector3(0, 0, 0), vertices, edges, color)
    
    def _make_dodecahedron(self, color: tuple[int, int, int, int]) -> Shape:
        vertices = [
            Vector3(0, -1/GOLDEN_RATIO, -GOLDEN_RATIO), 
            Vector3(0, 1/GOLDEN_RATIO, -GOLDEN_RATIO), 
            Vector3(-1, -1, -1), 
            Vector3(-1, 1, -1), 
            Vector3(1, -1, -1), 
            Vector3(1, 1, -1), 
            Vector3(-GOLDEN_RATIO, 0, -1/GOLDEN_RATIO), 
            Vector3(GOLDEN_RATIO, 0, -1/GOLDEN_RATIO), 
            Vector3(-1/GOLDEN_RATIO, -GOLDEN_RATIO, 0), 
            Vector3(-1/GOLDEN_RATIO, GOLDEN_RATIO, 0), 
            Vector3(1/GOLDEN_RATIO, -GOLDEN_RATIO, 0), 
            Vector3(1/GOLDEN_RATIO, GOLDEN_RATIO, 0), 
            Vector3(-GOLDEN_RATIO, 0, 1/GOLDEN_RATIO), 
            Vector3(GOLDEN_RATIO, 0, 1/GOLDEN_RATIO), 
            Vector3(-1, -1, 1), 
            Vector3(-1, 1, 1), 
            Vector3(1, -1, 1), 
            Vector3(1, 1, 1), 
            Vector3(0, -1/GOLDEN_RATIO, GOLDEN_RATIO), 
            Vector3(0, 1/GOLDEN_RATIO, GOLDEN_RATIO), 
            ]
        edges = [
            (0, 1), 
            (0, 2), 
            (0, 4), 
            (1, 3), 
            (1, 5), 
            (6, 2), 
            (6, 3), 
            (7, 4), 
            (7, 5), 
            (2, 8), 
            (3, 9), 
            (4, 10), 
            (5, 11), 
            (8, 10), 
            (9, 11), 
            (6, 12), 
            (7, 13), 
            (8, 14), 
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

    def _make_icosahedron(self, color: tuple[int, int, int, int]) -> Shape:
        vertices = [
            Vector3(0, 1, GOLDEN_RATIO), 
            Vector3(0, 1, -GOLDEN_RATIO), 
            Vector3(0, -1, GOLDEN_RATIO), 
            Vector3(0, -1, -GOLDEN_RATIO), 
            Vector3(1, GOLDEN_RATIO, 0), 
            Vector3(1, -GOLDEN_RATIO, 0), 
            Vector3(-1, GOLDEN_RATIO, 0), 
            Vector3(-1, -GOLDEN_RATIO, 0), 
            Vector3(GOLDEN_RATIO, 0, 1), 
            Vector3(-GOLDEN_RATIO, 0, 1), 
            Vector3(GOLDEN_RATIO, 0, -1), 
            Vector3(-GOLDEN_RATIO, 0, -1), 
            ]
        edges = [
            (1, 3), 
            (10, 1), 
            (10, 3), 
            (11, 1), 
            (11, 3), 
            (6, 11), 
            (11, 7), 
            (6, 1), 
            (7, 3), 
            (4, 1), 
            (5, 3), 
            (4, 6), 
            (5, 7), 
            (4, 10), 
            (5, 10), 
            (9, 7), 
            (9 , 6), 
            (9, 0), 
            (9, 2), 
            (9, 11), 
            (8, 0), 
            (8, 2), 
            (8, 10), 
            (8, 4), 
            (8, 5), 
            (0, 2), 
            (0, 4), 
            (0, 6), 
            (2, 5), 
            (2, 7), 
            ]
        return Shape(Vector3(0, 0, 0), vertices, edges, color)
