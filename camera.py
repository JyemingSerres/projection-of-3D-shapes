"""
Created on 12/15/2024
by Jye-Ming Serres
"""
from pygame import Vector3

class Camera:
    """
    Camera doc
    """

    def __init__(self, aperture: Vector3=(0, 0, 0), image_plane_dist: float=25) -> None:
        self._aperture = aperture
        self._image_x_vect = Vector3(0, -1, 0) # normalized vector
        self._image_y_vect = Vector3(0, 0, 1) # normalized vector
        self._orientation = self.__orientation() # normalized vector
        self._image_plane_dist = image_plane_dist # will influence FOV since the size of the plane is finite and constant

        self.velocity = Vector3(0, 0, 0)
    
    @property
    def aperture(self) -> Vector3:
        return self._aperture

    @property
    def image_x_vect(self) -> Vector3:
        return self._image_x_vect

    @property
    def image_y_vect(self) -> Vector3:
        return self._image_y_vect

    @property
    def orientation(self) -> Vector3:
        # calculated every time it is accessed
        # TODO: problem: accessing this property multiple times per frame leads to waste of computational ressources
        return self.__orientation()

    @property
    def image_plane_dist(self) -> float:
        return self._image_plane_dist

    def update(self) -> None:
        # TODO: update camera position
        self.move(self.velocity)

        # TODO: update camera angles
        self.image_x_vect.rotate_ip_rad(-0.003, self.image_y_vect)
        pass

    def move(self, velocity: Vector3) -> None:
        self._aperture += velocity

    def __orientation(self) -> Vector3:
        # orientation vector is a normal vector to the projection plane
        return self._image_y_vect.cross(self._image_x_vect).normalize()
