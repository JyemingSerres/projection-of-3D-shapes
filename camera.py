"""
Created on 12/15/2024
by Jye-Ming Serres
"""
from pygame import Vector3

class Camera:
    """
    Camera doc
    """

    def __init__(self, center: tuple=(0, 0, 0), aperture_distance: float=25) -> None:
        self._center_pos = Vector3(center) # also the principal point / image center
        self._image_x_vect = Vector3(0, -1, 0) # normalized vector
        self._image_y_vect = Vector3(0, 0, 1) # normalized vector
        self._orientation = self.__orientation() # normalized vector
        self._aperture_distance = aperture_distance # aperture_distance will influence FOV
        self._aperture_pos = self.__aperture_pos()

        self.velocity = Vector3(0, 0, 0)
    
    @property
    def image_x_vect(self) -> Vector3:
        return self._image_x_vect

    @property
    def image_y_vect(self) -> Vector3:
        return self._image_y_vect

    @property
    def orientation(self) -> Vector3:
        # calculated every time it is accessed
        # could do otherwise if orientation is accessed multiple times per frame to optimize performance
        return self.__orientation()

    @property
    def aperture_distance(self) -> float:
        return self._aperture_distance
    
    @property
    def aperture_pos(self) -> Vector3:
        # calculated every time it is accessed
        # could do otherwise if orientation is accessed multiple times per frame to optimize performance
        return self.__aperture_pos()

    def update(self) -> None:
        # TODO: update camera position
        self.move(self.velocity)

        # TODO: update camera angles
        self.image_x_vect.rotate_ip_rad(-0.003, self.image_y_vect)
        pass

    def move(self, velocity: Vector3) -> None:
        self._center_pos += velocity

    def __aperture_pos(self) -> Vector3:
        return self._center_pos - self._aperture_distance*self._orientation

    def __orientation(self) -> Vector3:
        # orientation vector is the cross product (image_y) x (image_x)
        return self._image_y_vect.cross(self._image_x_vect).normalize()
