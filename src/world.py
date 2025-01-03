"""
"""

from shape import Shape
from camera import Camera

__author__ = "Jye-Ming Serres"


class World:
    """
    World doc
    """

    def __init__(self, camera: Camera, shapes: list[Shape]) -> None:
        self._shapes = shapes
        self._camera = camera

    @property
    def shapes(self) -> list[Shape]:
        return self._shapes

    @property
    def camera(self) -> Camera:
        return self._camera

    def update(self, dt: float) -> None:
        for shape in self._shapes:
            shape.update(dt)
        self._camera.update(dt)
