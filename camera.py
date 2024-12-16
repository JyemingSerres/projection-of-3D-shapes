"""
Created on 12/15/2024
by Jye-Ming Serres
"""
from pygame import Vector3

class Camera:
    """
    Camera doc
    """
    DEFAULT_IMAGE_Y_VECT = Vector3(0, 0, 1)
    DEFAULT_IMAGE_X_VECT = Vector3(0, -1, 0)

    def __init__(self, center: tuple=(0, 0, 0), aperture_distance: float=25) -> None:
        # _center_pos is the principal point / image center
        self._center_pos = Vector3(center)
        self._image_x_vect = Camera.DEFAULT_IMAGE_X_VECT # needs to be normalized
        self._image_y_vect = Camera.DEFAULT_IMAGE_Y_VECT # needs to be normalized
        self._orientation = self.__orientation() # needs to be normalized
        self._aperture_distance = aperture_distance # aperture_distance will influence FOV
        self._pupil_pos = self.__aperture_pos()
    
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
        return self.__aperture_pos()

    def update(self) -> None:
        # TODO: update camera position
        self._center_pos += Vector3(0, 1, 0)
        # TODO: update camera angles
        pass

    def __aperture_pos(self) -> Vector3:
        return self._center_pos - self._aperture_distance*self._orientation

    def __orientation(self) -> Vector3:
        # orientation vector is the cross product (image_y) x (image_x)
        return self._image_y_vect.cross(self._image_x_vect)