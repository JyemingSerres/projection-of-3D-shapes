"""Provides a container class for shapes and the camera.

Classes:
    World
"""

from shape import Shape
from camera import Camera

__author__ = "Jye-Ming Serres"


class World:
    """Contains every shape and the camera. Acts as the model of the program.

    Methods:
        update()
    """

    def __init__(self, camera: Camera, shapes: list[Shape]) -> None:
        """Creates and instance containing the camera and shapes.

        Args:
            camera: A virtual camera controlled by the end user.
            shapes: The shapes that make up the world.

        Returns:
            None
        """
        self._shapes = shapes
        self._camera = camera

    @property
    def shapes(self) -> list[Shape]:
        return self._shapes

    @property
    def camera(self) -> Camera:
        return self._camera

    def update(self, dt: float) -> None:
        """Steps the camera and every shape across a time interval.

        Args:
            dt: Delta time (seconds).

        Returns:
            None    
        """
        for shape in self._shapes:
            shape.update(dt)
        self._camera.update(dt)
