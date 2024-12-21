"""
Created on 12/15/2024
by Jye-Ming Serres
"""
from pygame import Vector3

class Shape:
    """
    Shape doc
    """

    def __init__(self, vertices: list[Vector3], edges: list[tuple[int, int]], color: tuple[int, int, int]) -> None:
        self.color = color
        self._vertices = vertices
        self._edges = edges
    
    @property
    def vertices(self) -> list[Vector3]:
        return self._vertices
    
    @property
    def edges(self) -> list[tuple]:
        return self._edges

    def update(self, dt: float) -> None: pass

    def move(self, velocity: Vector3) -> None:
        for vertex in self._vertices:
            vertex += velocity
