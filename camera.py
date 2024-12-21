"""
Created on 12/15/2024
by Jye-Ming Serres
"""
from pygame import Vector3

class Camera:
    """
    Camera doc
    """

    def __init__(self, aperture: Vector3 = Vector3(0, 0, 0), focal_length: float = 360) -> None:
        self._aperture = aperture
        self._image_x_vect = Vector3(0, -1, 0) # normalized vector
        self._image_y_vect = Vector3(0, 0, 1) # normalized vector
        self._orientation = self._calculate_orientation() # normalized vector
        self._focal_length = focal_length # will influence FOV since the size of the plane is finite and constant

        self.velocity = Vector3(0, 0, 0)
        self.angular_velocity = (0, 0) # angular velocity (in degrees) with respect to image_y_vect and image_x_vect, in that order
    
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
        return self._orientation

    @property
    def focal_length(self) -> float:
        return self._focal_length

    def update(self) -> None:
        self.move(self.velocity)
        self.rotate(self.angular_velocity)

    def move(self, velocity: Vector3) -> None:
        self._aperture += velocity

    def rotate(self, angular_velocity: tuple[int, int]) -> None:
        self.image_x_vect.rotate_ip(angular_velocity[0], self.image_y_vect)
        self.image_y_vect.rotate_ip(angular_velocity[1], self.image_x_vect)
        self._orientation = self._calculate_orientation()

    def _calculate_orientation(self) -> Vector3:
        # orientation vector is the vector normal to the projection plane (principal plane)
        return self._image_y_vect.cross(self._image_x_vect).normalize()
