"""
Created on 12/15/2024
by Jye-Ming Serres
"""
from shape import Shape
from camera import Camera

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

    def update(self) -> None:
        for shape in self._shapes:
            shape.update()
        self._camera.update()